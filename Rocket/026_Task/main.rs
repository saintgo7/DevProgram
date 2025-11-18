#[macro_use] extern crate rocket;

use rocket::serde::{json::Json, Deserialize, Serialize};
use rocket::State;
use std::sync::Mutex;

#[derive(Serialize, Deserialize, Clone)]
#[serde(crate = "rocket::serde")]
struct Task {
    id: u64,
    name: String,
}

type TaskList = Mutex<Vec<Task>>;

#[get("/task")]
fn get_all(list: &State<TaskList>) -> Json<Vec<Task>> {
    let items = list.lock().unwrap();
    Json(items.clone())
}

#[get("/task/<id>")]
fn get_by_id(id: u64, list: &State<TaskList>) -> Option<Json<Task>> {
    let items = list.lock().unwrap();
    items.iter()
        .find(|item| item.id == id)
        .map(|item| Json(item.clone()))
}

#[post("/task", data = "<item>")]
fn create(item: Json<Task>, list: &State<TaskList>) -> Json<Task> {
    let mut items = list.lock().unwrap();
    items.push(item.clone());
    item
}

#[put("/task/<id>", data = "<item>")]
fn update(id: u64, item: Json<Task>, list: &State<TaskList>) -> Option<Json<Task>> {
    let mut items = list.lock().unwrap();
    items.iter_mut()
        .find(|i| i.id == id)
        .map(|i| {
            *i = item.clone();
            Json(i.clone())
        })
}

#[delete("/task/<id>")]
fn delete(id: u64, list: &State<TaskList>) -> Option<()> {
    let mut items = list.lock().unwrap();
    let pos = items.iter().position(|i| i.id == id)?;
    items.remove(pos);
    Some(())
}

#[launch]
fn rocket() -> _ {
    rocket::build()
        .manage(TaskList::new(Vec::new()))
        .mount("/api", routes![get_all, get_by_id, create, update, delete])
}
