#[macro_use] extern crate rocket;

use rocket::serde::{json::Json, Deserialize, Serialize};
use rocket::State;
use std::sync::Mutex;

#[derive(Serialize, Deserialize, Clone)]
#[serde(crate = "rocket::serde")]
struct Project {
    id: u64,
    name: String,
}

type ProjectList = Mutex<Vec<Project>>;

#[get("/project")]
fn get_all(list: &State<ProjectList>) -> Json<Vec<Project>> {
    let items = list.lock().unwrap();
    Json(items.clone())
}

#[get("/project/<id>")]
fn get_by_id(id: u64, list: &State<ProjectList>) -> Option<Json<Project>> {
    let items = list.lock().unwrap();
    items.iter()
        .find(|item| item.id == id)
        .map(|item| Json(item.clone()))
}

#[post("/project", data = "<item>")]
fn create(item: Json<Project>, list: &State<ProjectList>) -> Json<Project> {
    let mut items = list.lock().unwrap();
    items.push(item.clone());
    item
}

#[put("/project/<id>", data = "<item>")]
fn update(id: u64, item: Json<Project>, list: &State<ProjectList>) -> Option<Json<Project>> {
    let mut items = list.lock().unwrap();
    items.iter_mut()
        .find(|i| i.id == id)
        .map(|i| {
            *i = item.clone();
            Json(i.clone())
        })
}

#[delete("/project/<id>")]
fn delete(id: u64, list: &State<ProjectList>) -> Option<()> {
    let mut items = list.lock().unwrap();
    let pos = items.iter().position(|i| i.id == id)?;
    items.remove(pos);
    Some(())
}

#[launch]
fn rocket() -> _ {
    rocket::build()
        .manage(ProjectList::new(Vec::new()))
        .mount("/api", routes![get_all, get_by_id, create, update, delete])
}
