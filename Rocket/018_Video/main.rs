#[macro_use] extern crate rocket;

use rocket::serde::{json::Json, Deserialize, Serialize};
use rocket::State;
use std::sync::Mutex;

#[derive(Serialize, Deserialize, Clone)]
#[serde(crate = "rocket::serde")]
struct Video {
    id: u64,
    name: String,
}

type VideoList = Mutex<Vec<Video>>;

#[get("/video")]
fn get_all(list: &State<VideoList>) -> Json<Vec<Video>> {
    let items = list.lock().unwrap();
    Json(items.clone())
}

#[get("/video/<id>")]
fn get_by_id(id: u64, list: &State<VideoList>) -> Option<Json<Video>> {
    let items = list.lock().unwrap();
    items.iter()
        .find(|item| item.id == id)
        .map(|item| Json(item.clone()))
}

#[post("/video", data = "<item>")]
fn create(item: Json<Video>, list: &State<VideoList>) -> Json<Video> {
    let mut items = list.lock().unwrap();
    items.push(item.clone());
    item
}

#[put("/video/<id>", data = "<item>")]
fn update(id: u64, item: Json<Video>, list: &State<VideoList>) -> Option<Json<Video>> {
    let mut items = list.lock().unwrap();
    items.iter_mut()
        .find(|i| i.id == id)
        .map(|i| {
            *i = item.clone();
            Json(i.clone())
        })
}

#[delete("/video/<id>")]
fn delete(id: u64, list: &State<VideoList>) -> Option<()> {
    let mut items = list.lock().unwrap();
    let pos = items.iter().position(|i| i.id == id)?;
    items.remove(pos);
    Some(())
}

#[launch]
fn rocket() -> _ {
    rocket::build()
        .manage(VideoList::new(Vec::new()))
        .mount("/api", routes![get_all, get_by_id, create, update, delete])
}
