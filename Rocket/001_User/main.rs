#[macro_use] extern crate rocket;

use rocket::serde::{json::Json, Deserialize, Serialize};
use rocket::State;
use std::sync::Mutex;

#[derive(Serialize, Deserialize, Clone)]
#[serde(crate = "rocket::serde")]
struct User {
    id: u64,
    name: String,
}

type UserList = Mutex<Vec<User>>;

#[get("/user")]
fn get_all(list: &State<UserList>) -> Json<Vec<User>> {
    let items = list.lock().unwrap();
    Json(items.clone())
}

#[get("/user/<id>")]
fn get_by_id(id: u64, list: &State<UserList>) -> Option<Json<User>> {
    let items = list.lock().unwrap();
    items.iter()
        .find(|item| item.id == id)
        .map(|item| Json(item.clone()))
}

#[post("/user", data = "<item>")]
fn create(item: Json<User>, list: &State<UserList>) -> Json<User> {
    let mut items = list.lock().unwrap();
    items.push(item.clone());
    item
}

#[put("/user/<id>", data = "<item>")]
fn update(id: u64, item: Json<User>, list: &State<UserList>) -> Option<Json<User>> {
    let mut items = list.lock().unwrap();
    items.iter_mut()
        .find(|i| i.id == id)
        .map(|i| {
            *i = item.clone();
            Json(i.clone())
        })
}

#[delete("/user/<id>")]
fn delete(id: u64, list: &State<UserList>) -> Option<()> {
    let mut items = list.lock().unwrap();
    let pos = items.iter().position(|i| i.id == id)?;
    items.remove(pos);
    Some(())
}

#[launch]
fn rocket() -> _ {
    rocket::build()
        .manage(UserList::new(Vec::new()))
        .mount("/api", routes![get_all, get_by_id, create, update, delete])
}
