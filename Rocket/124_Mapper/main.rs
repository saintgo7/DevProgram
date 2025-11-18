#[macro_use] extern crate rocket;

use rocket::serde::{json::Json, Deserialize, Serialize};
use rocket::State;
use std::sync::Mutex;

#[derive(Serialize, Deserialize, Clone)]
#[serde(crate = "rocket::serde")]
struct Mapper {
    id: u64,
    name: String,
}

type MapperList = Mutex<Vec<Mapper>>;

#[get("/mapper")]
fn get_all(list: &State<MapperList>) -> Json<Vec<Mapper>> {
    let items = list.lock().unwrap();
    Json(items.clone())
}

#[get("/mapper/<id>")]
fn get_by_id(id: u64, list: &State<MapperList>) -> Option<Json<Mapper>> {
    let items = list.lock().unwrap();
    items.iter()
        .find(|item| item.id == id)
        .map(|item| Json(item.clone()))
}

#[post("/mapper", data = "<item>")]
fn create(item: Json<Mapper>, list: &State<MapperList>) -> Json<Mapper> {
    let mut items = list.lock().unwrap();
    items.push(item.clone());
    item
}

#[put("/mapper/<id>", data = "<item>")]
fn update(id: u64, item: Json<Mapper>, list: &State<MapperList>) -> Option<Json<Mapper>> {
    let mut items = list.lock().unwrap();
    items.iter_mut()
        .find(|i| i.id == id)
        .map(|i| {
            *i = item.clone();
            Json(i.clone())
        })
}

#[delete("/mapper/<id>")]
fn delete(id: u64, list: &State<MapperList>) -> Option<()> {
    let mut items = list.lock().unwrap();
    let pos = items.iter().position(|i| i.id == id)?;
    items.remove(pos);
    Some(())
}

#[launch]
fn rocket() -> _ {
    rocket::build()
        .manage(MapperList::new(Vec::new()))
        .mount("/api", routes![get_all, get_by_id, create, update, delete])
}
