#[macro_use] extern crate rocket;

use rocket::serde::{json::Json, Deserialize, Serialize};
use rocket::State;
use std::sync::Mutex;

#[derive(Serialize, Deserialize, Clone)]
#[serde(crate = "rocket::serde")]
struct Album {
    id: u64,
    name: String,
}

type AlbumList = Mutex<Vec<Album>>;

#[get("/album")]
fn get_all(list: &State<AlbumList>) -> Json<Vec<Album>> {
    let items = list.lock().unwrap();
    Json(items.clone())
}

#[get("/album/<id>")]
fn get_by_id(id: u64, list: &State<AlbumList>) -> Option<Json<Album>> {
    let items = list.lock().unwrap();
    items.iter()
        .find(|item| item.id == id)
        .map(|item| Json(item.clone()))
}

#[post("/album", data = "<item>")]
fn create(item: Json<Album>, list: &State<AlbumList>) -> Json<Album> {
    let mut items = list.lock().unwrap();
    items.push(item.clone());
    item
}

#[put("/album/<id>", data = "<item>")]
fn update(id: u64, item: Json<Album>, list: &State<AlbumList>) -> Option<Json<Album>> {
    let mut items = list.lock().unwrap();
    items.iter_mut()
        .find(|i| i.id == id)
        .map(|i| {
            *i = item.clone();
            Json(i.clone())
        })
}

#[delete("/album/<id>")]
fn delete(id: u64, list: &State<AlbumList>) -> Option<()> {
    let mut items = list.lock().unwrap();
    let pos = items.iter().position(|i| i.id == id)?;
    items.remove(pos);
    Some(())
}

#[launch]
fn rocket() -> _ {
    rocket::build()
        .manage(AlbumList::new(Vec::new()))
        .mount("/api", routes![get_all, get_by_id, create, update, delete])
}
