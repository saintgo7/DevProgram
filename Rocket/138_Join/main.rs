#[macro_use] extern crate rocket;

use rocket::serde::{json::Json, Deserialize, Serialize};
use rocket::State;
use std::sync::Mutex;

#[derive(Serialize, Deserialize, Clone)]
#[serde(crate = "rocket::serde")]
struct Join {
    id: u64,
    name: String,
}

type JoinList = Mutex<Vec<Join>>;

#[get("/join")]
fn get_all(list: &State<JoinList>) -> Json<Vec<Join>> {
    let items = list.lock().unwrap();
    Json(items.clone())
}

#[get("/join/<id>")]
fn get_by_id(id: u64, list: &State<JoinList>) -> Option<Json<Join>> {
    let items = list.lock().unwrap();
    items.iter()
        .find(|item| item.id == id)
        .map(|item| Json(item.clone()))
}

#[post("/join", data = "<item>")]
fn create(item: Json<Join>, list: &State<JoinList>) -> Json<Join> {
    let mut items = list.lock().unwrap();
    items.push(item.clone());
    item
}

#[put("/join/<id>", data = "<item>")]
fn update(id: u64, item: Json<Join>, list: &State<JoinList>) -> Option<Json<Join>> {
    let mut items = list.lock().unwrap();
    items.iter_mut()
        .find(|i| i.id == id)
        .map(|i| {
            *i = item.clone();
            Json(i.clone())
        })
}

#[delete("/join/<id>")]
fn delete(id: u64, list: &State<JoinList>) -> Option<()> {
    let mut items = list.lock().unwrap();
    let pos = items.iter().position(|i| i.id == id)?;
    items.remove(pos);
    Some(())
}

#[launch]
fn rocket() -> _ {
    rocket::build()
        .manage(JoinList::new(Vec::new()))
        .mount("/api", routes![get_all, get_by_id, create, update, delete])
}
