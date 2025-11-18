#[macro_use] extern crate rocket;

use rocket::serde::{json::Json, Deserialize, Serialize};
use rocket::State;
use std::sync::Mutex;

#[derive(Serialize, Deserialize, Clone)]
#[serde(crate = "rocket::serde")]
struct Graph {
    id: u64,
    name: String,
}

type GraphList = Mutex<Vec<Graph>>;

#[get("/graph")]
fn get_all(list: &State<GraphList>) -> Json<Vec<Graph>> {
    let items = list.lock().unwrap();
    Json(items.clone())
}

#[get("/graph/<id>")]
fn get_by_id(id: u64, list: &State<GraphList>) -> Option<Json<Graph>> {
    let items = list.lock().unwrap();
    items.iter()
        .find(|item| item.id == id)
        .map(|item| Json(item.clone()))
}

#[post("/graph", data = "<item>")]
fn create(item: Json<Graph>, list: &State<GraphList>) -> Json<Graph> {
    let mut items = list.lock().unwrap();
    items.push(item.clone());
    item
}

#[put("/graph/<id>", data = "<item>")]
fn update(id: u64, item: Json<Graph>, list: &State<GraphList>) -> Option<Json<Graph>> {
    let mut items = list.lock().unwrap();
    items.iter_mut()
        .find(|i| i.id == id)
        .map(|i| {
            *i = item.clone();
            Json(i.clone())
        })
}

#[delete("/graph/<id>")]
fn delete(id: u64, list: &State<GraphList>) -> Option<()> {
    let mut items = list.lock().unwrap();
    let pos = items.iter().position(|i| i.id == id)?;
    items.remove(pos);
    Some(())
}

#[launch]
fn rocket() -> _ {
    rocket::build()
        .manage(GraphList::new(Vec::new()))
        .mount("/api", routes![get_all, get_by_id, create, update, delete])
}
