#[macro_use] extern crate rocket;

use rocket::serde::{json::Json, Deserialize, Serialize};
use rocket::State;
use std::sync::Mutex;

#[derive(Serialize, Deserialize, Clone)]
#[serde(crate = "rocket::serde")]
struct Export {
    id: u64,
    name: String,
}

type ExportList = Mutex<Vec<Export>>;

#[get("/export")]
fn get_all(list: &State<ExportList>) -> Json<Vec<Export>> {
    let items = list.lock().unwrap();
    Json(items.clone())
}

#[get("/export/<id>")]
fn get_by_id(id: u64, list: &State<ExportList>) -> Option<Json<Export>> {
    let items = list.lock().unwrap();
    items.iter()
        .find(|item| item.id == id)
        .map(|item| Json(item.clone()))
}

#[post("/export", data = "<item>")]
fn create(item: Json<Export>, list: &State<ExportList>) -> Json<Export> {
    let mut items = list.lock().unwrap();
    items.push(item.clone());
    item
}

#[put("/export/<id>", data = "<item>")]
fn update(id: u64, item: Json<Export>, list: &State<ExportList>) -> Option<Json<Export>> {
    let mut items = list.lock().unwrap();
    items.iter_mut()
        .find(|i| i.id == id)
        .map(|i| {
            *i = item.clone();
            Json(i.clone())
        })
}

#[delete("/export/<id>")]
fn delete(id: u64, list: &State<ExportList>) -> Option<()> {
    let mut items = list.lock().unwrap();
    let pos = items.iter().position(|i| i.id == id)?;
    items.remove(pos);
    Some(())
}

#[launch]
fn rocket() -> _ {
    rocket::build()
        .manage(ExportList::new(Vec::new()))
        .mount("/api", routes![get_all, get_by_id, create, update, delete])
}
