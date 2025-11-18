#[macro_use] extern crate rocket;

use rocket::serde::{json::Json, Deserialize, Serialize};
use rocket::State;
use std::sync::Mutex;

#[derive(Serialize, Deserialize, Clone)]
#[serde(crate = "rocket::serde")]
struct Supplier {
    id: u64,
    name: String,
}

type SupplierList = Mutex<Vec<Supplier>>;

#[get("/supplier")]
fn get_all(list: &State<SupplierList>) -> Json<Vec<Supplier>> {
    let items = list.lock().unwrap();
    Json(items.clone())
}

#[get("/supplier/<id>")]
fn get_by_id(id: u64, list: &State<SupplierList>) -> Option<Json<Supplier>> {
    let items = list.lock().unwrap();
    items.iter()
        .find(|item| item.id == id)
        .map(|item| Json(item.clone()))
}

#[post("/supplier", data = "<item>")]
fn create(item: Json<Supplier>, list: &State<SupplierList>) -> Json<Supplier> {
    let mut items = list.lock().unwrap();
    items.push(item.clone());
    item
}

#[put("/supplier/<id>", data = "<item>")]
fn update(id: u64, item: Json<Supplier>, list: &State<SupplierList>) -> Option<Json<Supplier>> {
    let mut items = list.lock().unwrap();
    items.iter_mut()
        .find(|i| i.id == id)
        .map(|i| {
            *i = item.clone();
            Json(i.clone())
        })
}

#[delete("/supplier/<id>")]
fn delete(id: u64, list: &State<SupplierList>) -> Option<()> {
    let mut items = list.lock().unwrap();
    let pos = items.iter().position(|i| i.id == id)?;
    items.remove(pos);
    Some(())
}

#[launch]
fn rocket() -> _ {
    rocket::build()
        .manage(SupplierList::new(Vec::new()))
        .mount("/api", routes![get_all, get_by_id, create, update, delete])
}
