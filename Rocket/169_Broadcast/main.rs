#[macro_use] extern crate rocket;

use rocket::serde::{json::Json, Deserialize, Serialize};
use rocket::State;
use std::sync::Mutex;

#[derive(Serialize, Deserialize, Clone)]
#[serde(crate = "rocket::serde")]
struct Broadcast {
    id: u64,
    name: String,
}

type BroadcastList = Mutex<Vec<Broadcast>>;

#[get("/broadcast")]
fn get_all(list: &State<BroadcastList>) -> Json<Vec<Broadcast>> {
    let items = list.lock().unwrap();
    Json(items.clone())
}

#[get("/broadcast/<id>")]
fn get_by_id(id: u64, list: &State<BroadcastList>) -> Option<Json<Broadcast>> {
    let items = list.lock().unwrap();
    items.iter()
        .find(|item| item.id == id)
        .map(|item| Json(item.clone()))
}

#[post("/broadcast", data = "<item>")]
fn create(item: Json<Broadcast>, list: &State<BroadcastList>) -> Json<Broadcast> {
    let mut items = list.lock().unwrap();
    items.push(item.clone());
    item
}

#[put("/broadcast/<id>", data = "<item>")]
fn update(id: u64, item: Json<Broadcast>, list: &State<BroadcastList>) -> Option<Json<Broadcast>> {
    let mut items = list.lock().unwrap();
    items.iter_mut()
        .find(|i| i.id == id)
        .map(|i| {
            *i = item.clone();
            Json(i.clone())
        })
}

#[delete("/broadcast/<id>")]
fn delete(id: u64, list: &State<BroadcastList>) -> Option<()> {
    let mut items = list.lock().unwrap();
    let pos = items.iter().position(|i| i.id == id)?;
    items.remove(pos);
    Some(())
}

#[launch]
fn rocket() -> _ {
    rocket::build()
        .manage(BroadcastList::new(Vec::new()))
        .mount("/api", routes![get_all, get_by_id, create, update, delete])
}
