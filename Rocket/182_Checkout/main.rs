#[macro_use] extern crate rocket;

use rocket::serde::{json::Json, Deserialize, Serialize};
use rocket::State;
use std::sync::Mutex;

#[derive(Serialize, Deserialize, Clone)]
#[serde(crate = "rocket::serde")]
struct Checkout {
    id: u64,
    name: String,
}

type CheckoutList = Mutex<Vec<Checkout>>;

#[get("/checkout")]
fn get_all(list: &State<CheckoutList>) -> Json<Vec<Checkout>> {
    let items = list.lock().unwrap();
    Json(items.clone())
}

#[get("/checkout/<id>")]
fn get_by_id(id: u64, list: &State<CheckoutList>) -> Option<Json<Checkout>> {
    let items = list.lock().unwrap();
    items.iter()
        .find(|item| item.id == id)
        .map(|item| Json(item.clone()))
}

#[post("/checkout", data = "<item>")]
fn create(item: Json<Checkout>, list: &State<CheckoutList>) -> Json<Checkout> {
    let mut items = list.lock().unwrap();
    items.push(item.clone());
    item
}

#[put("/checkout/<id>", data = "<item>")]
fn update(id: u64, item: Json<Checkout>, list: &State<CheckoutList>) -> Option<Json<Checkout>> {
    let mut items = list.lock().unwrap();
    items.iter_mut()
        .find(|i| i.id == id)
        .map(|i| {
            *i = item.clone();
            Json(i.clone())
        })
}

#[delete("/checkout/<id>")]
fn delete(id: u64, list: &State<CheckoutList>) -> Option<()> {
    let mut items = list.lock().unwrap();
    let pos = items.iter().position(|i| i.id == id)?;
    items.remove(pos);
    Some(())
}

#[launch]
fn rocket() -> _ {
    rocket::build()
        .manage(CheckoutList::new(Vec::new()))
        .mount("/api", routes![get_all, get_by_id, create, update, delete])
}
