#[macro_use] extern crate rocket;

use rocket::serde::{json::Json, Deserialize, Serialize};
use rocket::State;
use std::sync::Mutex;

#[derive(Serialize, Deserialize, Clone)]
#[serde(crate = "rocket::serde")]
struct Tag {
    id: u64,
    name: String,
}

type TagList = Mutex<Vec<Tag>>;

#[get("/tag")]
fn get_all(list: &State<TagList>) -> Json<Vec<Tag>> {
    let items = list.lock().unwrap();
    Json(items.clone())
}

#[get("/tag/<id>")]
fn get_by_id(id: u64, list: &State<TagList>) -> Option<Json<Tag>> {
    let items = list.lock().unwrap();
    items.iter()
        .find(|item| item.id == id)
        .map(|item| Json(item.clone()))
}

#[post("/tag", data = "<item>")]
fn create(item: Json<Tag>, list: &State<TagList>) -> Json<Tag> {
    let mut items = list.lock().unwrap();
    items.push(item.clone());
    item
}

#[put("/tag/<id>", data = "<item>")]
fn update(id: u64, item: Json<Tag>, list: &State<TagList>) -> Option<Json<Tag>> {
    let mut items = list.lock().unwrap();
    items.iter_mut()
        .find(|i| i.id == id)
        .map(|i| {
            *i = item.clone();
            Json(i.clone())
        })
}

#[delete("/tag/<id>")]
fn delete(id: u64, list: &State<TagList>) -> Option<()> {
    let mut items = list.lock().unwrap();
    let pos = items.iter().position(|i| i.id == id)?;
    items.remove(pos);
    Some(())
}

#[launch]
fn rocket() -> _ {
    rocket::build()
        .manage(TagList::new(Vec::new()))
        .mount("/api", routes![get_all, get_by_id, create, update, delete])
}
