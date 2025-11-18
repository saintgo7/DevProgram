#[macro_use] extern crate rocket;

use rocket::serde::{json::Json, Deserialize, Serialize};
use rocket::State;
use std::sync::Mutex;

#[derive(Serialize, Deserialize, Clone)]
#[serde(crate = "rocket::serde")]
struct PaymentMethod {
    id: u64,
    name: String,
}

type PaymentMethodList = Mutex<Vec<PaymentMethod>>;

#[get("/paymentmethod")]
fn get_all(list: &State<PaymentMethodList>) -> Json<Vec<PaymentMethod>> {
    let items = list.lock().unwrap();
    Json(items.clone())
}

#[get("/paymentmethod/<id>")]
fn get_by_id(id: u64, list: &State<PaymentMethodList>) -> Option<Json<PaymentMethod>> {
    let items = list.lock().unwrap();
    items.iter()
        .find(|item| item.id == id)
        .map(|item| Json(item.clone()))
}

#[post("/paymentmethod", data = "<item>")]
fn create(item: Json<PaymentMethod>, list: &State<PaymentMethodList>) -> Json<PaymentMethod> {
    let mut items = list.lock().unwrap();
    items.push(item.clone());
    item
}

#[put("/paymentmethod/<id>", data = "<item>")]
fn update(id: u64, item: Json<PaymentMethod>, list: &State<PaymentMethodList>) -> Option<Json<PaymentMethod>> {
    let mut items = list.lock().unwrap();
    items.iter_mut()
        .find(|i| i.id == id)
        .map(|i| {
            *i = item.clone();
            Json(i.clone())
        })
}

#[delete("/paymentmethod/<id>")]
fn delete(id: u64, list: &State<PaymentMethodList>) -> Option<()> {
    let mut items = list.lock().unwrap();
    let pos = items.iter().position(|i| i.id == id)?;
    items.remove(pos);
    Some(())
}

#[launch]
fn rocket() -> _ {
    rocket::build()
        .manage(PaymentMethodList::new(Vec::new()))
        .mount("/api", routes![get_all, get_by_id, create, update, delete])
}
