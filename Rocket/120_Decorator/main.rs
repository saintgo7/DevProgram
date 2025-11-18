#[macro_use] extern crate rocket;

use rocket::serde::{json::Json, Deserialize, Serialize};
use rocket::State;
use std::sync::Mutex;

#[derive(Serialize, Deserialize, Clone)]
#[serde(crate = "rocket::serde")]
struct Decorator {
    id: u64,
    name: String,
}

type DecoratorList = Mutex<Vec<Decorator>>;

#[get("/decorator")]
fn get_all(list: &State<DecoratorList>) -> Json<Vec<Decorator>> {
    let items = list.lock().unwrap();
    Json(items.clone())
}

#[get("/decorator/<id>")]
fn get_by_id(id: u64, list: &State<DecoratorList>) -> Option<Json<Decorator>> {
    let items = list.lock().unwrap();
    items.iter()
        .find(|item| item.id == id)
        .map(|item| Json(item.clone()))
}

#[post("/decorator", data = "<item>")]
fn create(item: Json<Decorator>, list: &State<DecoratorList>) -> Json<Decorator> {
    let mut items = list.lock().unwrap();
    items.push(item.clone());
    item
}

#[put("/decorator/<id>", data = "<item>")]
fn update(id: u64, item: Json<Decorator>, list: &State<DecoratorList>) -> Option<Json<Decorator>> {
    let mut items = list.lock().unwrap();
    items.iter_mut()
        .find(|i| i.id == id)
        .map(|i| {
            *i = item.clone();
            Json(i.clone())
        })
}

#[delete("/decorator/<id>")]
fn delete(id: u64, list: &State<DecoratorList>) -> Option<()> {
    let mut items = list.lock().unwrap();
    let pos = items.iter().position(|i| i.id == id)?;
    items.remove(pos);
    Some(())
}

#[launch]
fn rocket() -> _ {
    rocket::build()
        .manage(DecoratorList::new(Vec::new()))
        .mount("/api", routes![get_all, get_by_id, create, update, delete])
}
