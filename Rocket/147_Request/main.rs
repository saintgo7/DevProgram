#[macro_use] extern crate rocket;

use rocket::serde::{json::Json, Deserialize, Serialize};
use rocket::State;
use std::sync::Mutex;

#[derive(Serialize, Deserialize, Clone)]
#[serde(crate = "rocket::serde")]
struct Request {
    id: u64,
    name: String,
}

type RequestList = Mutex<Vec<Request>>;

#[get("/request")]
fn get_all(list: &State<RequestList>) -> Json<Vec<Request>> {
    let items = list.lock().unwrap();
    Json(items.clone())
}

#[get("/request/<id>")]
fn get_by_id(id: u64, list: &State<RequestList>) -> Option<Json<Request>> {
    let items = list.lock().unwrap();
    items.iter()
        .find(|item| item.id == id)
        .map(|item| Json(item.clone()))
}

#[post("/request", data = "<item>")]
fn create(item: Json<Request>, list: &State<RequestList>) -> Json<Request> {
    let mut items = list.lock().unwrap();
    items.push(item.clone());
    item
}

#[put("/request/<id>", data = "<item>")]
fn update(id: u64, item: Json<Request>, list: &State<RequestList>) -> Option<Json<Request>> {
    let mut items = list.lock().unwrap();
    items.iter_mut()
        .find(|i| i.id == id)
        .map(|i| {
            *i = item.clone();
            Json(i.clone())
        })
}

#[delete("/request/<id>")]
fn delete(id: u64, list: &State<RequestList>) -> Option<()> {
    let mut items = list.lock().unwrap();
    let pos = items.iter().position(|i| i.id == id)?;
    items.remove(pos);
    Some(())
}

#[launch]
fn rocket() -> _ {
    rocket::build()
        .manage(RequestList::new(Vec::new()))
        .mount("/api", routes![get_all, get_by_id, create, update, delete])
}
