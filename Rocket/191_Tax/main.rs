#[macro_use] extern crate rocket;

use rocket::serde::{json::Json, Deserialize, Serialize};
use rocket::State;
use std::sync::Mutex;

#[derive(Serialize, Deserialize, Clone)]
#[serde(crate = "rocket::serde")]
struct Tax {
    id: u64,
    name: String,
}

type TaxList = Mutex<Vec<Tax>>;

#[get("/tax")]
fn get_all(list: &State<TaxList>) -> Json<Vec<Tax>> {
    let items = list.lock().unwrap();
    Json(items.clone())
}

#[get("/tax/<id>")]
fn get_by_id(id: u64, list: &State<TaxList>) -> Option<Json<Tax>> {
    let items = list.lock().unwrap();
    items.iter()
        .find(|item| item.id == id)
        .map(|item| Json(item.clone()))
}

#[post("/tax", data = "<item>")]
fn create(item: Json<Tax>, list: &State<TaxList>) -> Json<Tax> {
    let mut items = list.lock().unwrap();
    items.push(item.clone());
    item
}

#[put("/tax/<id>", data = "<item>")]
fn update(id: u64, item: Json<Tax>, list: &State<TaxList>) -> Option<Json<Tax>> {
    let mut items = list.lock().unwrap();
    items.iter_mut()
        .find(|i| i.id == id)
        .map(|i| {
            *i = item.clone();
            Json(i.clone())
        })
}

#[delete("/tax/<id>")]
fn delete(id: u64, list: &State<TaxList>) -> Option<()> {
    let mut items = list.lock().unwrap();
    let pos = items.iter().position(|i| i.id == id)?;
    items.remove(pos);
    Some(())
}

#[launch]
fn rocket() -> _ {
    rocket::build()
        .manage(TaxList::new(Vec::new()))
        .mount("/api", routes![get_all, get_by_id, create, update, delete])
}
