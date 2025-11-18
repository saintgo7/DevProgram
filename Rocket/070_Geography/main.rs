#[macro_use] extern crate rocket;

use rocket::serde::{json::Json, Deserialize, Serialize};
use rocket::State;
use std::sync::Mutex;

#[derive(Serialize, Deserialize, Clone)]
#[serde(crate = "rocket::serde")]
struct Geography {
    id: u64,
    name: String,
}

type GeographyList = Mutex<Vec<Geography>>;

#[get("/geography")]
fn get_all(list: &State<GeographyList>) -> Json<Vec<Geography>> {
    let items = list.lock().unwrap();
    Json(items.clone())
}

#[get("/geography/<id>")]
fn get_by_id(id: u64, list: &State<GeographyList>) -> Option<Json<Geography>> {
    let items = list.lock().unwrap();
    items.iter()
        .find(|item| item.id == id)
        .map(|item| Json(item.clone()))
}

#[post("/geography", data = "<item>")]
fn create(item: Json<Geography>, list: &State<GeographyList>) -> Json<Geography> {
    let mut items = list.lock().unwrap();
    items.push(item.clone());
    item
}

#[put("/geography/<id>", data = "<item>")]
fn update(id: u64, item: Json<Geography>, list: &State<GeographyList>) -> Option<Json<Geography>> {
    let mut items = list.lock().unwrap();
    items.iter_mut()
        .find(|i| i.id == id)
        .map(|i| {
            *i = item.clone();
            Json(i.clone())
        })
}

#[delete("/geography/<id>")]
fn delete(id: u64, list: &State<GeographyList>) -> Option<()> {
    let mut items = list.lock().unwrap();
    let pos = items.iter().position(|i| i.id == id)?;
    items.remove(pos);
    Some(())
}

#[launch]
fn rocket() -> _ {
    rocket::build()
        .manage(GeographyList::new(Vec::new()))
        .mount("/api", routes![get_all, get_by_id, create, update, delete])
}
