#[macro_use] extern crate rocket;

use rocket::serde::{json::Json, Deserialize, Serialize};
use rocket::State;
use std::sync::Mutex;

#[derive(Serialize, Deserialize, Clone)]
#[serde(crate = "rocket::serde")]
struct Analytics {
    id: u64,
    name: String,
}

type AnalyticsList = Mutex<Vec<Analytics>>;

#[get("/analytics")]
fn get_all(list: &State<AnalyticsList>) -> Json<Vec<Analytics>> {
    let items = list.lock().unwrap();
    Json(items.clone())
}

#[get("/analytics/<id>")]
fn get_by_id(id: u64, list: &State<AnalyticsList>) -> Option<Json<Analytics>> {
    let items = list.lock().unwrap();
    items.iter()
        .find(|item| item.id == id)
        .map(|item| Json(item.clone()))
}

#[post("/analytics", data = "<item>")]
fn create(item: Json<Analytics>, list: &State<AnalyticsList>) -> Json<Analytics> {
    let mut items = list.lock().unwrap();
    items.push(item.clone());
    item
}

#[put("/analytics/<id>", data = "<item>")]
fn update(id: u64, item: Json<Analytics>, list: &State<AnalyticsList>) -> Option<Json<Analytics>> {
    let mut items = list.lock().unwrap();
    items.iter_mut()
        .find(|i| i.id == id)
        .map(|i| {
            *i = item.clone();
            Json(i.clone())
        })
}

#[delete("/analytics/<id>")]
fn delete(id: u64, list: &State<AnalyticsList>) -> Option<()> {
    let mut items = list.lock().unwrap();
    let pos = items.iter().position(|i| i.id == id)?;
    items.remove(pos);
    Some(())
}

#[launch]
fn rocket() -> _ {
    rocket::build()
        .manage(AnalyticsList::new(Vec::new()))
        .mount("/api", routes![get_all, get_by_id, create, update, delete])
}
