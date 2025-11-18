#[macro_use] extern crate rocket;

use rocket::serde::{json::Json, Deserialize, Serialize};
use rocket::State;
use std::sync::Mutex;

#[derive(Serialize, Deserialize, Clone)]
#[serde(crate = "rocket::serde")]
struct Security {
    id: u64,
    name: String,
}

type SecurityList = Mutex<Vec<Security>>;

#[get("/security")]
fn get_all(list: &State<SecurityList>) -> Json<Vec<Security>> {
    let items = list.lock().unwrap();
    Json(items.clone())
}

#[get("/security/<id>")]
fn get_by_id(id: u64, list: &State<SecurityList>) -> Option<Json<Security>> {
    let items = list.lock().unwrap();
    items.iter()
        .find(|item| item.id == id)
        .map(|item| Json(item.clone()))
}

#[post("/security", data = "<item>")]
fn create(item: Json<Security>, list: &State<SecurityList>) -> Json<Security> {
    let mut items = list.lock().unwrap();
    items.push(item.clone());
    item
}

#[put("/security/<id>", data = "<item>")]
fn update(id: u64, item: Json<Security>, list: &State<SecurityList>) -> Option<Json<Security>> {
    let mut items = list.lock().unwrap();
    items.iter_mut()
        .find(|i| i.id == id)
        .map(|i| {
            *i = item.clone();
            Json(i.clone())
        })
}

#[delete("/security/<id>")]
fn delete(id: u64, list: &State<SecurityList>) -> Option<()> {
    let mut items = list.lock().unwrap();
    let pos = items.iter().position(|i| i.id == id)?;
    items.remove(pos);
    Some(())
}

#[launch]
fn rocket() -> _ {
    rocket::build()
        .manage(SecurityList::new(Vec::new()))
        .mount("/api", routes![get_all, get_by_id, create, update, delete])
}
