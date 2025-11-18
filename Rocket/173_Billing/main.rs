#[macro_use] extern crate rocket;

use rocket::serde::{json::Json, Deserialize, Serialize};
use rocket::State;
use std::sync::Mutex;

#[derive(Serialize, Deserialize, Clone)]
#[serde(crate = "rocket::serde")]
struct Billing {
    id: u64,
    name: String,
}

type BillingList = Mutex<Vec<Billing>>;

#[get("/billing")]
fn get_all(list: &State<BillingList>) -> Json<Vec<Billing>> {
    let items = list.lock().unwrap();
    Json(items.clone())
}

#[get("/billing/<id>")]
fn get_by_id(id: u64, list: &State<BillingList>) -> Option<Json<Billing>> {
    let items = list.lock().unwrap();
    items.iter()
        .find(|item| item.id == id)
        .map(|item| Json(item.clone()))
}

#[post("/billing", data = "<item>")]
fn create(item: Json<Billing>, list: &State<BillingList>) -> Json<Billing> {
    let mut items = list.lock().unwrap();
    items.push(item.clone());
    item
}

#[put("/billing/<id>", data = "<item>")]
fn update(id: u64, item: Json<Billing>, list: &State<BillingList>) -> Option<Json<Billing>> {
    let mut items = list.lock().unwrap();
    items.iter_mut()
        .find(|i| i.id == id)
        .map(|i| {
            *i = item.clone();
            Json(i.clone())
        })
}

#[delete("/billing/<id>")]
fn delete(id: u64, list: &State<BillingList>) -> Option<()> {
    let mut items = list.lock().unwrap();
    let pos = items.iter().position(|i| i.id == id)?;
    items.remove(pos);
    Some(())
}

#[launch]
fn rocket() -> _ {
    rocket::build()
        .manage(BillingList::new(Vec::new()))
        .mount("/api", routes![get_all, get_by_id, create, update, delete])
}
