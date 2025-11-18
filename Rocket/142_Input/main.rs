#[macro_use] extern crate rocket;

use rocket::serde::{json::Json, Deserialize, Serialize};
use rocket::State;
use std::sync::Mutex;

#[derive(Serialize, Deserialize, Clone)]
#[serde(crate = "rocket::serde")]
struct Input {
    id: u64,
    name: String,
}

type InputList = Mutex<Vec<Input>>;

#[get("/input")]
fn get_all(list: &State<InputList>) -> Json<Vec<Input>> {
    let items = list.lock().unwrap();
    Json(items.clone())
}

#[get("/input/<id>")]
fn get_by_id(id: u64, list: &State<InputList>) -> Option<Json<Input>> {
    let items = list.lock().unwrap();
    items.iter()
        .find(|item| item.id == id)
        .map(|item| Json(item.clone()))
}

#[post("/input", data = "<item>")]
fn create(item: Json<Input>, list: &State<InputList>) -> Json<Input> {
    let mut items = list.lock().unwrap();
    items.push(item.clone());
    item
}

#[put("/input/<id>", data = "<item>")]
fn update(id: u64, item: Json<Input>, list: &State<InputList>) -> Option<Json<Input>> {
    let mut items = list.lock().unwrap();
    items.iter_mut()
        .find(|i| i.id == id)
        .map(|i| {
            *i = item.clone();
            Json(i.clone())
        })
}

#[delete("/input/<id>")]
fn delete(id: u64, list: &State<InputList>) -> Option<()> {
    let mut items = list.lock().unwrap();
    let pos = items.iter().position(|i| i.id == id)?;
    items.remove(pos);
    Some(())
}

#[launch]
fn rocket() -> _ {
    rocket::build()
        .manage(InputList::new(Vec::new()))
        .mount("/api", routes![get_all, get_by_id, create, update, delete])
}
