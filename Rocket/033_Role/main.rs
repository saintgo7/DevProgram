#[macro_use] extern crate rocket;

use rocket::serde::{json::Json, Deserialize, Serialize};
use rocket::State;
use std::sync::Mutex;

#[derive(Serialize, Deserialize, Clone)]
#[serde(crate = "rocket::serde")]
struct Role {
    id: u64,
    name: String,
}

type RoleList = Mutex<Vec<Role>>;

#[get("/role")]
fn get_all(list: &State<RoleList>) -> Json<Vec<Role>> {
    let items = list.lock().unwrap();
    Json(items.clone())
}

#[get("/role/<id>")]
fn get_by_id(id: u64, list: &State<RoleList>) -> Option<Json<Role>> {
    let items = list.lock().unwrap();
    items.iter()
        .find(|item| item.id == id)
        .map(|item| Json(item.clone()))
}

#[post("/role", data = "<item>")]
fn create(item: Json<Role>, list: &State<RoleList>) -> Json<Role> {
    let mut items = list.lock().unwrap();
    items.push(item.clone());
    item
}

#[put("/role/<id>", data = "<item>")]
fn update(id: u64, item: Json<Role>, list: &State<RoleList>) -> Option<Json<Role>> {
    let mut items = list.lock().unwrap();
    items.iter_mut()
        .find(|i| i.id == id)
        .map(|i| {
            *i = item.clone();
            Json(i.clone())
        })
}

#[delete("/role/<id>")]
fn delete(id: u64, list: &State<RoleList>) -> Option<()> {
    let mut items = list.lock().unwrap();
    let pos = items.iter().position(|i| i.id == id)?;
    items.remove(pos);
    Some(())
}

#[launch]
fn rocket() -> _ {
    rocket::build()
        .manage(RoleList::new(Vec::new()))
        .mount("/api", routes![get_all, get_by_id, create, update, delete])
}
