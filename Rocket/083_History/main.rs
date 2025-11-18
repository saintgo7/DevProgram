#[macro_use] extern crate rocket;

use rocket::serde::{json::Json, Deserialize, Serialize};
use rocket::State;
use std::sync::Mutex;

#[derive(Serialize, Deserialize, Clone)]
#[serde(crate = "rocket::serde")]
struct History {
    id: u64,
    name: String,
}

type HistoryList = Mutex<Vec<History>>;

#[get("/history")]
fn get_all(list: &State<HistoryList>) -> Json<Vec<History>> {
    let items = list.lock().unwrap();
    Json(items.clone())
}

#[get("/history/<id>")]
fn get_by_id(id: u64, list: &State<HistoryList>) -> Option<Json<History>> {
    let items = list.lock().unwrap();
    items.iter()
        .find(|item| item.id == id)
        .map(|item| Json(item.clone()))
}

#[post("/history", data = "<item>")]
fn create(item: Json<History>, list: &State<HistoryList>) -> Json<History> {
    let mut items = list.lock().unwrap();
    items.push(item.clone());
    item
}

#[put("/history/<id>", data = "<item>")]
fn update(id: u64, item: Json<History>, list: &State<HistoryList>) -> Option<Json<History>> {
    let mut items = list.lock().unwrap();
    items.iter_mut()
        .find(|i| i.id == id)
        .map(|i| {
            *i = item.clone();
            Json(i.clone())
        })
}

#[delete("/history/<id>")]
fn delete(id: u64, list: &State<HistoryList>) -> Option<()> {
    let mut items = list.lock().unwrap();
    let pos = items.iter().position(|i| i.id == id)?;
    items.remove(pos);
    Some(())
}

#[launch]
fn rocket() -> _ {
    rocket::build()
        .manage(HistoryList::new(Vec::new()))
        .mount("/api", routes![get_all, get_by_id, create, update, delete])
}
