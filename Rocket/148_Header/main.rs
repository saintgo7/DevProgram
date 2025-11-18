#[macro_use] extern crate rocket;

use rocket::serde::{json::Json, Deserialize, Serialize};
use rocket::State;
use std::sync::Mutex;

#[derive(Serialize, Deserialize, Clone)]
#[serde(crate = "rocket::serde")]
struct Header {
    id: u64,
    name: String,
}

type HeaderList = Mutex<Vec<Header>>;

#[get("/header")]
fn get_all(list: &State<HeaderList>) -> Json<Vec<Header>> {
    let items = list.lock().unwrap();
    Json(items.clone())
}

#[get("/header/<id>")]
fn get_by_id(id: u64, list: &State<HeaderList>) -> Option<Json<Header>> {
    let items = list.lock().unwrap();
    items.iter()
        .find(|item| item.id == id)
        .map(|item| Json(item.clone()))
}

#[post("/header", data = "<item>")]
fn create(item: Json<Header>, list: &State<HeaderList>) -> Json<Header> {
    let mut items = list.lock().unwrap();
    items.push(item.clone());
    item
}

#[put("/header/<id>", data = "<item>")]
fn update(id: u64, item: Json<Header>, list: &State<HeaderList>) -> Option<Json<Header>> {
    let mut items = list.lock().unwrap();
    items.iter_mut()
        .find(|i| i.id == id)
        .map(|i| {
            *i = item.clone();
            Json(i.clone())
        })
}

#[delete("/header/<id>")]
fn delete(id: u64, list: &State<HeaderList>) -> Option<()> {
    let mut items = list.lock().unwrap();
    let pos = items.iter().position(|i| i.id == id)?;
    items.remove(pos);
    Some(())
}

#[launch]
fn rocket() -> _ {
    rocket::build()
        .manage(HeaderList::new(Vec::new()))
        .mount("/api", routes![get_all, get_by_id, create, update, delete])
}
