#[macro_use] extern crate rocket;

use rocket::serde::{json::Json, Deserialize, Serialize};
use rocket::State;
use std::sync::Mutex;

#[derive(Serialize, Deserialize, Clone)]
#[serde(crate = "rocket::serde")]
struct Worker {
    id: u64,
    name: String,
}

type WorkerList = Mutex<Vec<Worker>>;

#[get("/worker")]
fn get_all(list: &State<WorkerList>) -> Json<Vec<Worker>> {
    let items = list.lock().unwrap();
    Json(items.clone())
}

#[get("/worker/<id>")]
fn get_by_id(id: u64, list: &State<WorkerList>) -> Option<Json<Worker>> {
    let items = list.lock().unwrap();
    items.iter()
        .find(|item| item.id == id)
        .map(|item| Json(item.clone()))
}

#[post("/worker", data = "<item>")]
fn create(item: Json<Worker>, list: &State<WorkerList>) -> Json<Worker> {
    let mut items = list.lock().unwrap();
    items.push(item.clone());
    item
}

#[put("/worker/<id>", data = "<item>")]
fn update(id: u64, item: Json<Worker>, list: &State<WorkerList>) -> Option<Json<Worker>> {
    let mut items = list.lock().unwrap();
    items.iter_mut()
        .find(|i| i.id == id)
        .map(|i| {
            *i = item.clone();
            Json(i.clone())
        })
}

#[delete("/worker/<id>")]
fn delete(id: u64, list: &State<WorkerList>) -> Option<()> {
    let mut items = list.lock().unwrap();
    let pos = items.iter().position(|i| i.id == id)?;
    items.remove(pos);
    Some(())
}

#[launch]
fn rocket() -> _ {
    rocket::build()
        .manage(WorkerList::new(Vec::new()))
        .mount("/api", routes![get_all, get_by_id, create, update, delete])
}
