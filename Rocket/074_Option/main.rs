#[macro_use] extern crate rocket;

use rocket::serde::{json::Json, Deserialize, Serialize};
use rocket::State;
use std::sync::Mutex;

#[derive(Serialize, Deserialize, Clone)]
#[serde(crate = "rocket::serde")]
struct Option {
    id: u64,
    name: String,
}

type OptionList = Mutex<Vec<Option>>;

#[get("/option")]
fn get_all(list: &State<OptionList>) -> Json<Vec<Option>> {
    let items = list.lock().unwrap();
    Json(items.clone())
}

#[get("/option/<id>")]
fn get_by_id(id: u64, list: &State<OptionList>) -> Option<Json<Option>> {
    let items = list.lock().unwrap();
    items.iter()
        .find(|item| item.id == id)
        .map(|item| Json(item.clone()))
}

#[post("/option", data = "<item>")]
fn create(item: Json<Option>, list: &State<OptionList>) -> Json<Option> {
    let mut items = list.lock().unwrap();
    items.push(item.clone());
    item
}

#[put("/option/<id>", data = "<item>")]
fn update(id: u64, item: Json<Option>, list: &State<OptionList>) -> Option<Json<Option>> {
    let mut items = list.lock().unwrap();
    items.iter_mut()
        .find(|i| i.id == id)
        .map(|i| {
            *i = item.clone();
            Json(i.clone())
        })
}

#[delete("/option/<id>")]
fn delete(id: u64, list: &State<OptionList>) -> Option<()> {
    let mut items = list.lock().unwrap();
    let pos = items.iter().position(|i| i.id == id)?;
    items.remove(pos);
    Some(())
}

#[launch]
fn rocket() -> _ {
    rocket::build()
        .manage(OptionList::new(Vec::new()))
        .mount("/api", routes![get_all, get_by_id, create, update, delete])
}
