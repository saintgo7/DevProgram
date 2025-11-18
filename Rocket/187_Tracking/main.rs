#[macro_use] extern crate rocket;

use rocket::serde::{json::Json, Deserialize, Serialize};
use rocket::State;
use std::sync::Mutex;

#[derive(Serialize, Deserialize, Clone)]
#[serde(crate = "rocket::serde")]
struct Tracking {
    id: u64,
    name: String,
}

type TrackingList = Mutex<Vec<Tracking>>;

#[get("/tracking")]
fn get_all(list: &State<TrackingList>) -> Json<Vec<Tracking>> {
    let items = list.lock().unwrap();
    Json(items.clone())
}

#[get("/tracking/<id>")]
fn get_by_id(id: u64, list: &State<TrackingList>) -> Option<Json<Tracking>> {
    let items = list.lock().unwrap();
    items.iter()
        .find(|item| item.id == id)
        .map(|item| Json(item.clone()))
}

#[post("/tracking", data = "<item>")]
fn create(item: Json<Tracking>, list: &State<TrackingList>) -> Json<Tracking> {
    let mut items = list.lock().unwrap();
    items.push(item.clone());
    item
}

#[put("/tracking/<id>", data = "<item>")]
fn update(id: u64, item: Json<Tracking>, list: &State<TrackingList>) -> Option<Json<Tracking>> {
    let mut items = list.lock().unwrap();
    items.iter_mut()
        .find(|i| i.id == id)
        .map(|i| {
            *i = item.clone();
            Json(i.clone())
        })
}

#[delete("/tracking/<id>")]
fn delete(id: u64, list: &State<TrackingList>) -> Option<()> {
    let mut items = list.lock().unwrap();
    let pos = items.iter().position(|i| i.id == id)?;
    items.remove(pos);
    Some(())
}

#[launch]
fn rocket() -> _ {
    rocket::build()
        .manage(TrackingList::new(Vec::new()))
        .mount("/api", routes![get_all, get_by_id, create, update, delete])
}
