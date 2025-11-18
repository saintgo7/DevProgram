#[macro_use] extern crate rocket;

use rocket::serde::{json::Json, Deserialize, Serialize};
use rocket::State;
use std::sync::Mutex;

#[derive(Serialize, Deserialize, Clone)]
#[serde(crate = "rocket::serde")]
struct Answer {
    id: u64,
    name: String,
}

type AnswerList = Mutex<Vec<Answer>>;

#[get("/answer")]
fn get_all(list: &State<AnswerList>) -> Json<Vec<Answer>> {
    let items = list.lock().unwrap();
    Json(items.clone())
}

#[get("/answer/<id>")]
fn get_by_id(id: u64, list: &State<AnswerList>) -> Option<Json<Answer>> {
    let items = list.lock().unwrap();
    items.iter()
        .find(|item| item.id == id)
        .map(|item| Json(item.clone()))
}

#[post("/answer", data = "<item>")]
fn create(item: Json<Answer>, list: &State<AnswerList>) -> Json<Answer> {
    let mut items = list.lock().unwrap();
    items.push(item.clone());
    item
}

#[put("/answer/<id>", data = "<item>")]
fn update(id: u64, item: Json<Answer>, list: &State<AnswerList>) -> Option<Json<Answer>> {
    let mut items = list.lock().unwrap();
    items.iter_mut()
        .find(|i| i.id == id)
        .map(|i| {
            *i = item.clone();
            Json(i.clone())
        })
}

#[delete("/answer/<id>")]
fn delete(id: u64, list: &State<AnswerList>) -> Option<()> {
    let mut items = list.lock().unwrap();
    let pos = items.iter().position(|i| i.id == id)?;
    items.remove(pos);
    Some(())
}

#[launch]
fn rocket() -> _ {
    rocket::build()
        .manage(AnswerList::new(Vec::new()))
        .mount("/api", routes![get_all, get_by_id, create, update, delete])
}
