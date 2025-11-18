#[macro_use] extern crate rocket;

use rocket::serde::{json::Json, Deserialize, Serialize};
use rocket::State;
use std::sync::Mutex;

#[derive(Serialize, Deserialize, Clone)]
#[serde(crate = "rocket::serde")]
struct Scheduler {
    id: u64,
    name: String,
}

type SchedulerList = Mutex<Vec<Scheduler>>;

#[get("/scheduler")]
fn get_all(list: &State<SchedulerList>) -> Json<Vec<Scheduler>> {
    let items = list.lock().unwrap();
    Json(items.clone())
}

#[get("/scheduler/<id>")]
fn get_by_id(id: u64, list: &State<SchedulerList>) -> Option<Json<Scheduler>> {
    let items = list.lock().unwrap();
    items.iter()
        .find(|item| item.id == id)
        .map(|item| Json(item.clone()))
}

#[post("/scheduler", data = "<item>")]
fn create(item: Json<Scheduler>, list: &State<SchedulerList>) -> Json<Scheduler> {
    let mut items = list.lock().unwrap();
    items.push(item.clone());
    item
}

#[put("/scheduler/<id>", data = "<item>")]
fn update(id: u64, item: Json<Scheduler>, list: &State<SchedulerList>) -> Option<Json<Scheduler>> {
    let mut items = list.lock().unwrap();
    items.iter_mut()
        .find(|i| i.id == id)
        .map(|i| {
            *i = item.clone();
            Json(i.clone())
        })
}

#[delete("/scheduler/<id>")]
fn delete(id: u64, list: &State<SchedulerList>) -> Option<()> {
    let mut items = list.lock().unwrap();
    let pos = items.iter().position(|i| i.id == id)?;
    items.remove(pos);
    Some(())
}

#[launch]
fn rocket() -> _ {
    rocket::build()
        .manage(SchedulerList::new(Vec::new()))
        .mount("/api", routes![get_all, get_by_id, create, update, delete])
}
