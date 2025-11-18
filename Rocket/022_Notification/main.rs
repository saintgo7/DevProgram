#[macro_use] extern crate rocket;

use rocket::serde::{json::Json, Deserialize, Serialize};
use rocket::State;
use std::sync::Mutex;

#[derive(Serialize, Deserialize, Clone)]
#[serde(crate = "rocket::serde")]
struct Notification {
    id: u64,
    name: String,
}

type NotificationList = Mutex<Vec<Notification>>;

#[get("/notification")]
fn get_all(list: &State<NotificationList>) -> Json<Vec<Notification>> {
    let items = list.lock().unwrap();
    Json(items.clone())
}

#[get("/notification/<id>")]
fn get_by_id(id: u64, list: &State<NotificationList>) -> Option<Json<Notification>> {
    let items = list.lock().unwrap();
    items.iter()
        .find(|item| item.id == id)
        .map(|item| Json(item.clone()))
}

#[post("/notification", data = "<item>")]
fn create(item: Json<Notification>, list: &State<NotificationList>) -> Json<Notification> {
    let mut items = list.lock().unwrap();
    items.push(item.clone());
    item
}

#[put("/notification/<id>", data = "<item>")]
fn update(id: u64, item: Json<Notification>, list: &State<NotificationList>) -> Option<Json<Notification>> {
    let mut items = list.lock().unwrap();
    items.iter_mut()
        .find(|i| i.id == id)
        .map(|i| {
            *i = item.clone();
            Json(i.clone())
        })
}

#[delete("/notification/<id>")]
fn delete(id: u64, list: &State<NotificationList>) -> Option<()> {
    let mut items = list.lock().unwrap();
    let pos = items.iter().position(|i| i.id == id)?;
    items.remove(pos);
    Some(())
}

#[launch]
fn rocket() -> _ {
    rocket::build()
        .manage(NotificationList::new(Vec::new()))
        .mount("/api", routes![get_all, get_by_id, create, update, delete])
}
