#[macro_use] extern crate rocket;

use rocket::serde::{json::Json, Deserialize, Serialize};
use rocket::State;
use std::sync::Mutex;

#[derive(Serialize, Deserialize, Clone)]
#[serde(crate = "rocket::serde")]
struct Download {
    id: u64,
    name: String,
}

type DownloadList = Mutex<Vec<Download>>;

#[get("/download")]
fn get_all(list: &State<DownloadList>) -> Json<Vec<Download>> {
    let items = list.lock().unwrap();
    Json(items.clone())
}

#[get("/download/<id>")]
fn get_by_id(id: u64, list: &State<DownloadList>) -> Option<Json<Download>> {
    let items = list.lock().unwrap();
    items.iter()
        .find(|item| item.id == id)
        .map(|item| Json(item.clone()))
}

#[post("/download", data = "<item>")]
fn create(item: Json<Download>, list: &State<DownloadList>) -> Json<Download> {
    let mut items = list.lock().unwrap();
    items.push(item.clone());
    item
}

#[put("/download/<id>", data = "<item>")]
fn update(id: u64, item: Json<Download>, list: &State<DownloadList>) -> Option<Json<Download>> {
    let mut items = list.lock().unwrap();
    items.iter_mut()
        .find(|i| i.id == id)
        .map(|i| {
            *i = item.clone();
            Json(i.clone())
        })
}

#[delete("/download/<id>")]
fn delete(id: u64, list: &State<DownloadList>) -> Option<()> {
    let mut items = list.lock().unwrap();
    let pos = items.iter().position(|i| i.id == id)?;
    items.remove(pos);
    Some(())
}

#[launch]
fn rocket() -> _ {
    rocket::build()
        .manage(DownloadList::new(Vec::new()))
        .mount("/api", routes![get_all, get_by_id, create, update, delete])
}
