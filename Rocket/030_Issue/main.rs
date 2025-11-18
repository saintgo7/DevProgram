#[macro_use] extern crate rocket;

use rocket::serde::{json::Json, Deserialize, Serialize};
use rocket::State;
use std::sync::Mutex;

#[derive(Serialize, Deserialize, Clone)]
#[serde(crate = "rocket::serde")]
struct Issue {
    id: u64,
    name: String,
}

type IssueList = Mutex<Vec<Issue>>;

#[get("/issue")]
fn get_all(list: &State<IssueList>) -> Json<Vec<Issue>> {
    let items = list.lock().unwrap();
    Json(items.clone())
}

#[get("/issue/<id>")]
fn get_by_id(id: u64, list: &State<IssueList>) -> Option<Json<Issue>> {
    let items = list.lock().unwrap();
    items.iter()
        .find(|item| item.id == id)
        .map(|item| Json(item.clone()))
}

#[post("/issue", data = "<item>")]
fn create(item: Json<Issue>, list: &State<IssueList>) -> Json<Issue> {
    let mut items = list.lock().unwrap();
    items.push(item.clone());
    item
}

#[put("/issue/<id>", data = "<item>")]
fn update(id: u64, item: Json<Issue>, list: &State<IssueList>) -> Option<Json<Issue>> {
    let mut items = list.lock().unwrap();
    items.iter_mut()
        .find(|i| i.id == id)
        .map(|i| {
            *i = item.clone();
            Json(i.clone())
        })
}

#[delete("/issue/<id>")]
fn delete(id: u64, list: &State<IssueList>) -> Option<()> {
    let mut items = list.lock().unwrap();
    let pos = items.iter().position(|i| i.id == id)?;
    items.remove(pos);
    Some(())
}

#[launch]
fn rocket() -> _ {
    rocket::build()
        .manage(IssueList::new(Vec::new()))
        .mount("/api", routes![get_all, get_by_id, create, update, delete])
}
