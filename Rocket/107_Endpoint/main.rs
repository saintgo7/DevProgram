#[macro_use] extern crate rocket;

use rocket::serde::{json::Json, Deserialize, Serialize};
use rocket::State;
use std::sync::Mutex;

#[derive(Serialize, Deserialize, Clone)]
#[serde(crate = "rocket::serde")]
struct Endpoint {
    id: u64,
    name: String,
}

type EndpointList = Mutex<Vec<Endpoint>>;

#[get("/endpoint")]
fn get_all(list: &State<EndpointList>) -> Json<Vec<Endpoint>> {
    let items = list.lock().unwrap();
    Json(items.clone())
}

#[get("/endpoint/<id>")]
fn get_by_id(id: u64, list: &State<EndpointList>) -> Option<Json<Endpoint>> {
    let items = list.lock().unwrap();
    items.iter()
        .find(|item| item.id == id)
        .map(|item| Json(item.clone()))
}

#[post("/endpoint", data = "<item>")]
fn create(item: Json<Endpoint>, list: &State<EndpointList>) -> Json<Endpoint> {
    let mut items = list.lock().unwrap();
    items.push(item.clone());
    item
}

#[put("/endpoint/<id>", data = "<item>")]
fn update(id: u64, item: Json<Endpoint>, list: &State<EndpointList>) -> Option<Json<Endpoint>> {
    let mut items = list.lock().unwrap();
    items.iter_mut()
        .find(|i| i.id == id)
        .map(|i| {
            *i = item.clone();
            Json(i.clone())
        })
}

#[delete("/endpoint/<id>")]
fn delete(id: u64, list: &State<EndpointList>) -> Option<()> {
    let mut items = list.lock().unwrap();
    let pos = items.iter().position(|i| i.id == id)?;
    items.remove(pos);
    Some(())
}

#[launch]
fn rocket() -> _ {
    rocket::build()
        .manage(EndpointList::new(Vec::new()))
        .mount("/api", routes![get_all, get_by_id, create, update, delete])
}
