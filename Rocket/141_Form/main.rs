#[macro_use] extern crate rocket;

use rocket::serde::{json::Json, Deserialize, Serialize};
use rocket::State;
use std::sync::Mutex;

#[derive(Serialize, Deserialize, Clone)]
#[serde(crate = "rocket::serde")]
struct Form {
    id: u64,
    name: String,
}

type FormList = Mutex<Vec<Form>>;

#[get("/form")]
fn get_all(list: &State<FormList>) -> Json<Vec<Form>> {
    let items = list.lock().unwrap();
    Json(items.clone())
}

#[get("/form/<id>")]
fn get_by_id(id: u64, list: &State<FormList>) -> Option<Json<Form>> {
    let items = list.lock().unwrap();
    items.iter()
        .find(|item| item.id == id)
        .map(|item| Json(item.clone()))
}

#[post("/form", data = "<item>")]
fn create(item: Json<Form>, list: &State<FormList>) -> Json<Form> {
    let mut items = list.lock().unwrap();
    items.push(item.clone());
    item
}

#[put("/form/<id>", data = "<item>")]
fn update(id: u64, item: Json<Form>, list: &State<FormList>) -> Option<Json<Form>> {
    let mut items = list.lock().unwrap();
    items.iter_mut()
        .find(|i| i.id == id)
        .map(|i| {
            *i = item.clone();
            Json(i.clone())
        })
}

#[delete("/form/<id>")]
fn delete(id: u64, list: &State<FormList>) -> Option<()> {
    let mut items = list.lock().unwrap();
    let pos = items.iter().position(|i| i.id == id)?;
    items.remove(pos);
    Some(())
}

#[launch]
fn rocket() -> _ {
    rocket::build()
        .manage(FormList::new(Vec::new()))
        .mount("/api", routes![get_all, get_by_id, create, update, delete])
}
