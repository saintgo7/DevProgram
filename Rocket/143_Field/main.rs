#[macro_use] extern crate rocket;

use rocket::serde::{json::Json, Deserialize, Serialize};
use rocket::State;
use std::sync::Mutex;

#[derive(Serialize, Deserialize, Clone)]
#[serde(crate = "rocket::serde")]
struct Field {
    id: u64,
    name: String,
}

type FieldList = Mutex<Vec<Field>>;

#[get("/field")]
fn get_all(list: &State<FieldList>) -> Json<Vec<Field>> {
    let items = list.lock().unwrap();
    Json(items.clone())
}

#[get("/field/<id>")]
fn get_by_id(id: u64, list: &State<FieldList>) -> Option<Json<Field>> {
    let items = list.lock().unwrap();
    items.iter()
        .find(|item| item.id == id)
        .map(|item| Json(item.clone()))
}

#[post("/field", data = "<item>")]
fn create(item: Json<Field>, list: &State<FieldList>) -> Json<Field> {
    let mut items = list.lock().unwrap();
    items.push(item.clone());
    item
}

#[put("/field/<id>", data = "<item>")]
fn update(id: u64, item: Json<Field>, list: &State<FieldList>) -> Option<Json<Field>> {
    let mut items = list.lock().unwrap();
    items.iter_mut()
        .find(|i| i.id == id)
        .map(|i| {
            *i = item.clone();
            Json(i.clone())
        })
}

#[delete("/field/<id>")]
fn delete(id: u64, list: &State<FieldList>) -> Option<()> {
    let mut items = list.lock().unwrap();
    let pos = items.iter().position(|i| i.id == id)?;
    items.remove(pos);
    Some(())
}

#[launch]
fn rocket() -> _ {
    rocket::build()
        .manage(FieldList::new(Vec::new()))
        .mount("/api", routes![get_all, get_by_id, create, update, delete])
}
