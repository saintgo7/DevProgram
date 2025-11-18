#[macro_use] extern crate rocket;

use rocket::serde::{json::Json, Deserialize, Serialize};
use rocket::State;
use std::sync::Mutex;

#[derive(Serialize, Deserialize, Clone)]
#[serde(crate = "rocket::serde")]
struct Invoice {
    id: u64,
    name: String,
}

type InvoiceList = Mutex<Vec<Invoice>>;

#[get("/invoice")]
fn get_all(list: &State<InvoiceList>) -> Json<Vec<Invoice>> {
    let items = list.lock().unwrap();
    Json(items.clone())
}

#[get("/invoice/<id>")]
fn get_by_id(id: u64, list: &State<InvoiceList>) -> Option<Json<Invoice>> {
    let items = list.lock().unwrap();
    items.iter()
        .find(|item| item.id == id)
        .map(|item| Json(item.clone()))
}

#[post("/invoice", data = "<item>")]
fn create(item: Json<Invoice>, list: &State<InvoiceList>) -> Json<Invoice> {
    let mut items = list.lock().unwrap();
    items.push(item.clone());
    item
}

#[put("/invoice/<id>", data = "<item>")]
fn update(id: u64, item: Json<Invoice>, list: &State<InvoiceList>) -> Option<Json<Invoice>> {
    let mut items = list.lock().unwrap();
    items.iter_mut()
        .find(|i| i.id == id)
        .map(|i| {
            *i = item.clone();
            Json(i.clone())
        })
}

#[delete("/invoice/<id>")]
fn delete(id: u64, list: &State<InvoiceList>) -> Option<()> {
    let mut items = list.lock().unwrap();
    let pos = items.iter().position(|i| i.id == id)?;
    items.remove(pos);
    Some(())
}

#[launch]
fn rocket() -> _ {
    rocket::build()
        .manage(InvoiceList::new(Vec::new()))
        .mount("/api", routes![get_all, get_by_id, create, update, delete])
}
