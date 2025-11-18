#[macro_use] extern crate rocket;

use rocket::serde::{json::Json, Deserialize, Serialize};
use rocket::State;
use std::sync::Mutex;

#[derive(Serialize, Deserialize, Clone)]
#[serde(crate = "rocket::serde")]
struct PayPal {
    id: u64,
    name: String,
}

type PayPalList = Mutex<Vec<PayPal>>;

#[get("/paypal")]
fn get_all(list: &State<PayPalList>) -> Json<Vec<PayPal>> {
    let items = list.lock().unwrap();
    Json(items.clone())
}

#[get("/paypal/<id>")]
fn get_by_id(id: u64, list: &State<PayPalList>) -> Option<Json<PayPal>> {
    let items = list.lock().unwrap();
    items.iter()
        .find(|item| item.id == id)
        .map(|item| Json(item.clone()))
}

#[post("/paypal", data = "<item>")]
fn create(item: Json<PayPal>, list: &State<PayPalList>) -> Json<PayPal> {
    let mut items = list.lock().unwrap();
    items.push(item.clone());
    item
}

#[put("/paypal/<id>", data = "<item>")]
fn update(id: u64, item: Json<PayPal>, list: &State<PayPalList>) -> Option<Json<PayPal>> {
    let mut items = list.lock().unwrap();
    items.iter_mut()
        .find(|i| i.id == id)
        .map(|i| {
            *i = item.clone();
            Json(i.clone())
        })
}

#[delete("/paypal/<id>")]
fn delete(id: u64, list: &State<PayPalList>) -> Option<()> {
    let mut items = list.lock().unwrap();
    let pos = items.iter().position(|i| i.id == id)?;
    items.remove(pos);
    Some(())
}

#[launch]
fn rocket() -> _ {
    rocket::build()
        .manage(PayPalList::new(Vec::new()))
        .mount("/api", routes![get_all, get_by_id, create, update, delete])
}
