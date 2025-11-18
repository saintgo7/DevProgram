#[macro_use] extern crate rocket;

use rocket::serde::{json::Json, Deserialize, Serialize};
use rocket::State;
use std::sync::Mutex;

#[derive(Serialize, Deserialize, Clone)]
#[serde(crate = "rocket::serde")]
struct Review {
    id: u64,
    name: String,
}

type ReviewList = Mutex<Vec<Review>>;

#[get("/review")]
fn get_all(list: &State<ReviewList>) -> Json<Vec<Review>> {
    let items = list.lock().unwrap();
    Json(items.clone())
}

#[get("/review/<id>")]
fn get_by_id(id: u64, list: &State<ReviewList>) -> Option<Json<Review>> {
    let items = list.lock().unwrap();
    items.iter()
        .find(|item| item.id == id)
        .map(|item| Json(item.clone()))
}

#[post("/review", data = "<item>")]
fn create(item: Json<Review>, list: &State<ReviewList>) -> Json<Review> {
    let mut items = list.lock().unwrap();
    items.push(item.clone());
    item
}

#[put("/review/<id>", data = "<item>")]
fn update(id: u64, item: Json<Review>, list: &State<ReviewList>) -> Option<Json<Review>> {
    let mut items = list.lock().unwrap();
    items.iter_mut()
        .find(|i| i.id == id)
        .map(|i| {
            *i = item.clone();
            Json(i.clone())
        })
}

#[delete("/review/<id>")]
fn delete(id: u64, list: &State<ReviewList>) -> Option<()> {
    let mut items = list.lock().unwrap();
    let pos = items.iter().position(|i| i.id == id)?;
    items.remove(pos);
    Some(())
}

#[launch]
fn rocket() -> _ {
    rocket::build()
        .manage(ReviewList::new(Vec::new()))
        .mount("/api", routes![get_all, get_by_id, create, update, delete])
}
