#[macro_use] extern crate rocket;

use rocket::serde::{json::Json, Deserialize, Serialize};
use rocket::State;
use std::sync::Mutex;

#[derive(Serialize, Deserialize, Clone)]
#[serde(crate = "rocket::serde")]
struct Distributor {
    id: u64,
    name: String,
}

type DistributorList = Mutex<Vec<Distributor>>;

#[get("/distributor")]
fn get_all(list: &State<DistributorList>) -> Json<Vec<Distributor>> {
    let items = list.lock().unwrap();
    Json(items.clone())
}

#[get("/distributor/<id>")]
fn get_by_id(id: u64, list: &State<DistributorList>) -> Option<Json<Distributor>> {
    let items = list.lock().unwrap();
    items.iter()
        .find(|item| item.id == id)
        .map(|item| Json(item.clone()))
}

#[post("/distributor", data = "<item>")]
fn create(item: Json<Distributor>, list: &State<DistributorList>) -> Json<Distributor> {
    let mut items = list.lock().unwrap();
    items.push(item.clone());
    item
}

#[put("/distributor/<id>", data = "<item>")]
fn update(id: u64, item: Json<Distributor>, list: &State<DistributorList>) -> Option<Json<Distributor>> {
    let mut items = list.lock().unwrap();
    items.iter_mut()
        .find(|i| i.id == id)
        .map(|i| {
            *i = item.clone();
            Json(i.clone())
        })
}

#[delete("/distributor/<id>")]
fn delete(id: u64, list: &State<DistributorList>) -> Option<()> {
    let mut items = list.lock().unwrap();
    let pos = items.iter().position(|i| i.id == id)?;
    items.remove(pos);
    Some(())
}

#[launch]
fn rocket() -> _ {
    rocket::build()
        .manage(DistributorList::new(Vec::new()))
        .mount("/api", routes![get_all, get_by_id, create, update, delete])
}
