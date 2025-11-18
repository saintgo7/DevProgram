#[macro_use] extern crate rocket;

use rocket::serde::{json::Json, Deserialize, Serialize};
use rocket::State;
use std::sync::Mutex;

#[derive(Serialize, Deserialize, Clone)]
#[serde(crate = "rocket::serde")]
struct Delivery {
    id: u64,
    name: String,
}

type DeliveryList = Mutex<Vec<Delivery>>;

#[get("/delivery")]
fn get_all(list: &State<DeliveryList>) -> Json<Vec<Delivery>> {
    let items = list.lock().unwrap();
    Json(items.clone())
}

#[get("/delivery/<id>")]
fn get_by_id(id: u64, list: &State<DeliveryList>) -> Option<Json<Delivery>> {
    let items = list.lock().unwrap();
    items.iter()
        .find(|item| item.id == id)
        .map(|item| Json(item.clone()))
}

#[post("/delivery", data = "<item>")]
fn create(item: Json<Delivery>, list: &State<DeliveryList>) -> Json<Delivery> {
    let mut items = list.lock().unwrap();
    items.push(item.clone());
    item
}

#[put("/delivery/<id>", data = "<item>")]
fn update(id: u64, item: Json<Delivery>, list: &State<DeliveryList>) -> Option<Json<Delivery>> {
    let mut items = list.lock().unwrap();
    items.iter_mut()
        .find(|i| i.id == id)
        .map(|i| {
            *i = item.clone();
            Json(i.clone())
        })
}

#[delete("/delivery/<id>")]
fn delete(id: u64, list: &State<DeliveryList>) -> Option<()> {
    let mut items = list.lock().unwrap();
    let pos = items.iter().position(|i| i.id == id)?;
    items.remove(pos);
    Some(())
}

#[launch]
fn rocket() -> _ {
    rocket::build()
        .manage(DeliveryList::new(Vec::new()))
        .mount("/api", routes![get_all, get_by_id, create, update, delete])
}
