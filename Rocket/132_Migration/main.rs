#[macro_use] extern crate rocket;

use rocket::serde::{json::Json, Deserialize, Serialize};
use rocket::State;
use std::sync::Mutex;

#[derive(Serialize, Deserialize, Clone)]
#[serde(crate = "rocket::serde")]
struct Migration {
    id: u64,
    name: String,
}

type MigrationList = Mutex<Vec<Migration>>;

#[get("/migration")]
fn get_all(list: &State<MigrationList>) -> Json<Vec<Migration>> {
    let items = list.lock().unwrap();
    Json(items.clone())
}

#[get("/migration/<id>")]
fn get_by_id(id: u64, list: &State<MigrationList>) -> Option<Json<Migration>> {
    let items = list.lock().unwrap();
    items.iter()
        .find(|item| item.id == id)
        .map(|item| Json(item.clone()))
}

#[post("/migration", data = "<item>")]
fn create(item: Json<Migration>, list: &State<MigrationList>) -> Json<Migration> {
    let mut items = list.lock().unwrap();
    items.push(item.clone());
    item
}

#[put("/migration/<id>", data = "<item>")]
fn update(id: u64, item: Json<Migration>, list: &State<MigrationList>) -> Option<Json<Migration>> {
    let mut items = list.lock().unwrap();
    items.iter_mut()
        .find(|i| i.id == id)
        .map(|i| {
            *i = item.clone();
            Json(i.clone())
        })
}

#[delete("/migration/<id>")]
fn delete(id: u64, list: &State<MigrationList>) -> Option<()> {
    let mut items = list.lock().unwrap();
    let pos = items.iter().position(|i| i.id == id)?;
    items.remove(pos);
    Some(())
}

#[launch]
fn rocket() -> _ {
    rocket::build()
        .manage(MigrationList::new(Vec::new()))
        .mount("/api", routes![get_all, get_by_id, create, update, delete])
}
