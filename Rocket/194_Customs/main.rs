#[macro_use] extern crate rocket;

use rocket::serde::{json::Json, Deserialize, Serialize};
use rocket::State;
use std::sync::Mutex;

#[derive(Serialize, Deserialize, Clone)]
#[serde(crate = "rocket::serde")]
struct Customs {
    id: u64,
    name: String,
}

type CustomsList = Mutex<Vec<Customs>>;

#[get("/customs")]
fn get_all(list: &State<CustomsList>) -> Json<Vec<Customs>> {
    let items = list.lock().unwrap();
    Json(items.clone())
}

#[get("/customs/<id>")]
fn get_by_id(id: u64, list: &State<CustomsList>) -> Option<Json<Customs>> {
    let items = list.lock().unwrap();
    items.iter()
        .find(|item| item.id == id)
        .map(|item| Json(item.clone()))
}

#[post("/customs", data = "<item>")]
fn create(item: Json<Customs>, list: &State<CustomsList>) -> Json<Customs> {
    let mut items = list.lock().unwrap();
    items.push(item.clone());
    item
}

#[put("/customs/<id>", data = "<item>")]
fn update(id: u64, item: Json<Customs>, list: &State<CustomsList>) -> Option<Json<Customs>> {
    let mut items = list.lock().unwrap();
    items.iter_mut()
        .find(|i| i.id == id)
        .map(|i| {
            *i = item.clone();
            Json(i.clone())
        })
}

#[delete("/customs/<id>")]
fn delete(id: u64, list: &State<CustomsList>) -> Option<()> {
    let mut items = list.lock().unwrap();
    let pos = items.iter().position(|i| i.id == id)?;
    items.remove(pos);
    Some(())
}

#[launch]
fn rocket() -> _ {
    rocket::build()
        .manage(CustomsList::new(Vec::new()))
        .mount("/api", routes![get_all, get_by_id, create, update, delete])
}
