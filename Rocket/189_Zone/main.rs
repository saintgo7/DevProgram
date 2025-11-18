#[macro_use] extern crate rocket;

use rocket::serde::{json::Json, Deserialize, Serialize};
use rocket::State;
use std::sync::Mutex;

#[derive(Serialize, Deserialize, Clone)]
#[serde(crate = "rocket::serde")]
struct Zone {
    id: u64,
    name: String,
}

type ZoneList = Mutex<Vec<Zone>>;

#[get("/zone")]
fn get_all(list: &State<ZoneList>) -> Json<Vec<Zone>> {
    let items = list.lock().unwrap();
    Json(items.clone())
}

#[get("/zone/<id>")]
fn get_by_id(id: u64, list: &State<ZoneList>) -> Option<Json<Zone>> {
    let items = list.lock().unwrap();
    items.iter()
        .find(|item| item.id == id)
        .map(|item| Json(item.clone()))
}

#[post("/zone", data = "<item>")]
fn create(item: Json<Zone>, list: &State<ZoneList>) -> Json<Zone> {
    let mut items = list.lock().unwrap();
    items.push(item.clone());
    item
}

#[put("/zone/<id>", data = "<item>")]
fn update(id: u64, item: Json<Zone>, list: &State<ZoneList>) -> Option<Json<Zone>> {
    let mut items = list.lock().unwrap();
    items.iter_mut()
        .find(|i| i.id == id)
        .map(|i| {
            *i = item.clone();
            Json(i.clone())
        })
}

#[delete("/zone/<id>")]
fn delete(id: u64, list: &State<ZoneList>) -> Option<()> {
    let mut items = list.lock().unwrap();
    let pos = items.iter().position(|i| i.id == id)?;
    items.remove(pos);
    Some(())
}

#[launch]
fn rocket() -> _ {
    rocket::build()
        .manage(ZoneList::new(Vec::new()))
        .mount("/api", routes![get_all, get_by_id, create, update, delete])
}
