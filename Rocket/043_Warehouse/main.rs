#[macro_use] extern crate rocket;

use rocket::serde::{json::Json, Deserialize, Serialize};
use rocket::State;
use std::sync::Mutex;

#[derive(Serialize, Deserialize, Clone)]
#[serde(crate = "rocket::serde")]
struct Warehouse {
    id: u64,
    name: String,
}

type WarehouseList = Mutex<Vec<Warehouse>>;

#[get("/warehouse")]
fn get_all(list: &State<WarehouseList>) -> Json<Vec<Warehouse>> {
    let items = list.lock().unwrap();
    Json(items.clone())
}

#[get("/warehouse/<id>")]
fn get_by_id(id: u64, list: &State<WarehouseList>) -> Option<Json<Warehouse>> {
    let items = list.lock().unwrap();
    items.iter()
        .find(|item| item.id == id)
        .map(|item| Json(item.clone()))
}

#[post("/warehouse", data = "<item>")]
fn create(item: Json<Warehouse>, list: &State<WarehouseList>) -> Json<Warehouse> {
    let mut items = list.lock().unwrap();
    items.push(item.clone());
    item
}

#[put("/warehouse/<id>", data = "<item>")]
fn update(id: u64, item: Json<Warehouse>, list: &State<WarehouseList>) -> Option<Json<Warehouse>> {
    let mut items = list.lock().unwrap();
    items.iter_mut()
        .find(|i| i.id == id)
        .map(|i| {
            *i = item.clone();
            Json(i.clone())
        })
}

#[delete("/warehouse/<id>")]
fn delete(id: u64, list: &State<WarehouseList>) -> Option<()> {
    let mut items = list.lock().unwrap();
    let pos = items.iter().position(|i| i.id == id)?;
    items.remove(pos);
    Some(())
}

#[launch]
fn rocket() -> _ {
    rocket::build()
        .manage(WarehouseList::new(Vec::new()))
        .mount("/api", routes![get_all, get_by_id, create, update, delete])
}
