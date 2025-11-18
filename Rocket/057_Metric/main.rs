#[macro_use] extern crate rocket;

use rocket::serde::{json::Json, Deserialize, Serialize};
use rocket::State;
use std::sync::Mutex;

#[derive(Serialize, Deserialize, Clone)]
#[serde(crate = "rocket::serde")]
struct Metric {
    id: u64,
    name: String,
}

type MetricList = Mutex<Vec<Metric>>;

#[get("/metric")]
fn get_all(list: &State<MetricList>) -> Json<Vec<Metric>> {
    let items = list.lock().unwrap();
    Json(items.clone())
}

#[get("/metric/<id>")]
fn get_by_id(id: u64, list: &State<MetricList>) -> Option<Json<Metric>> {
    let items = list.lock().unwrap();
    items.iter()
        .find(|item| item.id == id)
        .map(|item| Json(item.clone()))
}

#[post("/metric", data = "<item>")]
fn create(item: Json<Metric>, list: &State<MetricList>) -> Json<Metric> {
    let mut items = list.lock().unwrap();
    items.push(item.clone());
    item
}

#[put("/metric/<id>", data = "<item>")]
fn update(id: u64, item: Json<Metric>, list: &State<MetricList>) -> Option<Json<Metric>> {
    let mut items = list.lock().unwrap();
    items.iter_mut()
        .find(|i| i.id == id)
        .map(|i| {
            *i = item.clone();
            Json(i.clone())
        })
}

#[delete("/metric/<id>")]
fn delete(id: u64, list: &State<MetricList>) -> Option<()> {
    let mut items = list.lock().unwrap();
    let pos = items.iter().position(|i| i.id == id)?;
    items.remove(pos);
    Some(())
}

#[launch]
fn rocket() -> _ {
    rocket::build()
        .manage(MetricList::new(Vec::new()))
        .mount("/api", routes![get_all, get_by_id, create, update, delete])
}
