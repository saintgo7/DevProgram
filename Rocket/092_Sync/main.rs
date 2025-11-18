#[macro_use] extern crate rocket;

use rocket::serde::{json::Json, Deserialize, Serialize};
use rocket::State;
use std::sync::Mutex;

#[derive(Serialize, Deserialize, Clone)]
#[serde(crate = "rocket::serde")]
struct Sync {
    id: u64,
    name: String,
}

type SyncList = Mutex<Vec<Sync>>;

#[get("/sync")]
fn get_all(list: &State<SyncList>) -> Json<Vec<Sync>> {
    let items = list.lock().unwrap();
    Json(items.clone())
}

#[get("/sync/<id>")]
fn get_by_id(id: u64, list: &State<SyncList>) -> Option<Json<Sync>> {
    let items = list.lock().unwrap();
    items.iter()
        .find(|item| item.id == id)
        .map(|item| Json(item.clone()))
}

#[post("/sync", data = "<item>")]
fn create(item: Json<Sync>, list: &State<SyncList>) -> Json<Sync> {
    let mut items = list.lock().unwrap();
    items.push(item.clone());
    item
}

#[put("/sync/<id>", data = "<item>")]
fn update(id: u64, item: Json<Sync>, list: &State<SyncList>) -> Option<Json<Sync>> {
    let mut items = list.lock().unwrap();
    items.iter_mut()
        .find(|i| i.id == id)
        .map(|i| {
            *i = item.clone();
            Json(i.clone())
        })
}

#[delete("/sync/<id>")]
fn delete(id: u64, list: &State<SyncList>) -> Option<()> {
    let mut items = list.lock().unwrap();
    let pos = items.iter().position(|i| i.id == id)?;
    items.remove(pos);
    Some(())
}

#[launch]
fn rocket() -> _ {
    rocket::build()
        .manage(SyncList::new(Vec::new()))
        .mount("/api", routes![get_all, get_by_id, create, update, delete])
}
