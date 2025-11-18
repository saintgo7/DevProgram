#[macro_use] extern crate rocket;

use rocket::serde::{json::Json, Deserialize, Serialize};
use rocket::State;
use std::sync::Mutex;

#[derive(Serialize, Deserialize, Clone)]
#[serde(crate = "rocket::serde")]
struct Like {
    id: u64,
    name: String,
}

type LikeList = Mutex<Vec<Like>>;

#[get("/like")]
fn get_all(list: &State<LikeList>) -> Json<Vec<Like>> {
    let items = list.lock().unwrap();
    Json(items.clone())
}

#[get("/like/<id>")]
fn get_by_id(id: u64, list: &State<LikeList>) -> Option<Json<Like>> {
    let items = list.lock().unwrap();
    items.iter()
        .find(|item| item.id == id)
        .map(|item| Json(item.clone()))
}

#[post("/like", data = "<item>")]
fn create(item: Json<Like>, list: &State<LikeList>) -> Json<Like> {
    let mut items = list.lock().unwrap();
    items.push(item.clone());
    item
}

#[put("/like/<id>", data = "<item>")]
fn update(id: u64, item: Json<Like>, list: &State<LikeList>) -> Option<Json<Like>> {
    let mut items = list.lock().unwrap();
    items.iter_mut()
        .find(|i| i.id == id)
        .map(|i| {
            *i = item.clone();
            Json(i.clone())
        })
}

#[delete("/like/<id>")]
fn delete(id: u64, list: &State<LikeList>) -> Option<()> {
    let mut items = list.lock().unwrap();
    let pos = items.iter().position(|i| i.id == id)?;
    items.remove(pos);
    Some(())
}

#[launch]
fn rocket() -> _ {
    rocket::build()
        .manage(LikeList::new(Vec::new()))
        .mount("/api", routes![get_all, get_by_id, create, update, delete])
}
