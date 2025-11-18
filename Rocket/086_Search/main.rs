#[macro_use] extern crate rocket;

use rocket::serde::{json::Json, Deserialize, Serialize};
use rocket::State;
use std::sync::Mutex;

#[derive(Serialize, Deserialize, Clone)]
#[serde(crate = "rocket::serde")]
struct Search {
    id: u64,
    name: String,
}

type SearchList = Mutex<Vec<Search>>;

#[get("/search")]
fn get_all(list: &State<SearchList>) -> Json<Vec<Search>> {
    let items = list.lock().unwrap();
    Json(items.clone())
}

#[get("/search/<id>")]
fn get_by_id(id: u64, list: &State<SearchList>) -> Option<Json<Search>> {
    let items = list.lock().unwrap();
    items.iter()
        .find(|item| item.id == id)
        .map(|item| Json(item.clone()))
}

#[post("/search", data = "<item>")]
fn create(item: Json<Search>, list: &State<SearchList>) -> Json<Search> {
    let mut items = list.lock().unwrap();
    items.push(item.clone());
    item
}

#[put("/search/<id>", data = "<item>")]
fn update(id: u64, item: Json<Search>, list: &State<SearchList>) -> Option<Json<Search>> {
    let mut items = list.lock().unwrap();
    items.iter_mut()
        .find(|i| i.id == id)
        .map(|i| {
            *i = item.clone();
            Json(i.clone())
        })
}

#[delete("/search/<id>")]
fn delete(id: u64, list: &State<SearchList>) -> Option<()> {
    let mut items = list.lock().unwrap();
    let pos = items.iter().position(|i| i.id == id)?;
    items.remove(pos);
    Some(())
}

#[launch]
fn rocket() -> _ {
    rocket::build()
        .manage(SearchList::new(Vec::new()))
        .mount("/api", routes![get_all, get_by_id, create, update, delete])
}
