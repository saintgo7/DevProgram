#[macro_use] extern crate rocket;

use rocket::serde::{json::Json, Deserialize, Serialize};
use rocket::State;
use std::sync::Mutex;

#[derive(Serialize, Deserialize, Clone)]
#[serde(crate = "rocket::serde")]
struct Photo {
    id: u64,
    name: String,
}

type PhotoList = Mutex<Vec<Photo>>;

#[get("/photo")]
fn get_all(list: &State<PhotoList>) -> Json<Vec<Photo>> {
    let items = list.lock().unwrap();
    Json(items.clone())
}

#[get("/photo/<id>")]
fn get_by_id(id: u64, list: &State<PhotoList>) -> Option<Json<Photo>> {
    let items = list.lock().unwrap();
    items.iter()
        .find(|item| item.id == id)
        .map(|item| Json(item.clone()))
}

#[post("/photo", data = "<item>")]
fn create(item: Json<Photo>, list: &State<PhotoList>) -> Json<Photo> {
    let mut items = list.lock().unwrap();
    items.push(item.clone());
    item
}

#[put("/photo/<id>", data = "<item>")]
fn update(id: u64, item: Json<Photo>, list: &State<PhotoList>) -> Option<Json<Photo>> {
    let mut items = list.lock().unwrap();
    items.iter_mut()
        .find(|i| i.id == id)
        .map(|i| {
            *i = item.clone();
            Json(i.clone())
        })
}

#[delete("/photo/<id>")]
fn delete(id: u64, list: &State<PhotoList>) -> Option<()> {
    let mut items = list.lock().unwrap();
    let pos = items.iter().position(|i| i.id == id)?;
    items.remove(pos);
    Some(())
}

#[launch]
fn rocket() -> _ {
    rocket::build()
        .manage(PhotoList::new(Vec::new()))
        .mount("/api", routes![get_all, get_by_id, create, update, delete])
}
