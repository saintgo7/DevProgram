#[macro_use] extern crate rocket;

use rocket::serde::{json::Json, Deserialize, Serialize};
use rocket::State;
use std::sync::Mutex;

#[derive(Serialize, Deserialize, Clone)]
#[serde(crate = "rocket::serde")]
struct Validator {
    id: u64,
    name: String,
}

type ValidatorList = Mutex<Vec<Validator>>;

#[get("/validator")]
fn get_all(list: &State<ValidatorList>) -> Json<Vec<Validator>> {
    let items = list.lock().unwrap();
    Json(items.clone())
}

#[get("/validator/<id>")]
fn get_by_id(id: u64, list: &State<ValidatorList>) -> Option<Json<Validator>> {
    let items = list.lock().unwrap();
    items.iter()
        .find(|item| item.id == id)
        .map(|item| Json(item.clone()))
}

#[post("/validator", data = "<item>")]
fn create(item: Json<Validator>, list: &State<ValidatorList>) -> Json<Validator> {
    let mut items = list.lock().unwrap();
    items.push(item.clone());
    item
}

#[put("/validator/<id>", data = "<item>")]
fn update(id: u64, item: Json<Validator>, list: &State<ValidatorList>) -> Option<Json<Validator>> {
    let mut items = list.lock().unwrap();
    items.iter_mut()
        .find(|i| i.id == id)
        .map(|i| {
            *i = item.clone();
            Json(i.clone())
        })
}

#[delete("/validator/<id>")]
fn delete(id: u64, list: &State<ValidatorList>) -> Option<()> {
    let mut items = list.lock().unwrap();
    let pos = items.iter().position(|i| i.id == id)?;
    items.remove(pos);
    Some(())
}

#[launch]
fn rocket() -> _ {
    rocket::build()
        .manage(ValidatorList::new(Vec::new()))
        .mount("/api", routes![get_all, get_by_id, create, update, delete])
}
