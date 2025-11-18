#[macro_use] extern crate rocket;

use rocket::serde::{json::Json, Deserialize, Serialize};
use rocket::State;
use std::sync::Mutex;

#[derive(Serialize, Deserialize, Clone)]
#[serde(crate = "rocket::serde")]
struct Rate {
    id: u64,
    name: String,
}

type RateList = Mutex<Vec<Rate>>;

#[get("/rate")]
fn get_all(list: &State<RateList>) -> Json<Vec<Rate>> {
    let items = list.lock().unwrap();
    Json(items.clone())
}

#[get("/rate/<id>")]
fn get_by_id(id: u64, list: &State<RateList>) -> Option<Json<Rate>> {
    let items = list.lock().unwrap();
    items.iter()
        .find(|item| item.id == id)
        .map(|item| Json(item.clone()))
}

#[post("/rate", data = "<item>")]
fn create(item: Json<Rate>, list: &State<RateList>) -> Json<Rate> {
    let mut items = list.lock().unwrap();
    items.push(item.clone());
    item
}

#[put("/rate/<id>", data = "<item>")]
fn update(id: u64, item: Json<Rate>, list: &State<RateList>) -> Option<Json<Rate>> {
    let mut items = list.lock().unwrap();
    items.iter_mut()
        .find(|i| i.id == id)
        .map(|i| {
            *i = item.clone();
            Json(i.clone())
        })
}

#[delete("/rate/<id>")]
fn delete(id: u64, list: &State<RateList>) -> Option<()> {
    let mut items = list.lock().unwrap();
    let pos = items.iter().position(|i| i.id == id)?;
    items.remove(pos);
    Some(())
}

#[launch]
fn rocket() -> _ {
    rocket::build()
        .manage(RateList::new(Vec::new()))
        .mount("/api", routes![get_all, get_by_id, create, update, delete])
}
