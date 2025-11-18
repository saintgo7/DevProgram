#[macro_use] extern crate rocket;

use rocket::serde::{json::Json, Deserialize, Serialize};
use rocket::State;
use std::sync::Mutex;

#[derive(Serialize, Deserialize, Clone)]
#[serde(crate = "rocket::serde")]
struct Chunk {
    id: u64,
    name: String,
}

type ChunkList = Mutex<Vec<Chunk>>;

#[get("/chunk")]
fn get_all(list: &State<ChunkList>) -> Json<Vec<Chunk>> {
    let items = list.lock().unwrap();
    Json(items.clone())
}

#[get("/chunk/<id>")]
fn get_by_id(id: u64, list: &State<ChunkList>) -> Option<Json<Chunk>> {
    let items = list.lock().unwrap();
    items.iter()
        .find(|item| item.id == id)
        .map(|item| Json(item.clone()))
}

#[post("/chunk", data = "<item>")]
fn create(item: Json<Chunk>, list: &State<ChunkList>) -> Json<Chunk> {
    let mut items = list.lock().unwrap();
    items.push(item.clone());
    item
}

#[put("/chunk/<id>", data = "<item>")]
fn update(id: u64, item: Json<Chunk>, list: &State<ChunkList>) -> Option<Json<Chunk>> {
    let mut items = list.lock().unwrap();
    items.iter_mut()
        .find(|i| i.id == id)
        .map(|i| {
            *i = item.clone();
            Json(i.clone())
        })
}

#[delete("/chunk/<id>")]
fn delete(id: u64, list: &State<ChunkList>) -> Option<()> {
    let mut items = list.lock().unwrap();
    let pos = items.iter().position(|i| i.id == id)?;
    items.remove(pos);
    Some(())
}

#[launch]
fn rocket() -> _ {
    rocket::build()
        .manage(ChunkList::new(Vec::new()))
        .mount("/api", routes![get_all, get_by_id, create, update, delete])
}
