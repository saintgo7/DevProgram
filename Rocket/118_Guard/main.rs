#[macro_use] extern crate rocket;

use rocket::serde::{json::Json, Deserialize, Serialize};
use rocket::State;
use std::sync::Mutex;

#[derive(Serialize, Deserialize, Clone)]
#[serde(crate = "rocket::serde")]
struct Guard {
    id: u64,
    name: String,
}

type GuardList = Mutex<Vec<Guard>>;

#[get("/guard")]
fn get_all(list: &State<GuardList>) -> Json<Vec<Guard>> {
    let items = list.lock().unwrap();
    Json(items.clone())
}

#[get("/guard/<id>")]
fn get_by_id(id: u64, list: &State<GuardList>) -> Option<Json<Guard>> {
    let items = list.lock().unwrap();
    items.iter()
        .find(|item| item.id == id)
        .map(|item| Json(item.clone()))
}

#[post("/guard", data = "<item>")]
fn create(item: Json<Guard>, list: &State<GuardList>) -> Json<Guard> {
    let mut items = list.lock().unwrap();
    items.push(item.clone());
    item
}

#[put("/guard/<id>", data = "<item>")]
fn update(id: u64, item: Json<Guard>, list: &State<GuardList>) -> Option<Json<Guard>> {
    let mut items = list.lock().unwrap();
    items.iter_mut()
        .find(|i| i.id == id)
        .map(|i| {
            *i = item.clone();
            Json(i.clone())
        })
}

#[delete("/guard/<id>")]
fn delete(id: u64, list: &State<GuardList>) -> Option<()> {
    let mut items = list.lock().unwrap();
    let pos = items.iter().position(|i| i.id == id)?;
    items.remove(pos);
    Some(())
}

#[launch]
fn rocket() -> _ {
    rocket::build()
        .manage(GuardList::new(Vec::new()))
        .mount("/api", routes![get_all, get_by_id, create, update, delete])
}
