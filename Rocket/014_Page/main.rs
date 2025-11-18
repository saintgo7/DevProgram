#[macro_use] extern crate rocket;

use rocket::serde::{json::Json, Deserialize, Serialize};
use rocket::State;
use std::sync::Mutex;

#[derive(Serialize, Deserialize, Clone)]
#[serde(crate = "rocket::serde")]
struct Page {
    id: u64,
    name: String,
}

type PageList = Mutex<Vec<Page>>;

#[get("/page")]
fn get_all(list: &State<PageList>) -> Json<Vec<Page>> {
    let items = list.lock().unwrap();
    Json(items.clone())
}

#[get("/page/<id>")]
fn get_by_id(id: u64, list: &State<PageList>) -> Option<Json<Page>> {
    let items = list.lock().unwrap();
    items.iter()
        .find(|item| item.id == id)
        .map(|item| Json(item.clone()))
}

#[post("/page", data = "<item>")]
fn create(item: Json<Page>, list: &State<PageList>) -> Json<Page> {
    let mut items = list.lock().unwrap();
    items.push(item.clone());
    item
}

#[put("/page/<id>", data = "<item>")]
fn update(id: u64, item: Json<Page>, list: &State<PageList>) -> Option<Json<Page>> {
    let mut items = list.lock().unwrap();
    items.iter_mut()
        .find(|i| i.id == id)
        .map(|i| {
            *i = item.clone();
            Json(i.clone())
        })
}

#[delete("/page/<id>")]
fn delete(id: u64, list: &State<PageList>) -> Option<()> {
    let mut items = list.lock().unwrap();
    let pos = items.iter().position(|i| i.id == id)?;
    items.remove(pos);
    Some(())
}

#[launch]
fn rocket() -> _ {
    rocket::build()
        .manage(PageList::new(Vec::new()))
        .mount("/api", routes![get_all, get_by_id, create, update, delete])
}
