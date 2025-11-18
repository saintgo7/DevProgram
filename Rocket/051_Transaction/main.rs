#[macro_use] extern crate rocket;

use rocket::serde::{json::Json, Deserialize, Serialize};
use rocket::State;
use std::sync::Mutex;

#[derive(Serialize, Deserialize, Clone)]
#[serde(crate = "rocket::serde")]
struct Transaction {
    id: u64,
    name: String,
}

type TransactionList = Mutex<Vec<Transaction>>;

#[get("/transaction")]
fn get_all(list: &State<TransactionList>) -> Json<Vec<Transaction>> {
    let items = list.lock().unwrap();
    Json(items.clone())
}

#[get("/transaction/<id>")]
fn get_by_id(id: u64, list: &State<TransactionList>) -> Option<Json<Transaction>> {
    let items = list.lock().unwrap();
    items.iter()
        .find(|item| item.id == id)
        .map(|item| Json(item.clone()))
}

#[post("/transaction", data = "<item>")]
fn create(item: Json<Transaction>, list: &State<TransactionList>) -> Json<Transaction> {
    let mut items = list.lock().unwrap();
    items.push(item.clone());
    item
}

#[put("/transaction/<id>", data = "<item>")]
fn update(id: u64, item: Json<Transaction>, list: &State<TransactionList>) -> Option<Json<Transaction>> {
    let mut items = list.lock().unwrap();
    items.iter_mut()
        .find(|i| i.id == id)
        .map(|i| {
            *i = item.clone();
            Json(i.clone())
        })
}

#[delete("/transaction/<id>")]
fn delete(id: u64, list: &State<TransactionList>) -> Option<()> {
    let mut items = list.lock().unwrap();
    let pos = items.iter().position(|i| i.id == id)?;
    items.remove(pos);
    Some(())
}

#[launch]
fn rocket() -> _ {
    rocket::build()
        .manage(TransactionList::new(Vec::new()))
        .mount("/api", routes![get_all, get_by_id, create, update, delete])
}
