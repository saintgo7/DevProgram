#[macro_use] extern crate rocket;

use rocket::serde::{json::Json, Deserialize, Serialize};
use rocket::State;
use std::sync::Mutex;

#[derive(Serialize, Deserialize, Clone)]
#[serde(crate = "rocket::serde")]
struct Post {
    id: u64,
    name: String,
}

type PostList = Mutex<Vec<Post>>;

#[get("/post")]
fn get_all(list: &State<PostList>) -> Json<Vec<Post>> {
    let items = list.lock().unwrap();
    Json(items.clone())
}

#[get("/post/<id>")]
fn get_by_id(id: u64, list: &State<PostList>) -> Option<Json<Post>> {
    let items = list.lock().unwrap();
    items.iter()
        .find(|item| item.id == id)
        .map(|item| Json(item.clone()))
}

#[post("/post", data = "<item>")]
fn create(item: Json<Post>, list: &State<PostList>) -> Json<Post> {
    let mut items = list.lock().unwrap();
    items.push(item.clone());
    item
}

#[put("/post/<id>", data = "<item>")]
fn update(id: u64, item: Json<Post>, list: &State<PostList>) -> Option<Json<Post>> {
    let mut items = list.lock().unwrap();
    items.iter_mut()
        .find(|i| i.id == id)
        .map(|i| {
            *i = item.clone();
            Json(i.clone())
        })
}

#[delete("/post/<id>")]
fn delete(id: u64, list: &State<PostList>) -> Option<()> {
    let mut items = list.lock().unwrap();
    let pos = items.iter().position(|i| i.id == id)?;
    items.remove(pos);
    Some(())
}

#[launch]
fn rocket() -> _ {
    rocket::build()
        .manage(PostList::new(Vec::new()))
        .mount("/api", routes![get_all, get_by_id, create, update, delete])
}
