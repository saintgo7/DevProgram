#[macro_use] extern crate rocket;

use rocket::serde::{json::Json, Deserialize, Serialize};
use rocket::State;
use std::sync::Mutex;

#[derive(Serialize, Deserialize, Clone)]
#[serde(crate = "rocket::serde")]
struct Plugin {
    id: u64,
    name: String,
}

type PluginList = Mutex<Vec<Plugin>>;

#[get("/plugin")]
fn get_all(list: &State<PluginList>) -> Json<Vec<Plugin>> {
    let items = list.lock().unwrap();
    Json(items.clone())
}

#[get("/plugin/<id>")]
fn get_by_id(id: u64, list: &State<PluginList>) -> Option<Json<Plugin>> {
    let items = list.lock().unwrap();
    items.iter()
        .find(|item| item.id == id)
        .map(|item| Json(item.clone()))
}

#[post("/plugin", data = "<item>")]
fn create(item: Json<Plugin>, list: &State<PluginList>) -> Json<Plugin> {
    let mut items = list.lock().unwrap();
    items.push(item.clone());
    item
}

#[put("/plugin/<id>", data = "<item>")]
fn update(id: u64, item: Json<Plugin>, list: &State<PluginList>) -> Option<Json<Plugin>> {
    let mut items = list.lock().unwrap();
    items.iter_mut()
        .find(|i| i.id == id)
        .map(|i| {
            *i = item.clone();
            Json(i.clone())
        })
}

#[delete("/plugin/<id>")]
fn delete(id: u64, list: &State<PluginList>) -> Option<()> {
    let mut items = list.lock().unwrap();
    let pos = items.iter().position(|i| i.id == id)?;
    items.remove(pos);
    Some(())
}

#[launch]
fn rocket() -> _ {
    rocket::build()
        .manage(PluginList::new(Vec::new()))
        .mount("/api", routes![get_all, get_by_id, create, update, delete])
}
