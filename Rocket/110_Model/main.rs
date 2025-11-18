#[macro_use] extern crate rocket;

use rocket::serde::{json::Json, Deserialize, Serialize};
use rocket::State;
use std::sync::Mutex;

#[derive(Serialize, Deserialize, Clone)]
#[serde(crate = "rocket::serde")]
struct Model {
    id: u64,
    name: String,
}

type ModelList = Mutex<Vec<Model>>;

#[get("/model")]
fn get_all(list: &State<ModelList>) -> Json<Vec<Model>> {
    let items = list.lock().unwrap();
    Json(items.clone())
}

#[get("/model/<id>")]
fn get_by_id(id: u64, list: &State<ModelList>) -> Option<Json<Model>> {
    let items = list.lock().unwrap();
    items.iter()
        .find(|item| item.id == id)
        .map(|item| Json(item.clone()))
}

#[post("/model", data = "<item>")]
fn create(item: Json<Model>, list: &State<ModelList>) -> Json<Model> {
    let mut items = list.lock().unwrap();
    items.push(item.clone());
    item
}

#[put("/model/<id>", data = "<item>")]
fn update(id: u64, item: Json<Model>, list: &State<ModelList>) -> Option<Json<Model>> {
    let mut items = list.lock().unwrap();
    items.iter_mut()
        .find(|i| i.id == id)
        .map(|i| {
            *i = item.clone();
            Json(i.clone())
        })
}

#[delete("/model/<id>")]
fn delete(id: u64, list: &State<ModelList>) -> Option<()> {
    let mut items = list.lock().unwrap();
    let pos = items.iter().position(|i| i.id == id)?;
    items.remove(pos);
    Some(())
}

#[launch]
fn rocket() -> _ {
    rocket::build()
        .manage(ModelList::new(Vec::new()))
        .mount("/api", routes![get_all, get_by_id, create, update, delete])
}
