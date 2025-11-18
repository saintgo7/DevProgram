#[macro_use] extern crate rocket;

use rocket::serde::{json::Json, Deserialize, Serialize};
use rocket::State;
use std::sync::Mutex;

#[derive(Serialize, Deserialize, Clone)]
#[serde(crate = "rocket::serde")]
struct Vote {
    id: u64,
    name: String,
}

type VoteList = Mutex<Vec<Vote>>;

#[get("/vote")]
fn get_all(list: &State<VoteList>) -> Json<Vec<Vote>> {
    let items = list.lock().unwrap();
    Json(items.clone())
}

#[get("/vote/<id>")]
fn get_by_id(id: u64, list: &State<VoteList>) -> Option<Json<Vote>> {
    let items = list.lock().unwrap();
    items.iter()
        .find(|item| item.id == id)
        .map(|item| Json(item.clone()))
}

#[post("/vote", data = "<item>")]
fn create(item: Json<Vote>, list: &State<VoteList>) -> Json<Vote> {
    let mut items = list.lock().unwrap();
    items.push(item.clone());
    item
}

#[put("/vote/<id>", data = "<item>")]
fn update(id: u64, item: Json<Vote>, list: &State<VoteList>) -> Option<Json<Vote>> {
    let mut items = list.lock().unwrap();
    items.iter_mut()
        .find(|i| i.id == id)
        .map(|i| {
            *i = item.clone();
            Json(i.clone())
        })
}

#[delete("/vote/<id>")]
fn delete(id: u64, list: &State<VoteList>) -> Option<()> {
    let mut items = list.lock().unwrap();
    let pos = items.iter().position(|i| i.id == id)?;
    items.remove(pos);
    Some(())
}

#[launch]
fn rocket() -> _ {
    rocket::build()
        .manage(VoteList::new(Vec::new()))
        .mount("/api", routes![get_all, get_by_id, create, update, delete])
}
