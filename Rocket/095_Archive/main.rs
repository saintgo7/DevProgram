#[macro_use] extern crate rocket;

use rocket::serde::{json::Json, Deserialize, Serialize};
use rocket::State;
use std::sync::Mutex;

#[derive(Serialize, Deserialize, Clone)]
#[serde(crate = "rocket::serde")]
struct Archive {
    id: u64,
    name: String,
}

type ArchiveList = Mutex<Vec<Archive>>;

#[get("/archive")]
fn get_all(list: &State<ArchiveList>) -> Json<Vec<Archive>> {
    let items = list.lock().unwrap();
    Json(items.clone())
}

#[get("/archive/<id>")]
fn get_by_id(id: u64, list: &State<ArchiveList>) -> Option<Json<Archive>> {
    let items = list.lock().unwrap();
    items.iter()
        .find(|item| item.id == id)
        .map(|item| Json(item.clone()))
}

#[post("/archive", data = "<item>")]
fn create(item: Json<Archive>, list: &State<ArchiveList>) -> Json<Archive> {
    let mut items = list.lock().unwrap();
    items.push(item.clone());
    item
}

#[put("/archive/<id>", data = "<item>")]
fn update(id: u64, item: Json<Archive>, list: &State<ArchiveList>) -> Option<Json<Archive>> {
    let mut items = list.lock().unwrap();
    items.iter_mut()
        .find(|i| i.id == id)
        .map(|i| {
            *i = item.clone();
            Json(i.clone())
        })
}

#[delete("/archive/<id>")]
fn delete(id: u64, list: &State<ArchiveList>) -> Option<()> {
    let mut items = list.lock().unwrap();
    let pos = items.iter().position(|i| i.id == id)?;
    items.remove(pos);
    Some(())
}

#[launch]
fn rocket() -> _ {
    rocket::build()
        .manage(ArchiveList::new(Vec::new()))
        .mount("/api", routes![get_all, get_by_id, create, update, delete])
}
