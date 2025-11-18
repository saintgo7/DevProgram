#[macro_use] extern crate rocket;

use rocket::serde::{json::Json, Deserialize, Serialize};
use rocket::State;
use std::sync::Mutex;

#[derive(Serialize, Deserialize, Clone)]
#[serde(crate = "rocket::serde")]
struct Cookie {
    id: u64,
    name: String,
}

type CookieList = Mutex<Vec<Cookie>>;

#[get("/cookie")]
fn get_all(list: &State<CookieList>) -> Json<Vec<Cookie>> {
    let items = list.lock().unwrap();
    Json(items.clone())
}

#[get("/cookie/<id>")]
fn get_by_id(id: u64, list: &State<CookieList>) -> Option<Json<Cookie>> {
    let items = list.lock().unwrap();
    items.iter()
        .find(|item| item.id == id)
        .map(|item| Json(item.clone()))
}

#[post("/cookie", data = "<item>")]
fn create(item: Json<Cookie>, list: &State<CookieList>) -> Json<Cookie> {
    let mut items = list.lock().unwrap();
    items.push(item.clone());
    item
}

#[put("/cookie/<id>", data = "<item>")]
fn update(id: u64, item: Json<Cookie>, list: &State<CookieList>) -> Option<Json<Cookie>> {
    let mut items = list.lock().unwrap();
    items.iter_mut()
        .find(|i| i.id == id)
        .map(|i| {
            *i = item.clone();
            Json(i.clone())
        })
}

#[delete("/cookie/<id>")]
fn delete(id: u64, list: &State<CookieList>) -> Option<()> {
    let mut items = list.lock().unwrap();
    let pos = items.iter().position(|i| i.id == id)?;
    items.remove(pos);
    Some(())
}

#[launch]
fn rocket() -> _ {
    rocket::build()
        .manage(CookieList::new(Vec::new()))
        .mount("/api", routes![get_all, get_by_id, create, update, delete])
}
