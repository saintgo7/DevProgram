#[macro_use] extern crate rocket;

use rocket::serde::{json::Json, Deserialize, Serialize};
use rocket::State;
use std::sync::Mutex;

#[derive(Serialize, Deserialize, Clone)]
#[serde(crate = "rocket::serde")]
struct Factory {
    id: u64,
    name: String,
}

type FactoryList = Mutex<Vec<Factory>>;

#[get("/factory")]
fn get_all(list: &State<FactoryList>) -> Json<Vec<Factory>> {
    let items = list.lock().unwrap();
    Json(items.clone())
}

#[get("/factory/<id>")]
fn get_by_id(id: u64, list: &State<FactoryList>) -> Option<Json<Factory>> {
    let items = list.lock().unwrap();
    items.iter()
        .find(|item| item.id == id)
        .map(|item| Json(item.clone()))
}

#[post("/factory", data = "<item>")]
fn create(item: Json<Factory>, list: &State<FactoryList>) -> Json<Factory> {
    let mut items = list.lock().unwrap();
    items.push(item.clone());
    item
}

#[put("/factory/<id>", data = "<item>")]
fn update(id: u64, item: Json<Factory>, list: &State<FactoryList>) -> Option<Json<Factory>> {
    let mut items = list.lock().unwrap();
    items.iter_mut()
        .find(|i| i.id == id)
        .map(|i| {
            *i = item.clone();
            Json(i.clone())
        })
}

#[delete("/factory/<id>")]
fn delete(id: u64, list: &State<FactoryList>) -> Option<()> {
    let mut items = list.lock().unwrap();
    let pos = items.iter().position(|i| i.id == id)?;
    items.remove(pos);
    Some(())
}

#[launch]
fn rocket() -> _ {
    rocket::build()
        .manage(FactoryList::new(Vec::new()))
        .mount("/api", routes![get_all, get_by_id, create, update, delete])
}
