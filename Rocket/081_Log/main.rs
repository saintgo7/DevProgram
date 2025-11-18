#[macro_use] extern crate rocket;

use rocket::serde::{json::Json, Deserialize, Serialize};
use rocket::State;
use std::sync::Mutex;

#[derive(Serialize, Deserialize, Clone)]
#[serde(crate = "rocket::serde")]
struct Log {
    id: u64,
    name: String,
}

type LogList = Mutex<Vec<Log>>;

#[get("/log")]
fn get_all(list: &State<LogList>) -> Json<Vec<Log>> {
    let items = list.lock().unwrap();
    Json(items.clone())
}

#[get("/log/<id>")]
fn get_by_id(id: u64, list: &State<LogList>) -> Option<Json<Log>> {
    let items = list.lock().unwrap();
    items.iter()
        .find(|item| item.id == id)
        .map(|item| Json(item.clone()))
}

#[post("/log", data = "<item>")]
fn create(item: Json<Log>, list: &State<LogList>) -> Json<Log> {
    let mut items = list.lock().unwrap();
    items.push(item.clone());
    item
}

#[put("/log/<id>", data = "<item>")]
fn update(id: u64, item: Json<Log>, list: &State<LogList>) -> Option<Json<Log>> {
    let mut items = list.lock().unwrap();
    items.iter_mut()
        .find(|i| i.id == id)
        .map(|i| {
            *i = item.clone();
            Json(i.clone())
        })
}

#[delete("/log/<id>")]
fn delete(id: u64, list: &State<LogList>) -> Option<()> {
    let mut items = list.lock().unwrap();
    let pos = items.iter().position(|i| i.id == id)?;
    items.remove(pos);
    Some(())
}

#[launch]
fn rocket() -> _ {
    rocket::build()
        .manage(LogList::new(Vec::new()))
        .mount("/api", routes![get_all, get_by_id, create, update, delete])
}
