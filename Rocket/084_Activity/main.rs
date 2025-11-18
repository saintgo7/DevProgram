#[macro_use] extern crate rocket;

use rocket::serde::{json::Json, Deserialize, Serialize};
use rocket::State;
use std::sync::Mutex;

#[derive(Serialize, Deserialize, Clone)]
#[serde(crate = "rocket::serde")]
struct Activity {
    id: u64,
    name: String,
}

type ActivityList = Mutex<Vec<Activity>>;

#[get("/activity")]
fn get_all(list: &State<ActivityList>) -> Json<Vec<Activity>> {
    let items = list.lock().unwrap();
    Json(items.clone())
}

#[get("/activity/<id>")]
fn get_by_id(id: u64, list: &State<ActivityList>) -> Option<Json<Activity>> {
    let items = list.lock().unwrap();
    items.iter()
        .find(|item| item.id == id)
        .map(|item| Json(item.clone()))
}

#[post("/activity", data = "<item>")]
fn create(item: Json<Activity>, list: &State<ActivityList>) -> Json<Activity> {
    let mut items = list.lock().unwrap();
    items.push(item.clone());
    item
}

#[put("/activity/<id>", data = "<item>")]
fn update(id: u64, item: Json<Activity>, list: &State<ActivityList>) -> Option<Json<Activity>> {
    let mut items = list.lock().unwrap();
    items.iter_mut()
        .find(|i| i.id == id)
        .map(|i| {
            *i = item.clone();
            Json(i.clone())
        })
}

#[delete("/activity/<id>")]
fn delete(id: u64, list: &State<ActivityList>) -> Option<()> {
    let mut items = list.lock().unwrap();
    let pos = items.iter().position(|i| i.id == id)?;
    items.remove(pos);
    Some(())
}

#[launch]
fn rocket() -> _ {
    rocket::build()
        .manage(ActivityList::new(Vec::new()))
        .mount("/api", routes![get_all, get_by_id, create, update, delete])
}
