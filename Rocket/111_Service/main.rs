#[macro_use] extern crate rocket;

use rocket::serde::{json::Json, Deserialize, Serialize};
use rocket::State;
use std::sync::Mutex;

#[derive(Serialize, Deserialize, Clone)]
#[serde(crate = "rocket::serde")]
struct Service {
    id: u64,
    name: String,
}

type ServiceList = Mutex<Vec<Service>>;

#[get("/service")]
fn get_all(list: &State<ServiceList>) -> Json<Vec<Service>> {
    let items = list.lock().unwrap();
    Json(items.clone())
}

#[get("/service/<id>")]
fn get_by_id(id: u64, list: &State<ServiceList>) -> Option<Json<Service>> {
    let items = list.lock().unwrap();
    items.iter()
        .find(|item| item.id == id)
        .map(|item| Json(item.clone()))
}

#[post("/service", data = "<item>")]
fn create(item: Json<Service>, list: &State<ServiceList>) -> Json<Service> {
    let mut items = list.lock().unwrap();
    items.push(item.clone());
    item
}

#[put("/service/<id>", data = "<item>")]
fn update(id: u64, item: Json<Service>, list: &State<ServiceList>) -> Option<Json<Service>> {
    let mut items = list.lock().unwrap();
    items.iter_mut()
        .find(|i| i.id == id)
        .map(|i| {
            *i = item.clone();
            Json(i.clone())
        })
}

#[delete("/service/<id>")]
fn delete(id: u64, list: &State<ServiceList>) -> Option<()> {
    let mut items = list.lock().unwrap();
    let pos = items.iter().position(|i| i.id == id)?;
    items.remove(pos);
    Some(())
}

#[launch]
fn rocket() -> _ {
    rocket::build()
        .manage(ServiceList::new(Vec::new()))
        .mount("/api", routes![get_all, get_by_id, create, update, delete])
}
