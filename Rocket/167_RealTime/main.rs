#[macro_use] extern crate rocket;

use rocket::serde::{json::Json, Deserialize, Serialize};
use rocket::State;
use std::sync::Mutex;

#[derive(Serialize, Deserialize, Clone)]
#[serde(crate = "rocket::serde")]
struct RealTime {
    id: u64,
    name: String,
}

type RealTimeList = Mutex<Vec<RealTime>>;

#[get("/realtime")]
fn get_all(list: &State<RealTimeList>) -> Json<Vec<RealTime>> {
    let items = list.lock().unwrap();
    Json(items.clone())
}

#[get("/realtime/<id>")]
fn get_by_id(id: u64, list: &State<RealTimeList>) -> Option<Json<RealTime>> {
    let items = list.lock().unwrap();
    items.iter()
        .find(|item| item.id == id)
        .map(|item| Json(item.clone()))
}

#[post("/realtime", data = "<item>")]
fn create(item: Json<RealTime>, list: &State<RealTimeList>) -> Json<RealTime> {
    let mut items = list.lock().unwrap();
    items.push(item.clone());
    item
}

#[put("/realtime/<id>", data = "<item>")]
fn update(id: u64, item: Json<RealTime>, list: &State<RealTimeList>) -> Option<Json<RealTime>> {
    let mut items = list.lock().unwrap();
    items.iter_mut()
        .find(|i| i.id == id)
        .map(|i| {
            *i = item.clone();
            Json(i.clone())
        })
}

#[delete("/realtime/<id>")]
fn delete(id: u64, list: &State<RealTimeList>) -> Option<()> {
    let mut items = list.lock().unwrap();
    let pos = items.iter().position(|i| i.id == id)?;
    items.remove(pos);
    Some(())
}

#[launch]
fn rocket() -> _ {
    rocket::build()
        .manage(RealTimeList::new(Vec::new()))
        .mount("/api", routes![get_all, get_by_id, create, update, delete])
}
