#[macro_use] extern crate rocket;

use rocket::serde::{json::Json, Deserialize, Serialize};
use rocket::State;
use std::sync::Mutex;

#[derive(Serialize, Deserialize, Clone)]
#[serde(crate = "rocket::serde")]
struct Configuration {
    id: u64,
    name: String,
}

type ConfigurationList = Mutex<Vec<Configuration>>;

#[get("/configuration")]
fn get_all(list: &State<ConfigurationList>) -> Json<Vec<Configuration>> {
    let items = list.lock().unwrap();
    Json(items.clone())
}

#[get("/configuration/<id>")]
fn get_by_id(id: u64, list: &State<ConfigurationList>) -> Option<Json<Configuration>> {
    let items = list.lock().unwrap();
    items.iter()
        .find(|item| item.id == id)
        .map(|item| Json(item.clone()))
}

#[post("/configuration", data = "<item>")]
fn create(item: Json<Configuration>, list: &State<ConfigurationList>) -> Json<Configuration> {
    let mut items = list.lock().unwrap();
    items.push(item.clone());
    item
}

#[put("/configuration/<id>", data = "<item>")]
fn update(id: u64, item: Json<Configuration>, list: &State<ConfigurationList>) -> Option<Json<Configuration>> {
    let mut items = list.lock().unwrap();
    items.iter_mut()
        .find(|i| i.id == id)
        .map(|i| {
            *i = item.clone();
            Json(i.clone())
        })
}

#[delete("/configuration/<id>")]
fn delete(id: u64, list: &State<ConfigurationList>) -> Option<()> {
    let mut items = list.lock().unwrap();
    let pos = items.iter().position(|i| i.id == id)?;
    items.remove(pos);
    Some(())
}

#[launch]
fn rocket() -> _ {
    rocket::build()
        .manage(ConfigurationList::new(Vec::new()))
        .mount("/api", routes![get_all, get_by_id, create, update, delete])
}
