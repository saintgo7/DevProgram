#[macro_use] extern crate rocket;

use rocket::serde::{json::Json, Deserialize, Serialize};
use rocket::State;
use std::sync::Mutex;

#[derive(Serialize, Deserialize, Clone)]
#[serde(crate = "rocket::serde")]
struct VAT {
    id: u64,
    name: String,
}

type VATList = Mutex<Vec<VAT>>;

#[get("/vat")]
fn get_all(list: &State<VATList>) -> Json<Vec<VAT>> {
    let items = list.lock().unwrap();
    Json(items.clone())
}

#[get("/vat/<id>")]
fn get_by_id(id: u64, list: &State<VATList>) -> Option<Json<VAT>> {
    let items = list.lock().unwrap();
    items.iter()
        .find(|item| item.id == id)
        .map(|item| Json(item.clone()))
}

#[post("/vat", data = "<item>")]
fn create(item: Json<VAT>, list: &State<VATList>) -> Json<VAT> {
    let mut items = list.lock().unwrap();
    items.push(item.clone());
    item
}

#[put("/vat/<id>", data = "<item>")]
fn update(id: u64, item: Json<VAT>, list: &State<VATList>) -> Option<Json<VAT>> {
    let mut items = list.lock().unwrap();
    items.iter_mut()
        .find(|i| i.id == id)
        .map(|i| {
            *i = item.clone();
            Json(i.clone())
        })
}

#[delete("/vat/<id>")]
fn delete(id: u64, list: &State<VATList>) -> Option<()> {
    let mut items = list.lock().unwrap();
    let pos = items.iter().position(|i| i.id == id)?;
    items.remove(pos);
    Some(())
}

#[launch]
fn rocket() -> _ {
    rocket::build()
        .manage(VATList::new(Vec::new()))
        .mount("/api", routes![get_all, get_by_id, create, update, delete])
}
