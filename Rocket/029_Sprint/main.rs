#[macro_use] extern crate rocket;

use rocket::serde::{json::Json, Deserialize, Serialize};
use rocket::State;
use std::sync::Mutex;

#[derive(Serialize, Deserialize, Clone)]
#[serde(crate = "rocket::serde")]
struct Sprint {
    id: u64,
    name: String,
}

type SprintList = Mutex<Vec<Sprint>>;

#[get("/sprint")]
fn get_all(list: &State<SprintList>) -> Json<Vec<Sprint>> {
    let items = list.lock().unwrap();
    Json(items.clone())
}

#[get("/sprint/<id>")]
fn get_by_id(id: u64, list: &State<SprintList>) -> Option<Json<Sprint>> {
    let items = list.lock().unwrap();
    items.iter()
        .find(|item| item.id == id)
        .map(|item| Json(item.clone()))
}

#[post("/sprint", data = "<item>")]
fn create(item: Json<Sprint>, list: &State<SprintList>) -> Json<Sprint> {
    let mut items = list.lock().unwrap();
    items.push(item.clone());
    item
}

#[put("/sprint/<id>", data = "<item>")]
fn update(id: u64, item: Json<Sprint>, list: &State<SprintList>) -> Option<Json<Sprint>> {
    let mut items = list.lock().unwrap();
    items.iter_mut()
        .find(|i| i.id == id)
        .map(|i| {
            *i = item.clone();
            Json(i.clone())
        })
}

#[delete("/sprint/<id>")]
fn delete(id: u64, list: &State<SprintList>) -> Option<()> {
    let mut items = list.lock().unwrap();
    let pos = items.iter().position(|i| i.id == id)?;
    items.remove(pos);
    Some(())
}

#[launch]
fn rocket() -> _ {
    rocket::build()
        .manage(SprintList::new(Vec::new()))
        .mount("/api", routes![get_all, get_by_id, create, update, delete])
}
