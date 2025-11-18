#[macro_use] extern crate rocket;

use rocket::serde::{json::Json, Deserialize, Serialize};
use rocket::State;
use std::sync::Mutex;

#[derive(Serialize, Deserialize, Clone)]
#[serde(crate = "rocket::serde")]
struct Hashing {
    id: u64,
    name: String,
}

type HashingList = Mutex<Vec<Hashing>>;

#[get("/hashing")]
fn get_all(list: &State<HashingList>) -> Json<Vec<Hashing>> {
    let items = list.lock().unwrap();
    Json(items.clone())
}

#[get("/hashing/<id>")]
fn get_by_id(id: u64, list: &State<HashingList>) -> Option<Json<Hashing>> {
    let items = list.lock().unwrap();
    items.iter()
        .find(|item| item.id == id)
        .map(|item| Json(item.clone()))
}

#[post("/hashing", data = "<item>")]
fn create(item: Json<Hashing>, list: &State<HashingList>) -> Json<Hashing> {
    let mut items = list.lock().unwrap();
    items.push(item.clone());
    item
}

#[put("/hashing/<id>", data = "<item>")]
fn update(id: u64, item: Json<Hashing>, list: &State<HashingList>) -> Option<Json<Hashing>> {
    let mut items = list.lock().unwrap();
    items.iter_mut()
        .find(|i| i.id == id)
        .map(|i| {
            *i = item.clone();
            Json(i.clone())
        })
}

#[delete("/hashing/<id>")]
fn delete(id: u64, list: &State<HashingList>) -> Option<()> {
    let mut items = list.lock().unwrap();
    let pos = items.iter().position(|i| i.id == id)?;
    items.remove(pos);
    Some(())
}

#[launch]
fn rocket() -> _ {
    rocket::build()
        .manage(HashingList::new(Vec::new()))
        .mount("/api", routes![get_all, get_by_id, create, update, delete])
}
