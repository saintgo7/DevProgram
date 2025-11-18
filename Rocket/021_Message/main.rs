#[macro_use] extern crate rocket;

use rocket::serde::{json::Json, Deserialize, Serialize};
use rocket::State;
use std::sync::Mutex;

#[derive(Serialize, Deserialize, Clone)]
#[serde(crate = "rocket::serde")]
struct Message {
    id: u64,
    name: String,
}

type MessageList = Mutex<Vec<Message>>;

#[get("/message")]
fn get_all(list: &State<MessageList>) -> Json<Vec<Message>> {
    let items = list.lock().unwrap();
    Json(items.clone())
}

#[get("/message/<id>")]
fn get_by_id(id: u64, list: &State<MessageList>) -> Option<Json<Message>> {
    let items = list.lock().unwrap();
    items.iter()
        .find(|item| item.id == id)
        .map(|item| Json(item.clone()))
}

#[post("/message", data = "<item>")]
fn create(item: Json<Message>, list: &State<MessageList>) -> Json<Message> {
    let mut items = list.lock().unwrap();
    items.push(item.clone());
    item
}

#[put("/message/<id>", data = "<item>")]
fn update(id: u64, item: Json<Message>, list: &State<MessageList>) -> Option<Json<Message>> {
    let mut items = list.lock().unwrap();
    items.iter_mut()
        .find(|i| i.id == id)
        .map(|i| {
            *i = item.clone();
            Json(i.clone())
        })
}

#[delete("/message/<id>")]
fn delete(id: u64, list: &State<MessageList>) -> Option<()> {
    let mut items = list.lock().unwrap();
    let pos = items.iter().position(|i| i.id == id)?;
    items.remove(pos);
    Some(())
}

#[launch]
fn rocket() -> _ {
    rocket::build()
        .manage(MessageList::new(Vec::new()))
        .mount("/api", routes![get_all, get_by_id, create, update, delete])
}
