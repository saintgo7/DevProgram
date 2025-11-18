#[macro_use] extern crate rocket;

use rocket::serde::{json::Json, Deserialize, Serialize};
use rocket::State;
use std::sync::Mutex;

#[derive(Serialize, Deserialize, Clone)]
#[serde(crate = "rocket::serde")]
struct Settings {
    id: u64,
    name: String,
}

type SettingsList = Mutex<Vec<Settings>>;

#[get("/settings")]
fn get_all(list: &State<SettingsList>) -> Json<Vec<Settings>> {
    let items = list.lock().unwrap();
    Json(items.clone())
}

#[get("/settings/<id>")]
fn get_by_id(id: u64, list: &State<SettingsList>) -> Option<Json<Settings>> {
    let items = list.lock().unwrap();
    items.iter()
        .find(|item| item.id == id)
        .map(|item| Json(item.clone()))
}

#[post("/settings", data = "<item>")]
fn create(item: Json<Settings>, list: &State<SettingsList>) -> Json<Settings> {
    let mut items = list.lock().unwrap();
    items.push(item.clone());
    item
}

#[put("/settings/<id>", data = "<item>")]
fn update(id: u64, item: Json<Settings>, list: &State<SettingsList>) -> Option<Json<Settings>> {
    let mut items = list.lock().unwrap();
    items.iter_mut()
        .find(|i| i.id == id)
        .map(|i| {
            *i = item.clone();
            Json(i.clone())
        })
}

#[delete("/settings/<id>")]
fn delete(id: u64, list: &State<SettingsList>) -> Option<()> {
    let mut items = list.lock().unwrap();
    let pos = items.iter().position(|i| i.id == id)?;
    items.remove(pos);
    Some(())
}

#[launch]
fn rocket() -> _ {
    rocket::build()
        .manage(SettingsList::new(Vec::new()))
        .mount("/api", routes![get_all, get_by_id, create, update, delete])
}
