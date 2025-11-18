#[macro_use] extern crate rocket;

use rocket::serde::{json::Json, Deserialize, Serialize};
use rocket::State;
use std::sync::Mutex;

#[derive(Serialize, Deserialize, Clone)]
#[serde(crate = "rocket::serde")]
struct Queue {
    id: u64,
    name: String,
}

type QueueList = Mutex<Vec<Queue>>;

#[get("/queue")]
fn get_all(list: &State<QueueList>) -> Json<Vec<Queue>> {
    let items = list.lock().unwrap();
    Json(items.clone())
}

#[get("/queue/<id>")]
fn get_by_id(id: u64, list: &State<QueueList>) -> Option<Json<Queue>> {
    let items = list.lock().unwrap();
    items.iter()
        .find(|item| item.id == id)
        .map(|item| Json(item.clone()))
}

#[post("/queue", data = "<item>")]
fn create(item: Json<Queue>, list: &State<QueueList>) -> Json<Queue> {
    let mut items = list.lock().unwrap();
    items.push(item.clone());
    item
}

#[put("/queue/<id>", data = "<item>")]
fn update(id: u64, item: Json<Queue>, list: &State<QueueList>) -> Option<Json<Queue>> {
    let mut items = list.lock().unwrap();
    items.iter_mut()
        .find(|i| i.id == id)
        .map(|i| {
            *i = item.clone();
            Json(i.clone())
        })
}

#[delete("/queue/<id>")]
fn delete(id: u64, list: &State<QueueList>) -> Option<()> {
    let mut items = list.lock().unwrap();
    let pos = items.iter().position(|i| i.id == id)?;
    items.remove(pos);
    Some(())
}

#[launch]
fn rocket() -> _ {
    rocket::build()
        .manage(QueueList::new(Vec::new()))
        .mount("/api", routes![get_all, get_by_id, create, update, delete])
}
