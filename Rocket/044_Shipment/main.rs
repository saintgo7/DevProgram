#[macro_use] extern crate rocket;

use rocket::serde::{json::Json, Deserialize, Serialize};
use rocket::State;
use std::sync::Mutex;

#[derive(Serialize, Deserialize, Clone)]
#[serde(crate = "rocket::serde")]
struct Shipment {
    id: u64,
    name: String,
}

type ShipmentList = Mutex<Vec<Shipment>>;

#[get("/shipment")]
fn get_all(list: &State<ShipmentList>) -> Json<Vec<Shipment>> {
    let items = list.lock().unwrap();
    Json(items.clone())
}

#[get("/shipment/<id>")]
fn get_by_id(id: u64, list: &State<ShipmentList>) -> Option<Json<Shipment>> {
    let items = list.lock().unwrap();
    items.iter()
        .find(|item| item.id == id)
        .map(|item| Json(item.clone()))
}

#[post("/shipment", data = "<item>")]
fn create(item: Json<Shipment>, list: &State<ShipmentList>) -> Json<Shipment> {
    let mut items = list.lock().unwrap();
    items.push(item.clone());
    item
}

#[put("/shipment/<id>", data = "<item>")]
fn update(id: u64, item: Json<Shipment>, list: &State<ShipmentList>) -> Option<Json<Shipment>> {
    let mut items = list.lock().unwrap();
    items.iter_mut()
        .find(|i| i.id == id)
        .map(|i| {
            *i = item.clone();
            Json(i.clone())
        })
}

#[delete("/shipment/<id>")]
fn delete(id: u64, list: &State<ShipmentList>) -> Option<()> {
    let mut items = list.lock().unwrap();
    let pos = items.iter().position(|i| i.id == id)?;
    items.remove(pos);
    Some(())
}

#[launch]
fn rocket() -> _ {
    rocket::build()
        .manage(ShipmentList::new(Vec::new()))
        .mount("/api", routes![get_all, get_by_id, create, update, delete])
}
