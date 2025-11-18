#[macro_use] extern crate rocket;

use rocket::serde::{json::Json, Deserialize, Serialize};
use rocket::State;
use std::sync::Mutex;

#[derive(Serialize, Deserialize, Clone)]
#[serde(crate = "rocket::serde")]
struct Location {
    id: u64,
    name: String,
}

type LocationList = Mutex<Vec<Location>>;

#[get("/location")]
fn get_all(list: &State<LocationList>) -> Json<Vec<Location>> {
    let items = list.lock().unwrap();
    Json(items.clone())
}

#[get("/location/<id>")]
fn get_by_id(id: u64, list: &State<LocationList>) -> Option<Json<Location>> {
    let items = list.lock().unwrap();
    items.iter()
        .find(|item| item.id == id)
        .map(|item| Json(item.clone()))
}

#[post("/location", data = "<item>")]
fn create(item: Json<Location>, list: &State<LocationList>) -> Json<Location> {
    let mut items = list.lock().unwrap();
    items.push(item.clone());
    item
}

#[put("/location/<id>", data = "<item>")]
fn update(id: u64, item: Json<Location>, list: &State<LocationList>) -> Option<Json<Location>> {
    let mut items = list.lock().unwrap();
    items.iter_mut()
        .find(|i| i.id == id)
        .map(|i| {
            *i = item.clone();
            Json(i.clone())
        })
}

#[delete("/location/<id>")]
fn delete(id: u64, list: &State<LocationList>) -> Option<()> {
    let mut items = list.lock().unwrap();
    let pos = items.iter().position(|i| i.id == id)?;
    items.remove(pos);
    Some(())
}

#[launch]
fn rocket() -> _ {
    rocket::build()
        .manage(LocationList::new(Vec::new()))
        .mount("/api", routes![get_all, get_by_id, create, update, delete])
}
