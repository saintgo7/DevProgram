#[macro_use] extern crate rocket;

use rocket::serde::{json::Json, Deserialize, Serialize};
use rocket::State;
use std::sync::Mutex;

#[derive(Serialize, Deserialize, Clone)]
#[serde(crate = "rocket::serde")]
struct Interceptor {
    id: u64,
    name: String,
}

type InterceptorList = Mutex<Vec<Interceptor>>;

#[get("/interceptor")]
fn get_all(list: &State<InterceptorList>) -> Json<Vec<Interceptor>> {
    let items = list.lock().unwrap();
    Json(items.clone())
}

#[get("/interceptor/<id>")]
fn get_by_id(id: u64, list: &State<InterceptorList>) -> Option<Json<Interceptor>> {
    let items = list.lock().unwrap();
    items.iter()
        .find(|item| item.id == id)
        .map(|item| Json(item.clone()))
}

#[post("/interceptor", data = "<item>")]
fn create(item: Json<Interceptor>, list: &State<InterceptorList>) -> Json<Interceptor> {
    let mut items = list.lock().unwrap();
    items.push(item.clone());
    item
}

#[put("/interceptor/<id>", data = "<item>")]
fn update(id: u64, item: Json<Interceptor>, list: &State<InterceptorList>) -> Option<Json<Interceptor>> {
    let mut items = list.lock().unwrap();
    items.iter_mut()
        .find(|i| i.id == id)
        .map(|i| {
            *i = item.clone();
            Json(i.clone())
        })
}

#[delete("/interceptor/<id>")]
fn delete(id: u64, list: &State<InterceptorList>) -> Option<()> {
    let mut items = list.lock().unwrap();
    let pos = items.iter().position(|i| i.id == id)?;
    items.remove(pos);
    Some(())
}

#[launch]
fn rocket() -> _ {
    rocket::build()
        .manage(InterceptorList::new(Vec::new()))
        .mount("/api", routes![get_all, get_by_id, create, update, delete])
}
