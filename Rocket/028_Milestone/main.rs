#[macro_use] extern crate rocket;

use rocket::serde::{json::Json, Deserialize, Serialize};
use rocket::State;
use std::sync::Mutex;

#[derive(Serialize, Deserialize, Clone)]
#[serde(crate = "rocket::serde")]
struct Milestone {
    id: u64,
    name: String,
}

type MilestoneList = Mutex<Vec<Milestone>>;

#[get("/milestone")]
fn get_all(list: &State<MilestoneList>) -> Json<Vec<Milestone>> {
    let items = list.lock().unwrap();
    Json(items.clone())
}

#[get("/milestone/<id>")]
fn get_by_id(id: u64, list: &State<MilestoneList>) -> Option<Json<Milestone>> {
    let items = list.lock().unwrap();
    items.iter()
        .find(|item| item.id == id)
        .map(|item| Json(item.clone()))
}

#[post("/milestone", data = "<item>")]
fn create(item: Json<Milestone>, list: &State<MilestoneList>) -> Json<Milestone> {
    let mut items = list.lock().unwrap();
    items.push(item.clone());
    item
}

#[put("/milestone/<id>", data = "<item>")]
fn update(id: u64, item: Json<Milestone>, list: &State<MilestoneList>) -> Option<Json<Milestone>> {
    let mut items = list.lock().unwrap();
    items.iter_mut()
        .find(|i| i.id == id)
        .map(|i| {
            *i = item.clone();
            Json(i.clone())
        })
}

#[delete("/milestone/<id>")]
fn delete(id: u64, list: &State<MilestoneList>) -> Option<()> {
    let mut items = list.lock().unwrap();
    let pos = items.iter().position(|i| i.id == id)?;
    items.remove(pos);
    Some(())
}

#[launch]
fn rocket() -> _ {
    rocket::build()
        .manage(MilestoneList::new(Vec::new()))
        .mount("/api", routes![get_all, get_by_id, create, update, delete])
}
