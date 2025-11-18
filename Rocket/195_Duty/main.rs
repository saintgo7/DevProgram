#[macro_use] extern crate rocket;

use rocket::serde::{json::Json, Deserialize, Serialize};
use rocket::State;
use std::sync::Mutex;

#[derive(Serialize, Deserialize, Clone)]
#[serde(crate = "rocket::serde")]
struct Duty {
    id: u64,
    name: String,
}

type DutyList = Mutex<Vec<Duty>>;

#[get("/duty")]
fn get_all(list: &State<DutyList>) -> Json<Vec<Duty>> {
    let items = list.lock().unwrap();
    Json(items.clone())
}

#[get("/duty/<id>")]
fn get_by_id(id: u64, list: &State<DutyList>) -> Option<Json<Duty>> {
    let items = list.lock().unwrap();
    items.iter()
        .find(|item| item.id == id)
        .map(|item| Json(item.clone()))
}

#[post("/duty", data = "<item>")]
fn create(item: Json<Duty>, list: &State<DutyList>) -> Json<Duty> {
    let mut items = list.lock().unwrap();
    items.push(item.clone());
    item
}

#[put("/duty/<id>", data = "<item>")]
fn update(id: u64, item: Json<Duty>, list: &State<DutyList>) -> Option<Json<Duty>> {
    let mut items = list.lock().unwrap();
    items.iter_mut()
        .find(|i| i.id == id)
        .map(|i| {
            *i = item.clone();
            Json(i.clone())
        })
}

#[delete("/duty/<id>")]
fn delete(id: u64, list: &State<DutyList>) -> Option<()> {
    let mut items = list.lock().unwrap();
    let pos = items.iter().position(|i| i.id == id)?;
    items.remove(pos);
    Some(())
}

#[launch]
fn rocket() -> _ {
    rocket::build()
        .manage(DutyList::new(Vec::new()))
        .mount("/api", routes![get_all, get_by_id, create, update, delete])
}
