#[macro_use] extern crate rocket;

use rocket::serde::{json::Json, Deserialize, Serialize};
use rocket::State;
use std::sync::Mutex;

#[derive(Serialize, Deserialize, Clone)]
#[serde(crate = "rocket::serde")]
struct Phone {
    id: u64,
    name: String,
}

type PhoneList = Mutex<Vec<Phone>>;

#[get("/phone")]
fn get_all(list: &State<PhoneList>) -> Json<Vec<Phone>> {
    let items = list.lock().unwrap();
    Json(items.clone())
}

#[get("/phone/<id>")]
fn get_by_id(id: u64, list: &State<PhoneList>) -> Option<Json<Phone>> {
    let items = list.lock().unwrap();
    items.iter()
        .find(|item| item.id == id)
        .map(|item| Json(item.clone()))
}

#[post("/phone", data = "<item>")]
fn create(item: Json<Phone>, list: &State<PhoneList>) -> Json<Phone> {
    let mut items = list.lock().unwrap();
    items.push(item.clone());
    item
}

#[put("/phone/<id>", data = "<item>")]
fn update(id: u64, item: Json<Phone>, list: &State<PhoneList>) -> Option<Json<Phone>> {
    let mut items = list.lock().unwrap();
    items.iter_mut()
        .find(|i| i.id == id)
        .map(|i| {
            *i = item.clone();
            Json(i.clone())
        })
}

#[delete("/phone/<id>")]
fn delete(id: u64, list: &State<PhoneList>) -> Option<()> {
    let mut items = list.lock().unwrap();
    let pos = items.iter().position(|i| i.id == id)?;
    items.remove(pos);
    Some(())
}

#[launch]
fn rocket() -> _ {
    rocket::build()
        .manage(PhoneList::new(Vec::new()))
        .mount("/api", routes![get_all, get_by_id, create, update, delete])
}
