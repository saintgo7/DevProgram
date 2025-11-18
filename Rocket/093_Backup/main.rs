#[macro_use] extern crate rocket;

use rocket::serde::{json::Json, Deserialize, Serialize};
use rocket::State;
use std::sync::Mutex;

#[derive(Serialize, Deserialize, Clone)]
#[serde(crate = "rocket::serde")]
struct Backup {
    id: u64,
    name: String,
}

type BackupList = Mutex<Vec<Backup>>;

#[get("/backup")]
fn get_all(list: &State<BackupList>) -> Json<Vec<Backup>> {
    let items = list.lock().unwrap();
    Json(items.clone())
}

#[get("/backup/<id>")]
fn get_by_id(id: u64, list: &State<BackupList>) -> Option<Json<Backup>> {
    let items = list.lock().unwrap();
    items.iter()
        .find(|item| item.id == id)
        .map(|item| Json(item.clone()))
}

#[post("/backup", data = "<item>")]
fn create(item: Json<Backup>, list: &State<BackupList>) -> Json<Backup> {
    let mut items = list.lock().unwrap();
    items.push(item.clone());
    item
}

#[put("/backup/<id>", data = "<item>")]
fn update(id: u64, item: Json<Backup>, list: &State<BackupList>) -> Option<Json<Backup>> {
    let mut items = list.lock().unwrap();
    items.iter_mut()
        .find(|i| i.id == id)
        .map(|i| {
            *i = item.clone();
            Json(i.clone())
        })
}

#[delete("/backup/<id>")]
fn delete(id: u64, list: &State<BackupList>) -> Option<()> {
    let mut items = list.lock().unwrap();
    let pos = items.iter().position(|i| i.id == id)?;
    items.remove(pos);
    Some(())
}

#[launch]
fn rocket() -> _ {
    rocket::build()
        .manage(BackupList::new(Vec::new()))
        .mount("/api", routes![get_all, get_by_id, create, update, delete])
}
