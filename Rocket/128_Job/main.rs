#[macro_use] extern crate rocket;

use rocket::serde::{json::Json, Deserialize, Serialize};
use rocket::State;
use std::sync::Mutex;

#[derive(Serialize, Deserialize, Clone)]
#[serde(crate = "rocket::serde")]
struct Job {
    id: u64,
    name: String,
}

type JobList = Mutex<Vec<Job>>;

#[get("/job")]
fn get_all(list: &State<JobList>) -> Json<Vec<Job>> {
    let items = list.lock().unwrap();
    Json(items.clone())
}

#[get("/job/<id>")]
fn get_by_id(id: u64, list: &State<JobList>) -> Option<Json<Job>> {
    let items = list.lock().unwrap();
    items.iter()
        .find(|item| item.id == id)
        .map(|item| Json(item.clone()))
}

#[post("/job", data = "<item>")]
fn create(item: Json<Job>, list: &State<JobList>) -> Json<Job> {
    let mut items = list.lock().unwrap();
    items.push(item.clone());
    item
}

#[put("/job/<id>", data = "<item>")]
fn update(id: u64, item: Json<Job>, list: &State<JobList>) -> Option<Json<Job>> {
    let mut items = list.lock().unwrap();
    items.iter_mut()
        .find(|i| i.id == id)
        .map(|i| {
            *i = item.clone();
            Json(i.clone())
        })
}

#[delete("/job/<id>")]
fn delete(id: u64, list: &State<JobList>) -> Option<()> {
    let mut items = list.lock().unwrap();
    let pos = items.iter().position(|i| i.id == id)?;
    items.remove(pos);
    Some(())
}

#[launch]
fn rocket() -> _ {
    rocket::build()
        .manage(JobList::new(Vec::new()))
        .mount("/api", routes![get_all, get_by_id, create, update, delete])
}
