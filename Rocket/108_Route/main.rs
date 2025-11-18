#[macro_use] extern crate rocket;

use rocket::serde::{json::Json, Deserialize, Serialize};
use rocket::State;
use std::sync::Mutex;

#[derive(Serialize, Deserialize, Clone)]
#[serde(crate = "rocket::serde")]
struct Route {
    id: u64,
    name: String,
}

type RouteList = Mutex<Vec<Route>>;

#[get("/route")]
fn get_all(list: &State<RouteList>) -> Json<Vec<Route>> {
    let items = list.lock().unwrap();
    Json(items.clone())
}

#[get("/route/<id>")]
fn get_by_id(id: u64, list: &State<RouteList>) -> Option<Json<Route>> {
    let items = list.lock().unwrap();
    items.iter()
        .find(|item| item.id == id)
        .map(|item| Json(item.clone()))
}

#[post("/route", data = "<item>")]
fn create(item: Json<Route>, list: &State<RouteList>) -> Json<Route> {
    let mut items = list.lock().unwrap();
    items.push(item.clone());
    item
}

#[put("/route/<id>", data = "<item>")]
fn update(id: u64, item: Json<Route>, list: &State<RouteList>) -> Option<Json<Route>> {
    let mut items = list.lock().unwrap();
    items.iter_mut()
        .find(|i| i.id == id)
        .map(|i| {
            *i = item.clone();
            Json(i.clone())
        })
}

#[delete("/route/<id>")]
fn delete(id: u64, list: &State<RouteList>) -> Option<()> {
    let mut items = list.lock().unwrap();
    let pos = items.iter().position(|i| i.id == id)?;
    items.remove(pos);
    Some(())
}

#[launch]
fn rocket() -> _ {
    rocket::build()
        .manage(RouteList::new(Vec::new()))
        .mount("/api", routes![get_all, get_by_id, create, update, delete])
}
