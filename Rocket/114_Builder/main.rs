#[macro_use] extern crate rocket;

use rocket::serde::{json::Json, Deserialize, Serialize};
use rocket::State;
use std::sync::Mutex;

#[derive(Serialize, Deserialize, Clone)]
#[serde(crate = "rocket::serde")]
struct Builder {
    id: u64,
    name: String,
}

type BuilderList = Mutex<Vec<Builder>>;

#[get("/builder")]
fn get_all(list: &State<BuilderList>) -> Json<Vec<Builder>> {
    let items = list.lock().unwrap();
    Json(items.clone())
}

#[get("/builder/<id>")]
fn get_by_id(id: u64, list: &State<BuilderList>) -> Option<Json<Builder>> {
    let items = list.lock().unwrap();
    items.iter()
        .find(|item| item.id == id)
        .map(|item| Json(item.clone()))
}

#[post("/builder", data = "<item>")]
fn create(item: Json<Builder>, list: &State<BuilderList>) -> Json<Builder> {
    let mut items = list.lock().unwrap();
    items.push(item.clone());
    item
}

#[put("/builder/<id>", data = "<item>")]
fn update(id: u64, item: Json<Builder>, list: &State<BuilderList>) -> Option<Json<Builder>> {
    let mut items = list.lock().unwrap();
    items.iter_mut()
        .find(|i| i.id == id)
        .map(|i| {
            *i = item.clone();
            Json(i.clone())
        })
}

#[delete("/builder/<id>")]
fn delete(id: u64, list: &State<BuilderList>) -> Option<()> {
    let mut items = list.lock().unwrap();
    let pos = items.iter().position(|i| i.id == id)?;
    items.remove(pos);
    Some(())
}

#[launch]
fn rocket() -> _ {
    rocket::build()
        .manage(BuilderList::new(Vec::new()))
        .mount("/api", routes![get_all, get_by_id, create, update, delete])
}
