#[macro_use] extern crate rocket;

use rocket::serde::{json::Json, Deserialize, Serialize};
use rocket::State;
use std::sync::Mutex;

#[derive(Serialize, Deserialize, Clone)]
#[serde(crate = "rocket::serde")]
struct Import {
    id: u64,
    name: String,
}

type ImportList = Mutex<Vec<Import>>;

#[get("/import")]
fn get_all(list: &State<ImportList>) -> Json<Vec<Import>> {
    let items = list.lock().unwrap();
    Json(items.clone())
}

#[get("/import/<id>")]
fn get_by_id(id: u64, list: &State<ImportList>) -> Option<Json<Import>> {
    let items = list.lock().unwrap();
    items.iter()
        .find(|item| item.id == id)
        .map(|item| Json(item.clone()))
}

#[post("/import", data = "<item>")]
fn create(item: Json<Import>, list: &State<ImportList>) -> Json<Import> {
    let mut items = list.lock().unwrap();
    items.push(item.clone());
    item
}

#[put("/import/<id>", data = "<item>")]
fn update(id: u64, item: Json<Import>, list: &State<ImportList>) -> Option<Json<Import>> {
    let mut items = list.lock().unwrap();
    items.iter_mut()
        .find(|i| i.id == id)
        .map(|i| {
            *i = item.clone();
            Json(i.clone())
        })
}

#[delete("/import/<id>")]
fn delete(id: u64, list: &State<ImportList>) -> Option<()> {
    let mut items = list.lock().unwrap();
    let pos = items.iter().position(|i| i.id == id)?;
    items.remove(pos);
    Some(())
}

#[launch]
fn rocket() -> _ {
    rocket::build()
        .manage(ImportList::new(Vec::new()))
        .mount("/api", routes![get_all, get_by_id, create, update, delete])
}
