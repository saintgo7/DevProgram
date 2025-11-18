#[macro_use] extern crate rocket;

use rocket::serde::{json::Json, Deserialize, Serialize};
use rocket::State;
use std::sync::Mutex;

#[derive(Serialize, Deserialize, Clone)]
#[serde(crate = "rocket::serde")]
struct Authentication {
    id: u64,
    name: String,
}

type AuthenticationList = Mutex<Vec<Authentication>>;

#[get("/authentication")]
fn get_all(list: &State<AuthenticationList>) -> Json<Vec<Authentication>> {
    let items = list.lock().unwrap();
    Json(items.clone())
}

#[get("/authentication/<id>")]
fn get_by_id(id: u64, list: &State<AuthenticationList>) -> Option<Json<Authentication>> {
    let items = list.lock().unwrap();
    items.iter()
        .find(|item| item.id == id)
        .map(|item| Json(item.clone()))
}

#[post("/authentication", data = "<item>")]
fn create(item: Json<Authentication>, list: &State<AuthenticationList>) -> Json<Authentication> {
    let mut items = list.lock().unwrap();
    items.push(item.clone());
    item
}

#[put("/authentication/<id>", data = "<item>")]
fn update(id: u64, item: Json<Authentication>, list: &State<AuthenticationList>) -> Option<Json<Authentication>> {
    let mut items = list.lock().unwrap();
    items.iter_mut()
        .find(|i| i.id == id)
        .map(|i| {
            *i = item.clone();
            Json(i.clone())
        })
}

#[delete("/authentication/<id>")]
fn delete(id: u64, list: &State<AuthenticationList>) -> Option<()> {
    let mut items = list.lock().unwrap();
    let pos = items.iter().position(|i| i.id == id)?;
    items.remove(pos);
    Some(())
}

#[launch]
fn rocket() -> _ {
    rocket::build()
        .manage(AuthenticationList::new(Vec::new()))
        .mount("/api", routes![get_all, get_by_id, create, update, delete])
}
