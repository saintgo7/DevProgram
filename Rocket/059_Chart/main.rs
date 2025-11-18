#[macro_use] extern crate rocket;

use rocket::serde::{json::Json, Deserialize, Serialize};
use rocket::State;
use std::sync::Mutex;

#[derive(Serialize, Deserialize, Clone)]
#[serde(crate = "rocket::serde")]
struct Chart {
    id: u64,
    name: String,
}

type ChartList = Mutex<Vec<Chart>>;

#[get("/chart")]
fn get_all(list: &State<ChartList>) -> Json<Vec<Chart>> {
    let items = list.lock().unwrap();
    Json(items.clone())
}

#[get("/chart/<id>")]
fn get_by_id(id: u64, list: &State<ChartList>) -> Option<Json<Chart>> {
    let items = list.lock().unwrap();
    items.iter()
        .find(|item| item.id == id)
        .map(|item| Json(item.clone()))
}

#[post("/chart", data = "<item>")]
fn create(item: Json<Chart>, list: &State<ChartList>) -> Json<Chart> {
    let mut items = list.lock().unwrap();
    items.push(item.clone());
    item
}

#[put("/chart/<id>", data = "<item>")]
fn update(id: u64, item: Json<Chart>, list: &State<ChartList>) -> Option<Json<Chart>> {
    let mut items = list.lock().unwrap();
    items.iter_mut()
        .find(|i| i.id == id)
        .map(|i| {
            *i = item.clone();
            Json(i.clone())
        })
}

#[delete("/chart/<id>")]
fn delete(id: u64, list: &State<ChartList>) -> Option<()> {
    let mut items = list.lock().unwrap();
    let pos = items.iter().position(|i| i.id == id)?;
    items.remove(pos);
    Some(())
}

#[launch]
fn rocket() -> _ {
    rocket::build()
        .manage(ChartList::new(Vec::new()))
        .mount("/api", routes![get_all, get_by_id, create, update, delete])
}
