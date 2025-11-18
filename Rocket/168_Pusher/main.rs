#[macro_use] extern crate rocket;

use rocket::serde::{json::Json, Deserialize, Serialize};
use rocket::State;
use std::sync::Mutex;

#[derive(Serialize, Deserialize, Clone)]
#[serde(crate = "rocket::serde")]
struct Pusher {
    id: u64,
    name: String,
}

type PusherList = Mutex<Vec<Pusher>>;

#[get("/pusher")]
fn get_all(list: &State<PusherList>) -> Json<Vec<Pusher>> {
    let items = list.lock().unwrap();
    Json(items.clone())
}

#[get("/pusher/<id>")]
fn get_by_id(id: u64, list: &State<PusherList>) -> Option<Json<Pusher>> {
    let items = list.lock().unwrap();
    items.iter()
        .find(|item| item.id == id)
        .map(|item| Json(item.clone()))
}

#[post("/pusher", data = "<item>")]
fn create(item: Json<Pusher>, list: &State<PusherList>) -> Json<Pusher> {
    let mut items = list.lock().unwrap();
    items.push(item.clone());
    item
}

#[put("/pusher/<id>", data = "<item>")]
fn update(id: u64, item: Json<Pusher>, list: &State<PusherList>) -> Option<Json<Pusher>> {
    let mut items = list.lock().unwrap();
    items.iter_mut()
        .find(|i| i.id == id)
        .map(|i| {
            *i = item.clone();
            Json(i.clone())
        })
}

#[delete("/pusher/<id>")]
fn delete(id: u64, list: &State<PusherList>) -> Option<()> {
    let mut items = list.lock().unwrap();
    let pos = items.iter().position(|i| i.id == id)?;
    items.remove(pos);
    Some(())
}

#[launch]
fn rocket() -> _ {
    rocket::build()
        .manage(PusherList::new(Vec::new()))
        .mount("/api", routes![get_all, get_by_id, create, update, delete])
}
