#[macro_use] extern crate rocket;

use rocket::serde::{json::Json, Deserialize, Serialize};
use rocket::State;
use std::sync::Mutex;

#[derive(Serialize, Deserialize, Clone)]
#[serde(crate = "rocket::serde")]
struct Question {
    id: u64,
    name: String,
}

type QuestionList = Mutex<Vec<Question>>;

#[get("/question")]
fn get_all(list: &State<QuestionList>) -> Json<Vec<Question>> {
    let items = list.lock().unwrap();
    Json(items.clone())
}

#[get("/question/<id>")]
fn get_by_id(id: u64, list: &State<QuestionList>) -> Option<Json<Question>> {
    let items = list.lock().unwrap();
    items.iter()
        .find(|item| item.id == id)
        .map(|item| Json(item.clone()))
}

#[post("/question", data = "<item>")]
fn create(item: Json<Question>, list: &State<QuestionList>) -> Json<Question> {
    let mut items = list.lock().unwrap();
    items.push(item.clone());
    item
}

#[put("/question/<id>", data = "<item>")]
fn update(id: u64, item: Json<Question>, list: &State<QuestionList>) -> Option<Json<Question>> {
    let mut items = list.lock().unwrap();
    items.iter_mut()
        .find(|i| i.id == id)
        .map(|i| {
            *i = item.clone();
            Json(i.clone())
        })
}

#[delete("/question/<id>")]
fn delete(id: u64, list: &State<QuestionList>) -> Option<()> {
    let mut items = list.lock().unwrap();
    let pos = items.iter().position(|i| i.id == id)?;
    items.remove(pos);
    Some(())
}

#[launch]
fn rocket() -> _ {
    rocket::build()
        .manage(QuestionList::new(Vec::new()))
        .mount("/api", routes![get_all, get_by_id, create, update, delete])
}
