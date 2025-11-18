#[macro_use] extern crate rocket;

use rocket::serde::{json::Json, Deserialize, Serialize};
use rocket::State;
use std::sync::Mutex;

#[derive(Serialize, Deserialize, Clone)]
#[serde(crate = "rocket::serde")]
struct Shipping {
    id: u64,
    name: String,
}

type ShippingList = Mutex<Vec<Shipping>>;

#[get("/shipping")]
fn get_all(list: &State<ShippingList>) -> Json<Vec<Shipping>> {
    let items = list.lock().unwrap();
    Json(items.clone())
}

#[get("/shipping/<id>")]
fn get_by_id(id: u64, list: &State<ShippingList>) -> Option<Json<Shipping>> {
    let items = list.lock().unwrap();
    items.iter()
        .find(|item| item.id == id)
        .map(|item| Json(item.clone()))
}

#[post("/shipping", data = "<item>")]
fn create(item: Json<Shipping>, list: &State<ShippingList>) -> Json<Shipping> {
    let mut items = list.lock().unwrap();
    items.push(item.clone());
    item
}

#[put("/shipping/<id>", data = "<item>")]
fn update(id: u64, item: Json<Shipping>, list: &State<ShippingList>) -> Option<Json<Shipping>> {
    let mut items = list.lock().unwrap();
    items.iter_mut()
        .find(|i| i.id == id)
        .map(|i| {
            *i = item.clone();
            Json(i.clone())
        })
}

#[delete("/shipping/<id>")]
fn delete(id: u64, list: &State<ShippingList>) -> Option<()> {
    let mut items = list.lock().unwrap();
    let pos = items.iter().position(|i| i.id == id)?;
    items.remove(pos);
    Some(())
}

#[launch]
fn rocket() -> _ {
    rocket::build()
        .manage(ShippingList::new(Vec::new()))
        .mount("/api", routes![get_all, get_by_id, create, update, delete])
}
