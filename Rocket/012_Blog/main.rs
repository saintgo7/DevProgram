#[macro_use] extern crate rocket;

use rocket::serde::{json::Json, Deserialize, Serialize};
use rocket::State;
use std::sync::Mutex;

#[derive(Serialize, Deserialize, Clone)]
#[serde(crate = "rocket::serde")]
struct Blog {
    id: u64,
    name: String,
}

type BlogList = Mutex<Vec<Blog>>;

#[get("/blog")]
fn get_all(list: &State<BlogList>) -> Json<Vec<Blog>> {
    let items = list.lock().unwrap();
    Json(items.clone())
}

#[get("/blog/<id>")]
fn get_by_id(id: u64, list: &State<BlogList>) -> Option<Json<Blog>> {
    let items = list.lock().unwrap();
    items.iter()
        .find(|item| item.id == id)
        .map(|item| Json(item.clone()))
}

#[post("/blog", data = "<item>")]
fn create(item: Json<Blog>, list: &State<BlogList>) -> Json<Blog> {
    let mut items = list.lock().unwrap();
    items.push(item.clone());
    item
}

#[put("/blog/<id>", data = "<item>")]
fn update(id: u64, item: Json<Blog>, list: &State<BlogList>) -> Option<Json<Blog>> {
    let mut items = list.lock().unwrap();
    items.iter_mut()
        .find(|i| i.id == id)
        .map(|i| {
            *i = item.clone();
            Json(i.clone())
        })
}

#[delete("/blog/<id>")]
fn delete(id: u64, list: &State<BlogList>) -> Option<()> {
    let mut items = list.lock().unwrap();
    let pos = items.iter().position(|i| i.id == id)?;
    items.remove(pos);
    Some(())
}

#[launch]
fn rocket() -> _ {
    rocket::build()
        .manage(BlogList::new(Vec::new()))
        .mount("/api", routes![get_all, get_by_id, create, update, delete])
}
