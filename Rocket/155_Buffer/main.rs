#[macro_use] extern crate rocket;

use rocket::serde::{json::Json, Deserialize, Serialize};
use rocket::State;
use std::sync::Mutex;

#[derive(Serialize, Deserialize, Clone)]
#[serde(crate = "rocket::serde")]
struct Buffer {
    id: u64,
    name: String,
}

type BufferList = Mutex<Vec<Buffer>>;

#[get("/buffer")]
fn get_all(list: &State<BufferList>) -> Json<Vec<Buffer>> {
    let items = list.lock().unwrap();
    Json(items.clone())
}

#[get("/buffer/<id>")]
fn get_by_id(id: u64, list: &State<BufferList>) -> Option<Json<Buffer>> {
    let items = list.lock().unwrap();
    items.iter()
        .find(|item| item.id == id)
        .map(|item| Json(item.clone()))
}

#[post("/buffer", data = "<item>")]
fn create(item: Json<Buffer>, list: &State<BufferList>) -> Json<Buffer> {
    let mut items = list.lock().unwrap();
    items.push(item.clone());
    item
}

#[put("/buffer/<id>", data = "<item>")]
fn update(id: u64, item: Json<Buffer>, list: &State<BufferList>) -> Option<Json<Buffer>> {
    let mut items = list.lock().unwrap();
    items.iter_mut()
        .find(|i| i.id == id)
        .map(|i| {
            *i = item.clone();
            Json(i.clone())
        })
}

#[delete("/buffer/<id>")]
fn delete(id: u64, list: &State<BufferList>) -> Option<()> {
    let mut items = list.lock().unwrap();
    let pos = items.iter().position(|i| i.id == id)?;
    items.remove(pos);
    Some(())
}

#[launch]
fn rocket() -> _ {
    rocket::build()
        .manage(BufferList::new(Vec::new()))
        .mount("/api", routes![get_all, get_by_id, create, update, delete])
}
