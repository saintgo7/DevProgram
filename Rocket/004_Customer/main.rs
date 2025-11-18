#[macro_use] extern crate rocket;

use rocket::serde::{json::Json, Deserialize, Serialize};
use rocket::State;
use std::sync::Mutex;

#[derive(Serialize, Deserialize, Clone)]
#[serde(crate = "rocket::serde")]
struct Customer {
    id: u64,
    name: String,
}

type CustomerList = Mutex<Vec<Customer>>;

#[get("/customer")]
fn get_all(list: &State<CustomerList>) -> Json<Vec<Customer>> {
    let items = list.lock().unwrap();
    Json(items.clone())
}

#[get("/customer/<id>")]
fn get_by_id(id: u64, list: &State<CustomerList>) -> Option<Json<Customer>> {
    let items = list.lock().unwrap();
    items.iter()
        .find(|item| item.id == id)
        .map(|item| Json(item.clone()))
}

#[post("/customer", data = "<item>")]
fn create(item: Json<Customer>, list: &State<CustomerList>) -> Json<Customer> {
    let mut items = list.lock().unwrap();
    items.push(item.clone());
    item
}

#[put("/customer/<id>", data = "<item>")]
fn update(id: u64, item: Json<Customer>, list: &State<CustomerList>) -> Option<Json<Customer>> {
    let mut items = list.lock().unwrap();
    items.iter_mut()
        .find(|i| i.id == id)
        .map(|i| {
            *i = item.clone();
            Json(i.clone())
        })
}

#[delete("/customer/<id>")]
fn delete(id: u64, list: &State<CustomerList>) -> Option<()> {
    let mut items = list.lock().unwrap();
    let pos = items.iter().position(|i| i.id == id)?;
    items.remove(pos);
    Some(())
}

#[launch]
fn rocket() -> _ {
    rocket::build()
        .manage(CustomerList::new(Vec::new()))
        .mount("/api", routes![get_all, get_by_id, create, update, delete])
}
