#[macro_use] extern crate rocket;

use rocket::serde::{json::Json, Deserialize, Serialize};
use rocket::State;
use std::sync::Mutex;

#[derive(Serialize, Deserialize, Clone)]
#[serde(crate = "rocket::serde")]
struct Cache {
    id: u64,
    name: String,
}

type CacheList = Mutex<Vec<Cache>>;

#[get("/cache")]
fn get_all(list: &State<CacheList>) -> Json<Vec<Cache>> {
    let items = list.lock().unwrap();
    Json(items.clone())
}

#[get("/cache/<id>")]
fn get_by_id(id: u64, list: &State<CacheList>) -> Option<Json<Cache>> {
    let items = list.lock().unwrap();
    items.iter()
        .find(|item| item.id == id)
        .map(|item| Json(item.clone()))
}

#[post("/cache", data = "<item>")]
fn create(item: Json<Cache>, list: &State<CacheList>) -> Json<Cache> {
    let mut items = list.lock().unwrap();
    items.push(item.clone());
    item
}

#[put("/cache/<id>", data = "<item>")]
fn update(id: u64, item: Json<Cache>, list: &State<CacheList>) -> Option<Json<Cache>> {
    let mut items = list.lock().unwrap();
    items.iter_mut()
        .find(|i| i.id == id)
        .map(|i| {
            *i = item.clone();
            Json(i.clone())
        })
}

#[delete("/cache/<id>")]
fn delete(id: u64, list: &State<CacheList>) -> Option<()> {
    let mut items = list.lock().unwrap();
    let pos = items.iter().position(|i| i.id == id)?;
    items.remove(pos);
    Some(())
}

#[launch]
fn rocket() -> _ {
    rocket::build()
        .manage(CacheList::new(Vec::new()))
        .mount("/api", routes![get_all, get_by_id, create, update, delete])
}
