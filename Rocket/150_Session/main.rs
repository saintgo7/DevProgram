#[macro_use] extern crate rocket;

use rocket::serde::{json::Json, Deserialize, Serialize};
use rocket::State;
use std::sync::Mutex;

#[derive(Serialize, Deserialize, Clone)]
#[serde(crate = "rocket::serde")]
struct Session {
    id: u64,
    name: String,
}

type SessionList = Mutex<Vec<Session>>;

#[get("/session")]
fn get_all(list: &State<SessionList>) -> Json<Vec<Session>> {
    let items = list.lock().unwrap();
    Json(items.clone())
}

#[get("/session/<id>")]
fn get_by_id(id: u64, list: &State<SessionList>) -> Option<Json<Session>> {
    let items = list.lock().unwrap();
    items.iter()
        .find(|item| item.id == id)
        .map(|item| Json(item.clone()))
}

#[post("/session", data = "<item>")]
fn create(item: Json<Session>, list: &State<SessionList>) -> Json<Session> {
    let mut items = list.lock().unwrap();
    items.push(item.clone());
    item
}

#[put("/session/<id>", data = "<item>")]
fn update(id: u64, item: Json<Session>, list: &State<SessionList>) -> Option<Json<Session>> {
    let mut items = list.lock().unwrap();
    items.iter_mut()
        .find(|i| i.id == id)
        .map(|i| {
            *i = item.clone();
            Json(i.clone())
        })
}

#[delete("/session/<id>")]
fn delete(id: u64, list: &State<SessionList>) -> Option<()> {
    let mut items = list.lock().unwrap();
    let pos = items.iter().position(|i| i.id == id)?;
    items.remove(pos);
    Some(())
}

#[launch]
fn rocket() -> _ {
    rocket::build()
        .manage(SessionList::new(Vec::new()))
        .mount("/api", routes![get_all, get_by_id, create, update, delete])
}
