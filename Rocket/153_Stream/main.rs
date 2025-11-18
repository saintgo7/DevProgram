#[macro_use] extern crate rocket;

use rocket::serde::{json::Json, Deserialize, Serialize};
use rocket::State;
use std::sync::Mutex;

#[derive(Serialize, Deserialize, Clone)]
#[serde(crate = "rocket::serde")]
struct Stream {
    id: u64,
    name: String,
}

type StreamList = Mutex<Vec<Stream>>;

#[get("/stream")]
fn get_all(list: &State<StreamList>) -> Json<Vec<Stream>> {
    let items = list.lock().unwrap();
    Json(items.clone())
}

#[get("/stream/<id>")]
fn get_by_id(id: u64, list: &State<StreamList>) -> Option<Json<Stream>> {
    let items = list.lock().unwrap();
    items.iter()
        .find(|item| item.id == id)
        .map(|item| Json(item.clone()))
}

#[post("/stream", data = "<item>")]
fn create(item: Json<Stream>, list: &State<StreamList>) -> Json<Stream> {
    let mut items = list.lock().unwrap();
    items.push(item.clone());
    item
}

#[put("/stream/<id>", data = "<item>")]
fn update(id: u64, item: Json<Stream>, list: &State<StreamList>) -> Option<Json<Stream>> {
    let mut items = list.lock().unwrap();
    items.iter_mut()
        .find(|i| i.id == id)
        .map(|i| {
            *i = item.clone();
            Json(i.clone())
        })
}

#[delete("/stream/<id>")]
fn delete(id: u64, list: &State<StreamList>) -> Option<()> {
    let mut items = list.lock().unwrap();
    let pos = items.iter().position(|i| i.id == id)?;
    items.remove(pos);
    Some(())
}

#[launch]
fn rocket() -> _ {
    rocket::build()
        .manage(StreamList::new(Vec::new()))
        .mount("/api", routes![get_all, get_by_id, create, update, delete])
}
