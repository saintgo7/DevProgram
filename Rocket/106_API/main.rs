#[macro_use] extern crate rocket;

use rocket::serde::{json::Json, Deserialize, Serialize};
use rocket::State;
use std::sync::Mutex;

#[derive(Serialize, Deserialize, Clone)]
#[serde(crate = "rocket::serde")]
struct API {
    id: u64,
    name: String,
}

type APIList = Mutex<Vec<API>>;

#[get("/api")]
fn get_all(list: &State<APIList>) -> Json<Vec<API>> {
    let items = list.lock().unwrap();
    Json(items.clone())
}

#[get("/api/<id>")]
fn get_by_id(id: u64, list: &State<APIList>) -> Option<Json<API>> {
    let items = list.lock().unwrap();
    items.iter()
        .find(|item| item.id == id)
        .map(|item| Json(item.clone()))
}

#[post("/api", data = "<item>")]
fn create(item: Json<API>, list: &State<APIList>) -> Json<API> {
    let mut items = list.lock().unwrap();
    items.push(item.clone());
    item
}

#[put("/api/<id>", data = "<item>")]
fn update(id: u64, item: Json<API>, list: &State<APIList>) -> Option<Json<API>> {
    let mut items = list.lock().unwrap();
    items.iter_mut()
        .find(|i| i.id == id)
        .map(|i| {
            *i = item.clone();
            Json(i.clone())
        })
}

#[delete("/api/<id>")]
fn delete(id: u64, list: &State<APIList>) -> Option<()> {
    let mut items = list.lock().unwrap();
    let pos = items.iter().position(|i| i.id == id)?;
    items.remove(pos);
    Some(())
}

#[launch]
fn rocket() -> _ {
    rocket::build()
        .manage(APIList::new(Vec::new()))
        .mount("/api", routes![get_all, get_by_id, create, update, delete])
}
