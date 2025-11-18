#[macro_use] extern crate rocket;

use rocket::serde::{json::Json, Deserialize, Serialize};
use rocket::State;
use std::sync::Mutex;

#[derive(Serialize, Deserialize, Clone)]
#[serde(crate = "rocket::serde")]
struct Validation {
    id: u64,
    name: String,
}

type ValidationList = Mutex<Vec<Validation>>;

#[get("/validation")]
fn get_all(list: &State<ValidationList>) -> Json<Vec<Validation>> {
    let items = list.lock().unwrap();
    Json(items.clone())
}

#[get("/validation/<id>")]
fn get_by_id(id: u64, list: &State<ValidationList>) -> Option<Json<Validation>> {
    let items = list.lock().unwrap();
    items.iter()
        .find(|item| item.id == id)
        .map(|item| Json(item.clone()))
}

#[post("/validation", data = "<item>")]
fn create(item: Json<Validation>, list: &State<ValidationList>) -> Json<Validation> {
    let mut items = list.lock().unwrap();
    items.push(item.clone());
    item
}

#[put("/validation/<id>", data = "<item>")]
fn update(id: u64, item: Json<Validation>, list: &State<ValidationList>) -> Option<Json<Validation>> {
    let mut items = list.lock().unwrap();
    items.iter_mut()
        .find(|i| i.id == id)
        .map(|i| {
            *i = item.clone();
            Json(i.clone())
        })
}

#[delete("/validation/<id>")]
fn delete(id: u64, list: &State<ValidationList>) -> Option<()> {
    let mut items = list.lock().unwrap();
    let pos = items.iter().position(|i| i.id == id)?;
    items.remove(pos);
    Some(())
}

#[launch]
fn rocket() -> _ {
    rocket::build()
        .manage(ValidationList::new(Vec::new()))
        .mount("/api", routes![get_all, get_by_id, create, update, delete])
}
