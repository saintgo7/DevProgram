#[macro_use] extern crate rocket;

use rocket::serde::{json::Json, Deserialize, Serialize};
use rocket::State;
use std::sync::Mutex;

#[derive(Serialize, Deserialize, Clone)]
#[serde(crate = "rocket::serde")]
struct Favorite {
    id: u64,
    name: String,
}

type FavoriteList = Mutex<Vec<Favorite>>;

#[get("/favorite")]
fn get_all(list: &State<FavoriteList>) -> Json<Vec<Favorite>> {
    let items = list.lock().unwrap();
    Json(items.clone())
}

#[get("/favorite/<id>")]
fn get_by_id(id: u64, list: &State<FavoriteList>) -> Option<Json<Favorite>> {
    let items = list.lock().unwrap();
    items.iter()
        .find(|item| item.id == id)
        .map(|item| Json(item.clone()))
}

#[post("/favorite", data = "<item>")]
fn create(item: Json<Favorite>, list: &State<FavoriteList>) -> Json<Favorite> {
    let mut items = list.lock().unwrap();
    items.push(item.clone());
    item
}

#[put("/favorite/<id>", data = "<item>")]
fn update(id: u64, item: Json<Favorite>, list: &State<FavoriteList>) -> Option<Json<Favorite>> {
    let mut items = list.lock().unwrap();
    items.iter_mut()
        .find(|i| i.id == id)
        .map(|i| {
            *i = item.clone();
            Json(i.clone())
        })
}

#[delete("/favorite/<id>")]
fn delete(id: u64, list: &State<FavoriteList>) -> Option<()> {
    let mut items = list.lock().unwrap();
    let pos = items.iter().position(|i| i.id == id)?;
    items.remove(pos);
    Some(())
}

#[launch]
fn rocket() -> _ {
    rocket::build()
        .manage(FavoriteList::new(Vec::new()))
        .mount("/api", routes![get_all, get_by_id, create, update, delete])
}
