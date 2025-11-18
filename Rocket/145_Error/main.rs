#[macro_use] extern crate rocket;

use rocket::serde::{json::Json, Deserialize, Serialize};
use rocket::State;
use std::sync::Mutex;

#[derive(Serialize, Deserialize, Clone)]
#[serde(crate = "rocket::serde")]
struct Error {
    id: u64,
    name: String,
}

type ErrorList = Mutex<Vec<Error>>;

#[get("/error")]
fn get_all(list: &State<ErrorList>) -> Json<Vec<Error>> {
    let items = list.lock().unwrap();
    Json(items.clone())
}

#[get("/error/<id>")]
fn get_by_id(id: u64, list: &State<ErrorList>) -> Option<Json<Error>> {
    let items = list.lock().unwrap();
    items.iter()
        .find(|item| item.id == id)
        .map(|item| Json(item.clone()))
}

#[post("/error", data = "<item>")]
fn create(item: Json<Error>, list: &State<ErrorList>) -> Json<Error> {
    let mut items = list.lock().unwrap();
    items.push(item.clone());
    item
}

#[put("/error/<id>", data = "<item>")]
fn update(id: u64, item: Json<Error>, list: &State<ErrorList>) -> Option<Json<Error>> {
    let mut items = list.lock().unwrap();
    items.iter_mut()
        .find(|i| i.id == id)
        .map(|i| {
            *i = item.clone();
            Json(i.clone())
        })
}

#[delete("/error/<id>")]
fn delete(id: u64, list: &State<ErrorList>) -> Option<()> {
    let mut items = list.lock().unwrap();
    let pos = items.iter().position(|i| i.id == id)?;
    items.remove(pos);
    Some(())
}

#[launch]
fn rocket() -> _ {
    rocket::build()
        .manage(ErrorList::new(Vec::new()))
        .mount("/api", routes![get_all, get_by_id, create, update, delete])
}
