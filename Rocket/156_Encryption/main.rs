#[macro_use] extern crate rocket;

use rocket::serde::{json::Json, Deserialize, Serialize};
use rocket::State;
use std::sync::Mutex;

#[derive(Serialize, Deserialize, Clone)]
#[serde(crate = "rocket::serde")]
struct Encryption {
    id: u64,
    name: String,
}

type EncryptionList = Mutex<Vec<Encryption>>;

#[get("/encryption")]
fn get_all(list: &State<EncryptionList>) -> Json<Vec<Encryption>> {
    let items = list.lock().unwrap();
    Json(items.clone())
}

#[get("/encryption/<id>")]
fn get_by_id(id: u64, list: &State<EncryptionList>) -> Option<Json<Encryption>> {
    let items = list.lock().unwrap();
    items.iter()
        .find(|item| item.id == id)
        .map(|item| Json(item.clone()))
}

#[post("/encryption", data = "<item>")]
fn create(item: Json<Encryption>, list: &State<EncryptionList>) -> Json<Encryption> {
    let mut items = list.lock().unwrap();
    items.push(item.clone());
    item
}

#[put("/encryption/<id>", data = "<item>")]
fn update(id: u64, item: Json<Encryption>, list: &State<EncryptionList>) -> Option<Json<Encryption>> {
    let mut items = list.lock().unwrap();
    items.iter_mut()
        .find(|i| i.id == id)
        .map(|i| {
            *i = item.clone();
            Json(i.clone())
        })
}

#[delete("/encryption/<id>")]
fn delete(id: u64, list: &State<EncryptionList>) -> Option<()> {
    let mut items = list.lock().unwrap();
    let pos = items.iter().position(|i| i.id == id)?;
    items.remove(pos);
    Some(())
}

#[launch]
fn rocket() -> _ {
    rocket::build()
        .manage(EncryptionList::new(Vec::new()))
        .mount("/api", routes![get_all, get_by_id, create, update, delete])
}
