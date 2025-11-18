#[macro_use] extern crate rocket;

use rocket::serde::{json::Json, Deserialize, Serialize};
use rocket::State;
use std::sync::Mutex;

#[derive(Serialize, Deserialize, Clone)]
#[serde(crate = "rocket::serde")]
struct Style {
    id: u64,
    name: String,
}

type StyleList = Mutex<Vec<Style>>;

#[get("/style")]
fn get_all(list: &State<StyleList>) -> Json<Vec<Style>> {
    let items = list.lock().unwrap();
    Json(items.clone())
}

#[get("/style/<id>")]
fn get_by_id(id: u64, list: &State<StyleList>) -> Option<Json<Style>> {
    let items = list.lock().unwrap();
    items.iter()
        .find(|item| item.id == id)
        .map(|item| Json(item.clone()))
}

#[post("/style", data = "<item>")]
fn create(item: Json<Style>, list: &State<StyleList>) -> Json<Style> {
    let mut items = list.lock().unwrap();
    items.push(item.clone());
    item
}

#[put("/style/<id>", data = "<item>")]
fn update(id: u64, item: Json<Style>, list: &State<StyleList>) -> Option<Json<Style>> {
    let mut items = list.lock().unwrap();
    items.iter_mut()
        .find(|i| i.id == id)
        .map(|i| {
            *i = item.clone();
            Json(i.clone())
        })
}

#[delete("/style/<id>")]
fn delete(id: u64, list: &State<StyleList>) -> Option<()> {
    let mut items = list.lock().unwrap();
    let pos = items.iter().position(|i| i.id == id)?;
    items.remove(pos);
    Some(())
}

#[launch]
fn rocket() -> _ {
    rocket::build()
        .manage(StyleList::new(Vec::new()))
        .mount("/api", routes![get_all, get_by_id, create, update, delete])
}
