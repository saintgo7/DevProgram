#[macro_use] extern crate rocket;

use rocket::serde::{json::Json, Deserialize, Serialize};
use rocket::State;
use std::sync::Mutex;

#[derive(Serialize, Deserialize, Clone)]
#[serde(crate = "rocket::serde")]
struct WebSocket {
    id: u64,
    name: String,
}

type WebSocketList = Mutex<Vec<WebSocket>>;

#[get("/websocket")]
fn get_all(list: &State<WebSocketList>) -> Json<Vec<WebSocket>> {
    let items = list.lock().unwrap();
    Json(items.clone())
}

#[get("/websocket/<id>")]
fn get_by_id(id: u64, list: &State<WebSocketList>) -> Option<Json<WebSocket>> {
    let items = list.lock().unwrap();
    items.iter()
        .find(|item| item.id == id)
        .map(|item| Json(item.clone()))
}

#[post("/websocket", data = "<item>")]
fn create(item: Json<WebSocket>, list: &State<WebSocketList>) -> Json<WebSocket> {
    let mut items = list.lock().unwrap();
    items.push(item.clone());
    item
}

#[put("/websocket/<id>", data = "<item>")]
fn update(id: u64, item: Json<WebSocket>, list: &State<WebSocketList>) -> Option<Json<WebSocket>> {
    let mut items = list.lock().unwrap();
    items.iter_mut()
        .find(|i| i.id == id)
        .map(|i| {
            *i = item.clone();
            Json(i.clone())
        })
}

#[delete("/websocket/<id>")]
fn delete(id: u64, list: &State<WebSocketList>) -> Option<()> {
    let mut items = list.lock().unwrap();
    let pos = items.iter().position(|i| i.id == id)?;
    items.remove(pos);
    Some(())
}

#[launch]
fn rocket() -> _ {
    rocket::build()
        .manage(WebSocketList::new(Vec::new()))
        .mount("/api", routes![get_all, get_by_id, create, update, delete])
}
