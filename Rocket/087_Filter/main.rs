#[macro_use] extern crate rocket;

use rocket::serde::{json::Json, Deserialize, Serialize};
use rocket::State;
use std::sync::Mutex;

#[derive(Serialize, Deserialize, Clone)]
#[serde(crate = "rocket::serde")]
struct Filter {
    id: u64,
    name: String,
}

type FilterList = Mutex<Vec<Filter>>;

#[get("/filter")]
fn get_all(list: &State<FilterList>) -> Json<Vec<Filter>> {
    let items = list.lock().unwrap();
    Json(items.clone())
}

#[get("/filter/<id>")]
fn get_by_id(id: u64, list: &State<FilterList>) -> Option<Json<Filter>> {
    let items = list.lock().unwrap();
    items.iter()
        .find(|item| item.id == id)
        .map(|item| Json(item.clone()))
}

#[post("/filter", data = "<item>")]
fn create(item: Json<Filter>, list: &State<FilterList>) -> Json<Filter> {
    let mut items = list.lock().unwrap();
    items.push(item.clone());
    item
}

#[put("/filter/<id>", data = "<item>")]
fn update(id: u64, item: Json<Filter>, list: &State<FilterList>) -> Option<Json<Filter>> {
    let mut items = list.lock().unwrap();
    items.iter_mut()
        .find(|i| i.id == id)
        .map(|i| {
            *i = item.clone();
            Json(i.clone())
        })
}

#[delete("/filter/<id>")]
fn delete(id: u64, list: &State<FilterList>) -> Option<()> {
    let mut items = list.lock().unwrap();
    let pos = items.iter().position(|i| i.id == id)?;
    items.remove(pos);
    Some(())
}

#[launch]
fn rocket() -> _ {
    rocket::build()
        .manage(FilterList::new(Vec::new()))
        .mount("/api", routes![get_all, get_by_id, create, update, delete])
}
