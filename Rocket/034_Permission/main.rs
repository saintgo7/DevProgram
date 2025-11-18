#[macro_use] extern crate rocket;

use rocket::serde::{json::Json, Deserialize, Serialize};
use rocket::State;
use std::sync::Mutex;

#[derive(Serialize, Deserialize, Clone)]
#[serde(crate = "rocket::serde")]
struct Permission {
    id: u64,
    name: String,
}

type PermissionList = Mutex<Vec<Permission>>;

#[get("/permission")]
fn get_all(list: &State<PermissionList>) -> Json<Vec<Permission>> {
    let items = list.lock().unwrap();
    Json(items.clone())
}

#[get("/permission/<id>")]
fn get_by_id(id: u64, list: &State<PermissionList>) -> Option<Json<Permission>> {
    let items = list.lock().unwrap();
    items.iter()
        .find(|item| item.id == id)
        .map(|item| Json(item.clone()))
}

#[post("/permission", data = "<item>")]
fn create(item: Json<Permission>, list: &State<PermissionList>) -> Json<Permission> {
    let mut items = list.lock().unwrap();
    items.push(item.clone());
    item
}

#[put("/permission/<id>", data = "<item>")]
fn update(id: u64, item: Json<Permission>, list: &State<PermissionList>) -> Option<Json<Permission>> {
    let mut items = list.lock().unwrap();
    items.iter_mut()
        .find(|i| i.id == id)
        .map(|i| {
            *i = item.clone();
            Json(i.clone())
        })
}

#[delete("/permission/<id>")]
fn delete(id: u64, list: &State<PermissionList>) -> Option<()> {
    let mut items = list.lock().unwrap();
    let pos = items.iter().position(|i| i.id == id)?;
    items.remove(pos);
    Some(())
}

#[launch]
fn rocket() -> _ {
    rocket::build()
        .manage(PermissionList::new(Vec::new()))
        .mount("/api", routes![get_all, get_by_id, create, update, delete])
}
