#[macro_use] extern crate rocket;

use rocket::serde::{json::Json, Deserialize, Serialize};
use rocket::State;
use std::sync::Mutex;

#[derive(Serialize, Deserialize, Clone)]
#[serde(crate = "rocket::serde")]
struct Adapter {
    id: u64,
    name: String,
}

type AdapterList = Mutex<Vec<Adapter>>;

#[get("/adapter")]
fn get_all(list: &State<AdapterList>) -> Json<Vec<Adapter>> {
    let items = list.lock().unwrap();
    Json(items.clone())
}

#[get("/adapter/<id>")]
fn get_by_id(id: u64, list: &State<AdapterList>) -> Option<Json<Adapter>> {
    let items = list.lock().unwrap();
    items.iter()
        .find(|item| item.id == id)
        .map(|item| Json(item.clone()))
}

#[post("/adapter", data = "<item>")]
fn create(item: Json<Adapter>, list: &State<AdapterList>) -> Json<Adapter> {
    let mut items = list.lock().unwrap();
    items.push(item.clone());
    item
}

#[put("/adapter/<id>", data = "<item>")]
fn update(id: u64, item: Json<Adapter>, list: &State<AdapterList>) -> Option<Json<Adapter>> {
    let mut items = list.lock().unwrap();
    items.iter_mut()
        .find(|i| i.id == id)
        .map(|i| {
            *i = item.clone();
            Json(i.clone())
        })
}

#[delete("/adapter/<id>")]
fn delete(id: u64, list: &State<AdapterList>) -> Option<()> {
    let mut items = list.lock().unwrap();
    let pos = items.iter().position(|i| i.id == id)?;
    items.remove(pos);
    Some(())
}

#[launch]
fn rocket() -> _ {
    rocket::build()
        .manage(AdapterList::new(Vec::new()))
        .mount("/api", routes![get_all, get_by_id, create, update, delete])
}
