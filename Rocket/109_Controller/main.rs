#[macro_use] extern crate rocket;

use rocket::serde::{json::Json, Deserialize, Serialize};
use rocket::State;
use std::sync::Mutex;

#[derive(Serialize, Deserialize, Clone)]
#[serde(crate = "rocket::serde")]
struct Controller {
    id: u64,
    name: String,
}

type ControllerList = Mutex<Vec<Controller>>;

#[get("/controller")]
fn get_all(list: &State<ControllerList>) -> Json<Vec<Controller>> {
    let items = list.lock().unwrap();
    Json(items.clone())
}

#[get("/controller/<id>")]
fn get_by_id(id: u64, list: &State<ControllerList>) -> Option<Json<Controller>> {
    let items = list.lock().unwrap();
    items.iter()
        .find(|item| item.id == id)
        .map(|item| Json(item.clone()))
}

#[post("/controller", data = "<item>")]
fn create(item: Json<Controller>, list: &State<ControllerList>) -> Json<Controller> {
    let mut items = list.lock().unwrap();
    items.push(item.clone());
    item
}

#[put("/controller/<id>", data = "<item>")]
fn update(id: u64, item: Json<Controller>, list: &State<ControllerList>) -> Option<Json<Controller>> {
    let mut items = list.lock().unwrap();
    items.iter_mut()
        .find(|i| i.id == id)
        .map(|i| {
            *i = item.clone();
            Json(i.clone())
        })
}

#[delete("/controller/<id>")]
fn delete(id: u64, list: &State<ControllerList>) -> Option<()> {
    let mut items = list.lock().unwrap();
    let pos = items.iter().position(|i| i.id == id)?;
    items.remove(pos);
    Some(())
}

#[launch]
fn rocket() -> _ {
    rocket::build()
        .manage(ControllerList::new(Vec::new()))
        .mount("/api", routes![get_all, get_by_id, create, update, delete])
}
