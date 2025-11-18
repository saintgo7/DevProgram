#[macro_use] extern crate rocket;

use rocket::serde::{json::Json, Deserialize, Serialize};
use rocket::State;
use std::sync::Mutex;

#[derive(Serialize, Deserialize, Clone)]
#[serde(crate = "rocket::serde")]
struct Preference {
    id: u64,
    name: String,
}

type PreferenceList = Mutex<Vec<Preference>>;

#[get("/preference")]
fn get_all(list: &State<PreferenceList>) -> Json<Vec<Preference>> {
    let items = list.lock().unwrap();
    Json(items.clone())
}

#[get("/preference/<id>")]
fn get_by_id(id: u64, list: &State<PreferenceList>) -> Option<Json<Preference>> {
    let items = list.lock().unwrap();
    items.iter()
        .find(|item| item.id == id)
        .map(|item| Json(item.clone()))
}

#[post("/preference", data = "<item>")]
fn create(item: Json<Preference>, list: &State<PreferenceList>) -> Json<Preference> {
    let mut items = list.lock().unwrap();
    items.push(item.clone());
    item
}

#[put("/preference/<id>", data = "<item>")]
fn update(id: u64, item: Json<Preference>, list: &State<PreferenceList>) -> Option<Json<Preference>> {
    let mut items = list.lock().unwrap();
    items.iter_mut()
        .find(|i| i.id == id)
        .map(|i| {
            *i = item.clone();
            Json(i.clone())
        })
}

#[delete("/preference/<id>")]
fn delete(id: u64, list: &State<PreferenceList>) -> Option<()> {
    let mut items = list.lock().unwrap();
    let pos = items.iter().position(|i| i.id == id)?;
    items.remove(pos);
    Some(())
}

#[launch]
fn rocket() -> _ {
    rocket::build()
        .manage(PreferenceList::new(Vec::new()))
        .mount("/api", routes![get_all, get_by_id, create, update, delete])
}
