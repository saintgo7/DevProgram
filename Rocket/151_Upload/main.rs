#[macro_use] extern crate rocket;

use rocket::serde::{json::Json, Deserialize, Serialize};
use rocket::State;
use std::sync::Mutex;

#[derive(Serialize, Deserialize, Clone)]
#[serde(crate = "rocket::serde")]
struct Upload {
    id: u64,
    name: String,
}

type UploadList = Mutex<Vec<Upload>>;

#[get("/upload")]
fn get_all(list: &State<UploadList>) -> Json<Vec<Upload>> {
    let items = list.lock().unwrap();
    Json(items.clone())
}

#[get("/upload/<id>")]
fn get_by_id(id: u64, list: &State<UploadList>) -> Option<Json<Upload>> {
    let items = list.lock().unwrap();
    items.iter()
        .find(|item| item.id == id)
        .map(|item| Json(item.clone()))
}

#[post("/upload", data = "<item>")]
fn create(item: Json<Upload>, list: &State<UploadList>) -> Json<Upload> {
    let mut items = list.lock().unwrap();
    items.push(item.clone());
    item
}

#[put("/upload/<id>", data = "<item>")]
fn update(id: u64, item: Json<Upload>, list: &State<UploadList>) -> Option<Json<Upload>> {
    let mut items = list.lock().unwrap();
    items.iter_mut()
        .find(|i| i.id == id)
        .map(|i| {
            *i = item.clone();
            Json(i.clone())
        })
}

#[delete("/upload/<id>")]
fn delete(id: u64, list: &State<UploadList>) -> Option<()> {
    let mut items = list.lock().unwrap();
    let pos = items.iter().position(|i| i.id == id)?;
    items.remove(pos);
    Some(())
}

#[launch]
fn rocket() -> _ {
    rocket::build()
        .manage(UploadList::new(Vec::new()))
        .mount("/api", routes![get_all, get_by_id, create, update, delete])
}
