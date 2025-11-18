#[macro_use] extern crate rocket;

use rocket::serde::{json::Json, Deserialize, Serialize};
use rocket::State;
use std::sync::Mutex;

#[derive(Serialize, Deserialize, Clone)]
#[serde(crate = "rocket::serde")]
struct Seeder {
    id: u64,
    name: String,
}

type SeederList = Mutex<Vec<Seeder>>;

#[get("/seeder")]
fn get_all(list: &State<SeederList>) -> Json<Vec<Seeder>> {
    let items = list.lock().unwrap();
    Json(items.clone())
}

#[get("/seeder/<id>")]
fn get_by_id(id: u64, list: &State<SeederList>) -> Option<Json<Seeder>> {
    let items = list.lock().unwrap();
    items.iter()
        .find(|item| item.id == id)
        .map(|item| Json(item.clone()))
}

#[post("/seeder", data = "<item>")]
fn create(item: Json<Seeder>, list: &State<SeederList>) -> Json<Seeder> {
    let mut items = list.lock().unwrap();
    items.push(item.clone());
    item
}

#[put("/seeder/<id>", data = "<item>")]
fn update(id: u64, item: Json<Seeder>, list: &State<SeederList>) -> Option<Json<Seeder>> {
    let mut items = list.lock().unwrap();
    items.iter_mut()
        .find(|i| i.id == id)
        .map(|i| {
            *i = item.clone();
            Json(i.clone())
        })
}

#[delete("/seeder/<id>")]
fn delete(id: u64, list: &State<SeederList>) -> Option<()> {
    let mut items = list.lock().unwrap();
    let pos = items.iter().position(|i| i.id == id)?;
    items.remove(pos);
    Some(())
}

#[launch]
fn rocket() -> _ {
    rocket::build()
        .manage(SeederList::new(Vec::new()))
        .mount("/api", routes![get_all, get_by_id, create, update, delete])
}
