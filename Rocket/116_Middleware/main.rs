#[macro_use] extern crate rocket;

use rocket::serde::{json::Json, Deserialize, Serialize};
use rocket::State;
use std::sync::Mutex;

#[derive(Serialize, Deserialize, Clone)]
#[serde(crate = "rocket::serde")]
struct Middleware {
    id: u64,
    name: String,
}

type MiddlewareList = Mutex<Vec<Middleware>>;

#[get("/middleware")]
fn get_all(list: &State<MiddlewareList>) -> Json<Vec<Middleware>> {
    let items = list.lock().unwrap();
    Json(items.clone())
}

#[get("/middleware/<id>")]
fn get_by_id(id: u64, list: &State<MiddlewareList>) -> Option<Json<Middleware>> {
    let items = list.lock().unwrap();
    items.iter()
        .find(|item| item.id == id)
        .map(|item| Json(item.clone()))
}

#[post("/middleware", data = "<item>")]
fn create(item: Json<Middleware>, list: &State<MiddlewareList>) -> Json<Middleware> {
    let mut items = list.lock().unwrap();
    items.push(item.clone());
    item
}

#[put("/middleware/<id>", data = "<item>")]
fn update(id: u64, item: Json<Middleware>, list: &State<MiddlewareList>) -> Option<Json<Middleware>> {
    let mut items = list.lock().unwrap();
    items.iter_mut()
        .find(|i| i.id == id)
        .map(|i| {
            *i = item.clone();
            Json(i.clone())
        })
}

#[delete("/middleware/<id>")]
fn delete(id: u64, list: &State<MiddlewareList>) -> Option<()> {
    let mut items = list.lock().unwrap();
    let pos = items.iter().position(|i| i.id == id)?;
    items.remove(pos);
    Some(())
}

#[launch]
fn rocket() -> _ {
    rocket::build()
        .manage(MiddlewareList::new(Vec::new()))
        .mount("/api", routes![get_all, get_by_id, create, update, delete])
}
