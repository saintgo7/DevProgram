#[macro_use] extern crate rocket;

use rocket::serde::{json::Json, Deserialize, Serialize};
use rocket::State;
use std::sync::Mutex;

#[derive(Serialize, Deserialize, Clone)]
#[serde(crate = "rocket::serde")]
struct Poll {
    id: u64,
    name: String,
}

type PollList = Mutex<Vec<Poll>>;

#[get("/poll")]
fn get_all(list: &State<PollList>) -> Json<Vec<Poll>> {
    let items = list.lock().unwrap();
    Json(items.clone())
}

#[get("/poll/<id>")]
fn get_by_id(id: u64, list: &State<PollList>) -> Option<Json<Poll>> {
    let items = list.lock().unwrap();
    items.iter()
        .find(|item| item.id == id)
        .map(|item| Json(item.clone()))
}

#[post("/poll", data = "<item>")]
fn create(item: Json<Poll>, list: &State<PollList>) -> Json<Poll> {
    let mut items = list.lock().unwrap();
    items.push(item.clone());
    item
}

#[put("/poll/<id>", data = "<item>")]
fn update(id: u64, item: Json<Poll>, list: &State<PollList>) -> Option<Json<Poll>> {
    let mut items = list.lock().unwrap();
    items.iter_mut()
        .find(|i| i.id == id)
        .map(|i| {
            *i = item.clone();
            Json(i.clone())
        })
}

#[delete("/poll/<id>")]
fn delete(id: u64, list: &State<PollList>) -> Option<()> {
    let mut items = list.lock().unwrap();
    let pos = items.iter().position(|i| i.id == id)?;
    items.remove(pos);
    Some(())
}

#[launch]
fn rocket() -> _ {
    rocket::build()
        .manage(PollList::new(Vec::new()))
        .mount("/api", routes![get_all, get_by_id, create, update, delete])
}
