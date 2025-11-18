#[macro_use] extern crate rocket;

use rocket::serde::{json::Json, Deserialize, Serialize};
use rocket::State;
use std::sync::Mutex;

#[derive(Serialize, Deserialize, Clone)]
#[serde(crate = "rocket::serde")]
struct Subscription {
    id: u64,
    name: String,
}

type SubscriptionList = Mutex<Vec<Subscription>>;

#[get("/subscription")]
fn get_all(list: &State<SubscriptionList>) -> Json<Vec<Subscription>> {
    let items = list.lock().unwrap();
    Json(items.clone())
}

#[get("/subscription/<id>")]
fn get_by_id(id: u64, list: &State<SubscriptionList>) -> Option<Json<Subscription>> {
    let items = list.lock().unwrap();
    items.iter()
        .find(|item| item.id == id)
        .map(|item| Json(item.clone()))
}

#[post("/subscription", data = "<item>")]
fn create(item: Json<Subscription>, list: &State<SubscriptionList>) -> Json<Subscription> {
    let mut items = list.lock().unwrap();
    items.push(item.clone());
    item
}

#[put("/subscription/<id>", data = "<item>")]
fn update(id: u64, item: Json<Subscription>, list: &State<SubscriptionList>) -> Option<Json<Subscription>> {
    let mut items = list.lock().unwrap();
    items.iter_mut()
        .find(|i| i.id == id)
        .map(|i| {
            *i = item.clone();
            Json(i.clone())
        })
}

#[delete("/subscription/<id>")]
fn delete(id: u64, list: &State<SubscriptionList>) -> Option<()> {
    let mut items = list.lock().unwrap();
    let pos = items.iter().position(|i| i.id == id)?;
    items.remove(pos);
    Some(())
}

#[launch]
fn rocket() -> _ {
    rocket::build()
        .manage(SubscriptionList::new(Vec::new()))
        .mount("/api", routes![get_all, get_by_id, create, update, delete])
}
