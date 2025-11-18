#[macro_use] extern crate rocket;

use rocket::serde::{json::Json, Deserialize, Serialize};
use rocket::State;
use std::sync::Mutex;

#[derive(Serialize, Deserialize, Clone)]
#[serde(crate = "rocket::serde")]
struct Stock {
    id: u64,
    name: String,
}

type StockList = Mutex<Vec<Stock>>;

#[get("/stock")]
fn get_all(list: &State<StockList>) -> Json<Vec<Stock>> {
    let items = list.lock().unwrap();
    Json(items.clone())
}

#[get("/stock/<id>")]
fn get_by_id(id: u64, list: &State<StockList>) -> Option<Json<Stock>> {
    let items = list.lock().unwrap();
    items.iter()
        .find(|item| item.id == id)
        .map(|item| Json(item.clone()))
}

#[post("/stock", data = "<item>")]
fn create(item: Json<Stock>, list: &State<StockList>) -> Json<Stock> {
    let mut items = list.lock().unwrap();
    items.push(item.clone());
    item
}

#[put("/stock/<id>", data = "<item>")]
fn update(id: u64, item: Json<Stock>, list: &State<StockList>) -> Option<Json<Stock>> {
    let mut items = list.lock().unwrap();
    items.iter_mut()
        .find(|i| i.id == id)
        .map(|i| {
            *i = item.clone();
            Json(i.clone())
        })
}

#[delete("/stock/<id>")]
fn delete(id: u64, list: &State<StockList>) -> Option<()> {
    let mut items = list.lock().unwrap();
    let pos = items.iter().position(|i| i.id == id)?;
    items.remove(pos);
    Some(())
}

#[launch]
fn rocket() -> _ {
    rocket::build()
        .manage(StockList::new(Vec::new()))
        .mount("/api", routes![get_all, get_by_id, create, update, delete])
}
