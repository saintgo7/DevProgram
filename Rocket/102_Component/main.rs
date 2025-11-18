#[macro_use] extern crate rocket;

use rocket::serde::{json::Json, Deserialize, Serialize};
use rocket::State;
use std::sync::Mutex;

#[derive(Serialize, Deserialize, Clone)]
#[serde(crate = "rocket::serde")]
struct Component {
    id: u64,
    name: String,
}

type ComponentList = Mutex<Vec<Component>>;

#[get("/component")]
fn get_all(list: &State<ComponentList>) -> Json<Vec<Component>> {
    let items = list.lock().unwrap();
    Json(items.clone())
}

#[get("/component/<id>")]
fn get_by_id(id: u64, list: &State<ComponentList>) -> Option<Json<Component>> {
    let items = list.lock().unwrap();
    items.iter()
        .find(|item| item.id == id)
        .map(|item| Json(item.clone()))
}

#[post("/component", data = "<item>")]
fn create(item: Json<Component>, list: &State<ComponentList>) -> Json<Component> {
    let mut items = list.lock().unwrap();
    items.push(item.clone());
    item
}

#[put("/component/<id>", data = "<item>")]
fn update(id: u64, item: Json<Component>, list: &State<ComponentList>) -> Option<Json<Component>> {
    let mut items = list.lock().unwrap();
    items.iter_mut()
        .find(|i| i.id == id)
        .map(|i| {
            *i = item.clone();
            Json(i.clone())
        })
}

#[delete("/component/<id>")]
fn delete(id: u64, list: &State<ComponentList>) -> Option<()> {
    let mut items = list.lock().unwrap();
    let pos = items.iter().position(|i| i.id == id)?;
    items.remove(pos);
    Some(())
}

#[launch]
fn rocket() -> _ {
    rocket::build()
        .manage(ComponentList::new(Vec::new()))
        .mount("/api", routes![get_all, get_by_id, create, update, delete])
}
