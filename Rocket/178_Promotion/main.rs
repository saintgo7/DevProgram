#[macro_use] extern crate rocket;

use rocket::serde::{json::Json, Deserialize, Serialize};
use rocket::State;
use std::sync::Mutex;

#[derive(Serialize, Deserialize, Clone)]
#[serde(crate = "rocket::serde")]
struct Promotion {
    id: u64,
    name: String,
}

type PromotionList = Mutex<Vec<Promotion>>;

#[get("/promotion")]
fn get_all(list: &State<PromotionList>) -> Json<Vec<Promotion>> {
    let items = list.lock().unwrap();
    Json(items.clone())
}

#[get("/promotion/<id>")]
fn get_by_id(id: u64, list: &State<PromotionList>) -> Option<Json<Promotion>> {
    let items = list.lock().unwrap();
    items.iter()
        .find(|item| item.id == id)
        .map(|item| Json(item.clone()))
}

#[post("/promotion", data = "<item>")]
fn create(item: Json<Promotion>, list: &State<PromotionList>) -> Json<Promotion> {
    let mut items = list.lock().unwrap();
    items.push(item.clone());
    item
}

#[put("/promotion/<id>", data = "<item>")]
fn update(id: u64, item: Json<Promotion>, list: &State<PromotionList>) -> Option<Json<Promotion>> {
    let mut items = list.lock().unwrap();
    items.iter_mut()
        .find(|i| i.id == id)
        .map(|i| {
            *i = item.clone();
            Json(i.clone())
        })
}

#[delete("/promotion/<id>")]
fn delete(id: u64, list: &State<PromotionList>) -> Option<()> {
    let mut items = list.lock().unwrap();
    let pos = items.iter().position(|i| i.id == id)?;
    items.remove(pos);
    Some(())
}

#[launch]
fn rocket() -> _ {
    rocket::build()
        .manage(PromotionList::new(Vec::new()))
        .mount("/api", routes![get_all, get_by_id, create, update, delete])
}
