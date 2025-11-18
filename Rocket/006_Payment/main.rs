#[macro_use] extern crate rocket;

use rocket::serde::{json::Json, Deserialize, Serialize};
use rocket::State;
use std::sync::Mutex;

#[derive(Serialize, Deserialize, Clone)]
#[serde(crate = "rocket::serde")]
struct Payment {
    id: u64,
    name: String,
}

type PaymentList = Mutex<Vec<Payment>>;

#[get("/payment")]
fn get_all(list: &State<PaymentList>) -> Json<Vec<Payment>> {
    let items = list.lock().unwrap();
    Json(items.clone())
}

#[get("/payment/<id>")]
fn get_by_id(id: u64, list: &State<PaymentList>) -> Option<Json<Payment>> {
    let items = list.lock().unwrap();
    items.iter()
        .find(|item| item.id == id)
        .map(|item| Json(item.clone()))
}

#[post("/payment", data = "<item>")]
fn create(item: Json<Payment>, list: &State<PaymentList>) -> Json<Payment> {
    let mut items = list.lock().unwrap();
    items.push(item.clone());
    item
}

#[put("/payment/<id>", data = "<item>")]
fn update(id: u64, item: Json<Payment>, list: &State<PaymentList>) -> Option<Json<Payment>> {
    let mut items = list.lock().unwrap();
    items.iter_mut()
        .find(|i| i.id == id)
        .map(|i| {
            *i = item.clone();
            Json(i.clone())
        })
}

#[delete("/payment/<id>")]
fn delete(id: u64, list: &State<PaymentList>) -> Option<()> {
    let mut items = list.lock().unwrap();
    let pos = items.iter().position(|i| i.id == id)?;
    items.remove(pos);
    Some(())
}

#[launch]
fn rocket() -> _ {
    rocket::build()
        .manage(PaymentList::new(Vec::new()))
        .mount("/api", routes![get_all, get_by_id, create, update, delete])
}
