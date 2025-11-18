#[macro_use] extern crate rocket;

use rocket::serde::{json::Json, Deserialize, Serialize};
use rocket::State;
use std::sync::Mutex;

#[derive(Serialize, Deserialize, Clone)]
#[serde(crate = "rocket::serde")]
struct Module {
    id: u64,
    name: String,
}

type ModuleList = Mutex<Vec<Module>>;

#[get("/module")]
fn get_all(list: &State<ModuleList>) -> Json<Vec<Module>> {
    let items = list.lock().unwrap();
    Json(items.clone())
}

#[get("/module/<id>")]
fn get_by_id(id: u64, list: &State<ModuleList>) -> Option<Json<Module>> {
    let items = list.lock().unwrap();
    items.iter()
        .find(|item| item.id == id)
        .map(|item| Json(item.clone()))
}

#[post("/module", data = "<item>")]
fn create(item: Json<Module>, list: &State<ModuleList>) -> Json<Module> {
    let mut items = list.lock().unwrap();
    items.push(item.clone());
    item
}

#[put("/module/<id>", data = "<item>")]
fn update(id: u64, item: Json<Module>, list: &State<ModuleList>) -> Option<Json<Module>> {
    let mut items = list.lock().unwrap();
    items.iter_mut()
        .find(|i| i.id == id)
        .map(|i| {
            *i = item.clone();
            Json(i.clone())
        })
}

#[delete("/module/<id>")]
fn delete(id: u64, list: &State<ModuleList>) -> Option<()> {
    let mut items = list.lock().unwrap();
    let pos = items.iter().position(|i| i.id == id)?;
    items.remove(pos);
    Some(())
}

#[launch]
fn rocket() -> _ {
    rocket::build()
        .manage(ModuleList::new(Vec::new()))
        .mount("/api", routes![get_all, get_by_id, create, update, delete])
}
