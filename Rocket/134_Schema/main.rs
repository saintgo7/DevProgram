#[macro_use] extern crate rocket;

use rocket::serde::{json::Json, Deserialize, Serialize};
use rocket::State;
use std::sync::Mutex;

#[derive(Serialize, Deserialize, Clone)]
#[serde(crate = "rocket::serde")]
struct Schema {
    id: u64,
    name: String,
}

type SchemaList = Mutex<Vec<Schema>>;

#[get("/schema")]
fn get_all(list: &State<SchemaList>) -> Json<Vec<Schema>> {
    let items = list.lock().unwrap();
    Json(items.clone())
}

#[get("/schema/<id>")]
fn get_by_id(id: u64, list: &State<SchemaList>) -> Option<Json<Schema>> {
    let items = list.lock().unwrap();
    items.iter()
        .find(|item| item.id == id)
        .map(|item| Json(item.clone()))
}

#[post("/schema", data = "<item>")]
fn create(item: Json<Schema>, list: &State<SchemaList>) -> Json<Schema> {
    let mut items = list.lock().unwrap();
    items.push(item.clone());
    item
}

#[put("/schema/<id>", data = "<item>")]
fn update(id: u64, item: Json<Schema>, list: &State<SchemaList>) -> Option<Json<Schema>> {
    let mut items = list.lock().unwrap();
    items.iter_mut()
        .find(|i| i.id == id)
        .map(|i| {
            *i = item.clone();
            Json(i.clone())
        })
}

#[delete("/schema/<id>")]
fn delete(id: u64, list: &State<SchemaList>) -> Option<()> {
    let mut items = list.lock().unwrap();
    let pos = items.iter().position(|i| i.id == id)?;
    items.remove(pos);
    Some(())
}

#[launch]
fn rocket() -> _ {
    rocket::build()
        .manage(SchemaList::new(Vec::new()))
        .mount("/api", routes![get_all, get_by_id, create, update, delete])
}
