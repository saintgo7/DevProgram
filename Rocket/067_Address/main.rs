#[macro_use] extern crate rocket;

use rocket::serde::{json::Json, Deserialize, Serialize};
use rocket::State;
use std::sync::Mutex;

#[derive(Serialize, Deserialize, Clone)]
#[serde(crate = "rocket::serde")]
struct Address {
    id: u64,
    name: String,
}

type AddressList = Mutex<Vec<Address>>;

#[get("/address")]
fn get_all(list: &State<AddressList>) -> Json<Vec<Address>> {
    let items = list.lock().unwrap();
    Json(items.clone())
}

#[get("/address/<id>")]
fn get_by_id(id: u64, list: &State<AddressList>) -> Option<Json<Address>> {
    let items = list.lock().unwrap();
    items.iter()
        .find(|item| item.id == id)
        .map(|item| Json(item.clone()))
}

#[post("/address", data = "<item>")]
fn create(item: Json<Address>, list: &State<AddressList>) -> Json<Address> {
    let mut items = list.lock().unwrap();
    items.push(item.clone());
    item
}

#[put("/address/<id>", data = "<item>")]
fn update(id: u64, item: Json<Address>, list: &State<AddressList>) -> Option<Json<Address>> {
    let mut items = list.lock().unwrap();
    items.iter_mut()
        .find(|i| i.id == id)
        .map(|i| {
            *i = item.clone();
            Json(i.clone())
        })
}

#[delete("/address/<id>")]
fn delete(id: u64, list: &State<AddressList>) -> Option<()> {
    let mut items = list.lock().unwrap();
    let pos = items.iter().position(|i| i.id == id)?;
    items.remove(pos);
    Some(())
}

#[launch]
fn rocket() -> _ {
    rocket::build()
        .manage(AddressList::new(Vec::new()))
        .mount("/api", routes![get_all, get_by_id, create, update, delete])
}
