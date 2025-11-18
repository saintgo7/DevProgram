#[macro_use] extern crate rocket;

use rocket::serde::{json::Json, Deserialize, Serialize};
use rocket::State;
use std::sync::Mutex;

#[derive(Serialize, Deserialize, Clone)]
#[serde(crate = "rocket::serde")]
struct Feature {
    id: u64,
    name: String,
}

type FeatureList = Mutex<Vec<Feature>>;

#[get("/feature")]
fn get_all(list: &State<FeatureList>) -> Json<Vec<Feature>> {
    let items = list.lock().unwrap();
    Json(items.clone())
}

#[get("/feature/<id>")]
fn get_by_id(id: u64, list: &State<FeatureList>) -> Option<Json<Feature>> {
    let items = list.lock().unwrap();
    items.iter()
        .find(|item| item.id == id)
        .map(|item| Json(item.clone()))
}

#[post("/feature", data = "<item>")]
fn create(item: Json<Feature>, list: &State<FeatureList>) -> Json<Feature> {
    let mut items = list.lock().unwrap();
    items.push(item.clone());
    item
}

#[put("/feature/<id>", data = "<item>")]
fn update(id: u64, item: Json<Feature>, list: &State<FeatureList>) -> Option<Json<Feature>> {
    let mut items = list.lock().unwrap();
    items.iter_mut()
        .find(|i| i.id == id)
        .map(|i| {
            *i = item.clone();
            Json(i.clone())
        })
}

#[delete("/feature/<id>")]
fn delete(id: u64, list: &State<FeatureList>) -> Option<()> {
    let mut items = list.lock().unwrap();
    let pos = items.iter().position(|i| i.id == id)?;
    items.remove(pos);
    Some(())
}

#[launch]
fn rocket() -> _ {
    rocket::build()
        .manage(FeatureList::new(Vec::new()))
        .mount("/api", routes![get_all, get_by_id, create, update, delete])
}
