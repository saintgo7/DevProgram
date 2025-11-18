#[macro_use] extern crate rocket;

use rocket::serde::{json::Json, Deserialize, Serialize};
use rocket::State;
use std::sync::Mutex;

#[derive(Serialize, Deserialize, Clone)]
#[serde(crate = "rocket::serde")]
struct JWT {
    id: u64,
    name: String,
}

type JWTList = Mutex<Vec<JWT>>;

#[get("/jwt")]
fn get_all(list: &State<JWTList>) -> Json<Vec<JWT>> {
    let items = list.lock().unwrap();
    Json(items.clone())
}

#[get("/jwt/<id>")]
fn get_by_id(id: u64, list: &State<JWTList>) -> Option<Json<JWT>> {
    let items = list.lock().unwrap();
    items.iter()
        .find(|item| item.id == id)
        .map(|item| Json(item.clone()))
}

#[post("/jwt", data = "<item>")]
fn create(item: Json<JWT>, list: &State<JWTList>) -> Json<JWT> {
    let mut items = list.lock().unwrap();
    items.push(item.clone());
    item
}

#[put("/jwt/<id>", data = "<item>")]
fn update(id: u64, item: Json<JWT>, list: &State<JWTList>) -> Option<Json<JWT>> {
    let mut items = list.lock().unwrap();
    items.iter_mut()
        .find(|i| i.id == id)
        .map(|i| {
            *i = item.clone();
            Json(i.clone())
        })
}

#[delete("/jwt/<id>")]
fn delete(id: u64, list: &State<JWTList>) -> Option<()> {
    let mut items = list.lock().unwrap();
    let pos = items.iter().position(|i| i.id == id)?;
    items.remove(pos);
    Some(())
}

#[launch]
fn rocket() -> _ {
    rocket::build()
        .manage(JWTList::new(Vec::new()))
        .mount("/api", routes![get_all, get_by_id, create, update, delete])
}
