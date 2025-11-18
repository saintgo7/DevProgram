#[macro_use] extern crate rocket;

use rocket::serde::{json::Json, Deserialize, Serialize};
use rocket::State;
use std::sync::Mutex;

#[derive(Serialize, Deserialize, Clone)]
#[serde(crate = "rocket::serde")]
struct Relationship {
    id: u64,
    name: String,
}

type RelationshipList = Mutex<Vec<Relationship>>;

#[get("/relationship")]
fn get_all(list: &State<RelationshipList>) -> Json<Vec<Relationship>> {
    let items = list.lock().unwrap();
    Json(items.clone())
}

#[get("/relationship/<id>")]
fn get_by_id(id: u64, list: &State<RelationshipList>) -> Option<Json<Relationship>> {
    let items = list.lock().unwrap();
    items.iter()
        .find(|item| item.id == id)
        .map(|item| Json(item.clone()))
}

#[post("/relationship", data = "<item>")]
fn create(item: Json<Relationship>, list: &State<RelationshipList>) -> Json<Relationship> {
    let mut items = list.lock().unwrap();
    items.push(item.clone());
    item
}

#[put("/relationship/<id>", data = "<item>")]
fn update(id: u64, item: Json<Relationship>, list: &State<RelationshipList>) -> Option<Json<Relationship>> {
    let mut items = list.lock().unwrap();
    items.iter_mut()
        .find(|i| i.id == id)
        .map(|i| {
            *i = item.clone();
            Json(i.clone())
        })
}

#[delete("/relationship/<id>")]
fn delete(id: u64, list: &State<RelationshipList>) -> Option<()> {
    let mut items = list.lock().unwrap();
    let pos = items.iter().position(|i| i.id == id)?;
    items.remove(pos);
    Some(())
}

#[launch]
fn rocket() -> _ {
    rocket::build()
        .manage(RelationshipList::new(Vec::new()))
        .mount("/api", routes![get_all, get_by_id, create, update, delete])
}
