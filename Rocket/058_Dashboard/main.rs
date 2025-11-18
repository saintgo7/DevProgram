#[macro_use] extern crate rocket;

use rocket::serde::{json::Json, Deserialize, Serialize};
use rocket::State;
use std::sync::Mutex;

#[derive(Serialize, Deserialize, Clone)]
#[serde(crate = "rocket::serde")]
struct Dashboard {
    id: u64,
    name: String,
}

type DashboardList = Mutex<Vec<Dashboard>>;

#[get("/dashboard")]
fn get_all(list: &State<DashboardList>) -> Json<Vec<Dashboard>> {
    let items = list.lock().unwrap();
    Json(items.clone())
}

#[get("/dashboard/<id>")]
fn get_by_id(id: u64, list: &State<DashboardList>) -> Option<Json<Dashboard>> {
    let items = list.lock().unwrap();
    items.iter()
        .find(|item| item.id == id)
        .map(|item| Json(item.clone()))
}

#[post("/dashboard", data = "<item>")]
fn create(item: Json<Dashboard>, list: &State<DashboardList>) -> Json<Dashboard> {
    let mut items = list.lock().unwrap();
    items.push(item.clone());
    item
}

#[put("/dashboard/<id>", data = "<item>")]
fn update(id: u64, item: Json<Dashboard>, list: &State<DashboardList>) -> Option<Json<Dashboard>> {
    let mut items = list.lock().unwrap();
    items.iter_mut()
        .find(|i| i.id == id)
        .map(|i| {
            *i = item.clone();
            Json(i.clone())
        })
}

#[delete("/dashboard/<id>")]
fn delete(id: u64, list: &State<DashboardList>) -> Option<()> {
    let mut items = list.lock().unwrap();
    let pos = items.iter().position(|i| i.id == id)?;
    items.remove(pos);
    Some(())
}

#[launch]
fn rocket() -> _ {
    rocket::build()
        .manage(DashboardList::new(Vec::new()))
        .mount("/api", routes![get_all, get_by_id, create, update, delete])
}
