#[macro_use] extern crate rocket;

use rocket::serde::{json::Json, Deserialize, Serialize};
use rocket::State;
use std::sync::Mutex;

#[derive(Serialize, Deserialize, Clone)]
#[serde(crate = "rocket::serde")]
struct Signing {
    id: u64,
    name: String,
}

type SigningList = Mutex<Vec<Signing>>;

#[get("/signing")]
fn get_all(list: &State<SigningList>) -> Json<Vec<Signing>> {
    let items = list.lock().unwrap();
    Json(items.clone())
}

#[get("/signing/<id>")]
fn get_by_id(id: u64, list: &State<SigningList>) -> Option<Json<Signing>> {
    let items = list.lock().unwrap();
    items.iter()
        .find(|item| item.id == id)
        .map(|item| Json(item.clone()))
}

#[post("/signing", data = "<item>")]
fn create(item: Json<Signing>, list: &State<SigningList>) -> Json<Signing> {
    let mut items = list.lock().unwrap();
    items.push(item.clone());
    item
}

#[put("/signing/<id>", data = "<item>")]
fn update(id: u64, item: Json<Signing>, list: &State<SigningList>) -> Option<Json<Signing>> {
    let mut items = list.lock().unwrap();
    items.iter_mut()
        .find(|i| i.id == id)
        .map(|i| {
            *i = item.clone();
            Json(i.clone())
        })
}

#[delete("/signing/<id>")]
fn delete(id: u64, list: &State<SigningList>) -> Option<()> {
    let mut items = list.lock().unwrap();
    let pos = items.iter().position(|i| i.id == id)?;
    items.remove(pos);
    Some(())
}

#[launch]
fn rocket() -> _ {
    rocket::build()
        .manage(SigningList::new(Vec::new()))
        .mount("/api", routes![get_all, get_by_id, create, update, delete])
}
