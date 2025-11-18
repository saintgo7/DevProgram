#[macro_use] extern crate rocket;

use rocket::serde::{json::Json, Deserialize, Serialize};
use rocket::State;
use std::sync::Mutex;

#[derive(Serialize, Deserialize, Clone)]
#[serde(crate = "rocket::serde")]
struct Sort {
    id: u64,
    name: String,
}

type SortList = Mutex<Vec<Sort>>;

#[get("/sort")]
fn get_all(list: &State<SortList>) -> Json<Vec<Sort>> {
    let items = list.lock().unwrap();
    Json(items.clone())
}

#[get("/sort/<id>")]
fn get_by_id(id: u64, list: &State<SortList>) -> Option<Json<Sort>> {
    let items = list.lock().unwrap();
    items.iter()
        .find(|item| item.id == id)
        .map(|item| Json(item.clone()))
}

#[post("/sort", data = "<item>")]
fn create(item: Json<Sort>, list: &State<SortList>) -> Json<Sort> {
    let mut items = list.lock().unwrap();
    items.push(item.clone());
    item
}

#[put("/sort/<id>", data = "<item>")]
fn update(id: u64, item: Json<Sort>, list: &State<SortList>) -> Option<Json<Sort>> {
    let mut items = list.lock().unwrap();
    items.iter_mut()
        .find(|i| i.id == id)
        .map(|i| {
            *i = item.clone();
            Json(i.clone())
        })
}

#[delete("/sort/<id>")]
fn delete(id: u64, list: &State<SortList>) -> Option<()> {
    let mut items = list.lock().unwrap();
    let pos = items.iter().position(|i| i.id == id)?;
    items.remove(pos);
    Some(())
}

#[launch]
fn rocket() -> _ {
    rocket::build()
        .manage(SortList::new(Vec::new()))
        .mount("/api", routes![get_all, get_by_id, create, update, delete])
}
