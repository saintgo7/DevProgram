#[macro_use] extern crate rocket;

use rocket::serde::{json::Json, Deserialize, Serialize};
use rocket::State;
use std::sync::Mutex;

#[derive(Serialize, Deserialize, Clone)]
#[serde(crate = "rocket::serde")]
struct Event {
    id: u64,
    name: String,
}

type EventList = Mutex<Vec<Event>>;

#[get("/event")]
fn get_all(list: &State<EventList>) -> Json<Vec<Event>> {
    let items = list.lock().unwrap();
    Json(items.clone())
}

#[get("/event/<id>")]
fn get_by_id(id: u64, list: &State<EventList>) -> Option<Json<Event>> {
    let items = list.lock().unwrap();
    items.iter()
        .find(|item| item.id == id)
        .map(|item| Json(item.clone()))
}

#[post("/event", data = "<item>")]
fn create(item: Json<Event>, list: &State<EventList>) -> Json<Event> {
    let mut items = list.lock().unwrap();
    items.push(item.clone());
    item
}

#[put("/event/<id>", data = "<item>")]
fn update(id: u64, item: Json<Event>, list: &State<EventList>) -> Option<Json<Event>> {
    let mut items = list.lock().unwrap();
    items.iter_mut()
        .find(|i| i.id == id)
        .map(|i| {
            *i = item.clone();
            Json(i.clone())
        })
}

#[delete("/event/<id>")]
fn delete(id: u64, list: &State<EventList>) -> Option<()> {
    let mut items = list.lock().unwrap();
    let pos = items.iter().position(|i| i.id == id)?;
    items.remove(pos);
    Some(())
}

#[launch]
fn rocket() -> _ {
    rocket::build()
        .manage(EventList::new(Vec::new()))
        .mount("/api", routes![get_all, get_by_id, create, update, delete])
}
