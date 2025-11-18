#[macro_use] extern crate rocket;

use rocket::serde::{json::Json, Deserialize, Serialize};
use rocket::State;
use std::sync::Mutex;

#[derive(Serialize, Deserialize, Clone)]
#[serde(crate = "rocket::serde")]
struct Retailer {
    id: u64,
    name: String,
}

type RetailerList = Mutex<Vec<Retailer>>;

#[get("/retailer")]
fn get_all(list: &State<RetailerList>) -> Json<Vec<Retailer>> {
    let items = list.lock().unwrap();
    Json(items.clone())
}

#[get("/retailer/<id>")]
fn get_by_id(id: u64, list: &State<RetailerList>) -> Option<Json<Retailer>> {
    let items = list.lock().unwrap();
    items.iter()
        .find(|item| item.id == id)
        .map(|item| Json(item.clone()))
}

#[post("/retailer", data = "<item>")]
fn create(item: Json<Retailer>, list: &State<RetailerList>) -> Json<Retailer> {
    let mut items = list.lock().unwrap();
    items.push(item.clone());
    item
}

#[put("/retailer/<id>", data = "<item>")]
fn update(id: u64, item: Json<Retailer>, list: &State<RetailerList>) -> Option<Json<Retailer>> {
    let mut items = list.lock().unwrap();
    items.iter_mut()
        .find(|i| i.id == id)
        .map(|i| {
            *i = item.clone();
            Json(i.clone())
        })
}

#[delete("/retailer/<id>")]
fn delete(id: u64, list: &State<RetailerList>) -> Option<()> {
    let mut items = list.lock().unwrap();
    let pos = items.iter().position(|i| i.id == id)?;
    items.remove(pos);
    Some(())
}

#[launch]
fn rocket() -> _ {
    rocket::build()
        .manage(RetailerList::new(Vec::new()))
        .mount("/api", routes![get_all, get_by_id, create, update, delete])
}
