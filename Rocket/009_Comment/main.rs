#[macro_use] extern crate rocket;

use rocket::serde::{json::Json, Deserialize, Serialize};
use rocket::State;
use std::sync::Mutex;

#[derive(Serialize, Deserialize, Clone)]
#[serde(crate = "rocket::serde")]
struct Comment {
    id: u64,
    name: String,
}

type CommentList = Mutex<Vec<Comment>>;

#[get("/comment")]
fn get_all(list: &State<CommentList>) -> Json<Vec<Comment>> {
    let items = list.lock().unwrap();
    Json(items.clone())
}

#[get("/comment/<id>")]
fn get_by_id(id: u64, list: &State<CommentList>) -> Option<Json<Comment>> {
    let items = list.lock().unwrap();
    items.iter()
        .find(|item| item.id == id)
        .map(|item| Json(item.clone()))
}

#[post("/comment", data = "<item>")]
fn create(item: Json<Comment>, list: &State<CommentList>) -> Json<Comment> {
    let mut items = list.lock().unwrap();
    items.push(item.clone());
    item
}

#[put("/comment/<id>", data = "<item>")]
fn update(id: u64, item: Json<Comment>, list: &State<CommentList>) -> Option<Json<Comment>> {
    let mut items = list.lock().unwrap();
    items.iter_mut()
        .find(|i| i.id == id)
        .map(|i| {
            *i = item.clone();
            Json(i.clone())
        })
}

#[delete("/comment/<id>")]
fn delete(id: u64, list: &State<CommentList>) -> Option<()> {
    let mut items = list.lock().unwrap();
    let pos = items.iter().position(|i| i.id == id)?;
    items.remove(pos);
    Some(())
}

#[launch]
fn rocket() -> _ {
    rocket::build()
        .manage(CommentList::new(Vec::new()))
        .mount("/api", routes![get_all, get_by_id, create, update, delete])
}
