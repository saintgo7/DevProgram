#[macro_use] extern crate rocket;

use rocket::serde::{json::Json, Deserialize, Serialize};
use rocket::State;
use std::sync::Mutex;

#[derive(Serialize, Deserialize, Clone)]
#[serde(crate = "rocket::serde")]
struct Restore {
    id: u64,
    name: String,
}

type RestoreList = Mutex<Vec<Restore>>;

#[get("/restore")]
fn get_all(list: &State<RestoreList>) -> Json<Vec<Restore>> {
    let items = list.lock().unwrap();
    Json(items.clone())
}

#[get("/restore/<id>")]
fn get_by_id(id: u64, list: &State<RestoreList>) -> Option<Json<Restore>> {
    let items = list.lock().unwrap();
    items.iter()
        .find(|item| item.id == id)
        .map(|item| Json(item.clone()))
}

#[post("/restore", data = "<item>")]
fn create(item: Json<Restore>, list: &State<RestoreList>) -> Json<Restore> {
    let mut items = list.lock().unwrap();
    items.push(item.clone());
    item
}

#[put("/restore/<id>", data = "<item>")]
fn update(id: u64, item: Json<Restore>, list: &State<RestoreList>) -> Option<Json<Restore>> {
    let mut items = list.lock().unwrap();
    items.iter_mut()
        .find(|i| i.id == id)
        .map(|i| {
            *i = item.clone();
            Json(i.clone())
        })
}

#[delete("/restore/<id>")]
fn delete(id: u64, list: &State<RestoreList>) -> Option<()> {
    let mut items = list.lock().unwrap();
    let pos = items.iter().position(|i| i.id == id)?;
    items.remove(pos);
    Some(())
}

#[launch]
fn rocket() -> _ {
    rocket::build()
        .manage(RestoreList::new(Vec::new()))
        .mount("/api", routes![get_all, get_by_id, create, update, delete])
}
