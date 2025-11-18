#[macro_use] extern crate rocket;

use rocket::serde::{json::Json, Deserialize, Serialize};
use rocket::State;
use std::sync::Mutex;

#[derive(Serialize, Deserialize, Clone)]
#[serde(crate = "rocket::serde")]
struct Pagination {
    id: u64,
    name: String,
}

type PaginationList = Mutex<Vec<Pagination>>;

#[get("/pagination")]
fn get_all(list: &State<PaginationList>) -> Json<Vec<Pagination>> {
    let items = list.lock().unwrap();
    Json(items.clone())
}

#[get("/pagination/<id>")]
fn get_by_id(id: u64, list: &State<PaginationList>) -> Option<Json<Pagination>> {
    let items = list.lock().unwrap();
    items.iter()
        .find(|item| item.id == id)
        .map(|item| Json(item.clone()))
}

#[post("/pagination", data = "<item>")]
fn create(item: Json<Pagination>, list: &State<PaginationList>) -> Json<Pagination> {
    let mut items = list.lock().unwrap();
    items.push(item.clone());
    item
}

#[put("/pagination/<id>", data = "<item>")]
fn update(id: u64, item: Json<Pagination>, list: &State<PaginationList>) -> Option<Json<Pagination>> {
    let mut items = list.lock().unwrap();
    items.iter_mut()
        .find(|i| i.id == id)
        .map(|i| {
            *i = item.clone();
            Json(i.clone())
        })
}

#[delete("/pagination/<id>")]
fn delete(id: u64, list: &State<PaginationList>) -> Option<()> {
    let mut items = list.lock().unwrap();
    let pos = items.iter().position(|i| i.id == id)?;
    items.remove(pos);
    Some(())
}

#[launch]
fn rocket() -> _ {
    rocket::build()
        .manage(PaginationList::new(Vec::new()))
        .mount("/api", routes![get_all, get_by_id, create, update, delete])
}
