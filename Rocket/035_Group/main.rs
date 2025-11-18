#[macro_use] extern crate rocket;

use rocket::serde::{json::Json, Deserialize, Serialize};
use rocket::State;
use std::sync::Mutex;

#[derive(Serialize, Deserialize, Clone)]
#[serde(crate = "rocket::serde")]
struct Group {
    id: u64,
    name: String,
}

type GroupList = Mutex<Vec<Group>>;

#[get("/group")]
fn get_all(list: &State<GroupList>) -> Json<Vec<Group>> {
    let items = list.lock().unwrap();
    Json(items.clone())
}

#[get("/group/<id>")]
fn get_by_id(id: u64, list: &State<GroupList>) -> Option<Json<Group>> {
    let items = list.lock().unwrap();
    items.iter()
        .find(|item| item.id == id)
        .map(|item| Json(item.clone()))
}

#[post("/group", data = "<item>")]
fn create(item: Json<Group>, list: &State<GroupList>) -> Json<Group> {
    let mut items = list.lock().unwrap();
    items.push(item.clone());
    item
}

#[put("/group/<id>", data = "<item>")]
fn update(id: u64, item: Json<Group>, list: &State<GroupList>) -> Option<Json<Group>> {
    let mut items = list.lock().unwrap();
    items.iter_mut()
        .find(|i| i.id == id)
        .map(|i| {
            *i = item.clone();
            Json(i.clone())
        })
}

#[delete("/group/<id>")]
fn delete(id: u64, list: &State<GroupList>) -> Option<()> {
    let mut items = list.lock().unwrap();
    let pos = items.iter().position(|i| i.id == id)?;
    items.remove(pos);
    Some(())
}

#[launch]
fn rocket() -> _ {
    rocket::build()
        .manage(GroupList::new(Vec::new()))
        .mount("/api", routes![get_all, get_by_id, create, update, delete])
}
