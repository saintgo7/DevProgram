#[macro_use] extern crate rocket;

use rocket::serde::{json::Json, Deserialize, Serialize};
use rocket::State;
use std::sync::Mutex;

#[derive(Serialize, Deserialize, Clone)]
#[serde(crate = "rocket::serde")]
struct Charge {
    id: u64,
    name: String,
}

type ChargeList = Mutex<Vec<Charge>>;

#[get("/charge")]
fn get_all(list: &State<ChargeList>) -> Json<Vec<Charge>> {
    let items = list.lock().unwrap();
    Json(items.clone())
}

#[get("/charge/<id>")]
fn get_by_id(id: u64, list: &State<ChargeList>) -> Option<Json<Charge>> {
    let items = list.lock().unwrap();
    items.iter()
        .find(|item| item.id == id)
        .map(|item| Json(item.clone()))
}

#[post("/charge", data = "<item>")]
fn create(item: Json<Charge>, list: &State<ChargeList>) -> Json<Charge> {
    let mut items = list.lock().unwrap();
    items.push(item.clone());
    item
}

#[put("/charge/<id>", data = "<item>")]
fn update(id: u64, item: Json<Charge>, list: &State<ChargeList>) -> Option<Json<Charge>> {
    let mut items = list.lock().unwrap();
    items.iter_mut()
        .find(|i| i.id == id)
        .map(|i| {
            *i = item.clone();
            Json(i.clone())
        })
}

#[delete("/charge/<id>")]
fn delete(id: u64, list: &State<ChargeList>) -> Option<()> {
    let mut items = list.lock().unwrap();
    let pos = items.iter().position(|i| i.id == id)?;
    items.remove(pos);
    Some(())
}

#[launch]
fn rocket() -> _ {
    rocket::build()
        .manage(ChargeList::new(Vec::new()))
        .mount("/api", routes![get_all, get_by_id, create, update, delete])
}
