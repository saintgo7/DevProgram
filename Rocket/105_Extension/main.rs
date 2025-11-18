#[macro_use] extern crate rocket;

use rocket::serde::{json::Json, Deserialize, Serialize};
use rocket::State;
use std::sync::Mutex;

#[derive(Serialize, Deserialize, Clone)]
#[serde(crate = "rocket::serde")]
struct Extension {
    id: u64,
    name: String,
}

type ExtensionList = Mutex<Vec<Extension>>;

#[get("/extension")]
fn get_all(list: &State<ExtensionList>) -> Json<Vec<Extension>> {
    let items = list.lock().unwrap();
    Json(items.clone())
}

#[get("/extension/<id>")]
fn get_by_id(id: u64, list: &State<ExtensionList>) -> Option<Json<Extension>> {
    let items = list.lock().unwrap();
    items.iter()
        .find(|item| item.id == id)
        .map(|item| Json(item.clone()))
}

#[post("/extension", data = "<item>")]
fn create(item: Json<Extension>, list: &State<ExtensionList>) -> Json<Extension> {
    let mut items = list.lock().unwrap();
    items.push(item.clone());
    item
}

#[put("/extension/<id>", data = "<item>")]
fn update(id: u64, item: Json<Extension>, list: &State<ExtensionList>) -> Option<Json<Extension>> {
    let mut items = list.lock().unwrap();
    items.iter_mut()
        .find(|i| i.id == id)
        .map(|i| {
            *i = item.clone();
            Json(i.clone())
        })
}

#[delete("/extension/<id>")]
fn delete(id: u64, list: &State<ExtensionList>) -> Option<()> {
    let mut items = list.lock().unwrap();
    let pos = items.iter().position(|i| i.id == id)?;
    items.remove(pos);
    Some(())
}

#[launch]
fn rocket() -> _ {
    rocket::build()
        .manage(ExtensionList::new(Vec::new()))
        .mount("/api", routes![get_all, get_by_id, create, update, delete])
}
