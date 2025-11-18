#[macro_use] extern crate rocket;

use rocket::serde::{json::Json, Deserialize, Serialize};
use rocket::State;
use std::sync::Mutex;

#[derive(Serialize, Deserialize, Clone)]
#[serde(crate = "rocket::serde")]
struct Criteria {
    id: u64,
    name: String,
}

type CriteriaList = Mutex<Vec<Criteria>>;

#[get("/criteria")]
fn get_all(list: &State<CriteriaList>) -> Json<Vec<Criteria>> {
    let items = list.lock().unwrap();
    Json(items.clone())
}

#[get("/criteria/<id>")]
fn get_by_id(id: u64, list: &State<CriteriaList>) -> Option<Json<Criteria>> {
    let items = list.lock().unwrap();
    items.iter()
        .find(|item| item.id == id)
        .map(|item| Json(item.clone()))
}

#[post("/criteria", data = "<item>")]
fn create(item: Json<Criteria>, list: &State<CriteriaList>) -> Json<Criteria> {
    let mut items = list.lock().unwrap();
    items.push(item.clone());
    item
}

#[put("/criteria/<id>", data = "<item>")]
fn update(id: u64, item: Json<Criteria>, list: &State<CriteriaList>) -> Option<Json<Criteria>> {
    let mut items = list.lock().unwrap();
    items.iter_mut()
        .find(|i| i.id == id)
        .map(|i| {
            *i = item.clone();
            Json(i.clone())
        })
}

#[delete("/criteria/<id>")]
fn delete(id: u64, list: &State<CriteriaList>) -> Option<()> {
    let mut items = list.lock().unwrap();
    let pos = items.iter().position(|i| i.id == id)?;
    items.remove(pos);
    Some(())
}

#[launch]
fn rocket() -> _ {
    rocket::build()
        .manage(CriteriaList::new(Vec::new()))
        .mount("/api", routes![get_all, get_by_id, create, update, delete])
}
