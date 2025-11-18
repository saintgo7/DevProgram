#[macro_use] extern crate rocket;

use rocket::serde::{json::Json, Deserialize, Serialize};
use rocket::State;
use std::sync::Mutex;

#[derive(Serialize, Deserialize, Clone)]
#[serde(crate = "rocket::serde")]
struct Contact {
    id: u64,
    name: String,
}

type ContactList = Mutex<Vec<Contact>>;

#[get("/contact")]
fn get_all(list: &State<ContactList>) -> Json<Vec<Contact>> {
    let items = list.lock().unwrap();
    Json(items.clone())
}

#[get("/contact/<id>")]
fn get_by_id(id: u64, list: &State<ContactList>) -> Option<Json<Contact>> {
    let items = list.lock().unwrap();
    items.iter()
        .find(|item| item.id == id)
        .map(|item| Json(item.clone()))
}

#[post("/contact", data = "<item>")]
fn create(item: Json<Contact>, list: &State<ContactList>) -> Json<Contact> {
    let mut items = list.lock().unwrap();
    items.push(item.clone());
    item
}

#[put("/contact/<id>", data = "<item>")]
fn update(id: u64, item: Json<Contact>, list: &State<ContactList>) -> Option<Json<Contact>> {
    let mut items = list.lock().unwrap();
    items.iter_mut()
        .find(|i| i.id == id)
        .map(|i| {
            *i = item.clone();
            Json(i.clone())
        })
}

#[delete("/contact/<id>")]
fn delete(id: u64, list: &State<ContactList>) -> Option<()> {
    let mut items = list.lock().unwrap();
    let pos = items.iter().position(|i| i.id == id)?;
    items.remove(pos);
    Some(())
}

#[launch]
fn rocket() -> _ {
    rocket::build()
        .manage(ContactList::new(Vec::new()))
        .mount("/api", routes![get_all, get_by_id, create, update, delete])
}
