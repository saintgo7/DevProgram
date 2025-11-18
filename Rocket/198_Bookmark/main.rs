#[macro_use] extern crate rocket;

use rocket::serde::{json::Json, Deserialize, Serialize};
use rocket::State;
use std::sync::Mutex;

#[derive(Serialize, Deserialize, Clone)]
#[serde(crate = "rocket::serde")]
struct Bookmark {
    id: u64,
    name: String,
}

type BookmarkList = Mutex<Vec<Bookmark>>;

#[get("/bookmark")]
fn get_all(list: &State<BookmarkList>) -> Json<Vec<Bookmark>> {
    let items = list.lock().unwrap();
    Json(items.clone())
}

#[get("/bookmark/<id>")]
fn get_by_id(id: u64, list: &State<BookmarkList>) -> Option<Json<Bookmark>> {
    let items = list.lock().unwrap();
    items.iter()
        .find(|item| item.id == id)
        .map(|item| Json(item.clone()))
}

#[post("/bookmark", data = "<item>")]
fn create(item: Json<Bookmark>, list: &State<BookmarkList>) -> Json<Bookmark> {
    let mut items = list.lock().unwrap();
    items.push(item.clone());
    item
}

#[put("/bookmark/<id>", data = "<item>")]
fn update(id: u64, item: Json<Bookmark>, list: &State<BookmarkList>) -> Option<Json<Bookmark>> {
    let mut items = list.lock().unwrap();
    items.iter_mut()
        .find(|i| i.id == id)
        .map(|i| {
            *i = item.clone();
            Json(i.clone())
        })
}

#[delete("/bookmark/<id>")]
fn delete(id: u64, list: &State<BookmarkList>) -> Option<()> {
    let mut items = list.lock().unwrap();
    let pos = items.iter().position(|i| i.id == id)?;
    items.remove(pos);
    Some(())
}

#[launch]
fn rocket() -> _ {
    rocket::build()
        .manage(BookmarkList::new(Vec::new()))
        .mount("/api", routes![get_all, get_by_id, create, update, delete])
}
