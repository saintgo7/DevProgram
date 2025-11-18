#[macro_use] extern crate rocket;

use rocket::serde::{json::Json, Deserialize, Serialize};
use rocket::State;
use std::sync::Mutex;

#[derive(Serialize, Deserialize, Clone)]
#[serde(crate = "rocket::serde")]
struct Query {
    id: u64,
    name: String,
}

type QueryList = Mutex<Vec<Query>>;

#[get("/query")]
fn get_all(list: &State<QueryList>) -> Json<Vec<Query>> {
    let items = list.lock().unwrap();
    Json(items.clone())
}

#[get("/query/<id>")]
fn get_by_id(id: u64, list: &State<QueryList>) -> Option<Json<Query>> {
    let items = list.lock().unwrap();
    items.iter()
        .find(|item| item.id == id)
        .map(|item| Json(item.clone()))
}

#[post("/query", data = "<item>")]
fn create(item: Json<Query>, list: &State<QueryList>) -> Json<Query> {
    let mut items = list.lock().unwrap();
    items.push(item.clone());
    item
}

#[put("/query/<id>", data = "<item>")]
fn update(id: u64, item: Json<Query>, list: &State<QueryList>) -> Option<Json<Query>> {
    let mut items = list.lock().unwrap();
    items.iter_mut()
        .find(|i| i.id == id)
        .map(|i| {
            *i = item.clone();
            Json(i.clone())
        })
}

#[delete("/query/<id>")]
fn delete(id: u64, list: &State<QueryList>) -> Option<()> {
    let mut items = list.lock().unwrap();
    let pos = items.iter().position(|i| i.id == id)?;
    items.remove(pos);
    Some(())
}

#[launch]
fn rocket() -> _ {
    rocket::build()
        .manage(QueryList::new(Vec::new()))
        .mount("/api", routes![get_all, get_by_id, create, update, delete])
}
