#[macro_use] extern crate rocket;

use rocket::serde::{json::Json, Deserialize, Serialize};
use rocket::State;
use std::sync::Mutex;

#[derive(Serialize, Deserialize, Clone)]
#[serde(crate = "rocket::serde")]
struct Transformer {
    id: u64,
    name: String,
}

type TransformerList = Mutex<Vec<Transformer>>;

#[get("/transformer")]
fn get_all(list: &State<TransformerList>) -> Json<Vec<Transformer>> {
    let items = list.lock().unwrap();
    Json(items.clone())
}

#[get("/transformer/<id>")]
fn get_by_id(id: u64, list: &State<TransformerList>) -> Option<Json<Transformer>> {
    let items = list.lock().unwrap();
    items.iter()
        .find(|item| item.id == id)
        .map(|item| Json(item.clone()))
}

#[post("/transformer", data = "<item>")]
fn create(item: Json<Transformer>, list: &State<TransformerList>) -> Json<Transformer> {
    let mut items = list.lock().unwrap();
    items.push(item.clone());
    item
}

#[put("/transformer/<id>", data = "<item>")]
fn update(id: u64, item: Json<Transformer>, list: &State<TransformerList>) -> Option<Json<Transformer>> {
    let mut items = list.lock().unwrap();
    items.iter_mut()
        .find(|i| i.id == id)
        .map(|i| {
            *i = item.clone();
            Json(i.clone())
        })
}

#[delete("/transformer/<id>")]
fn delete(id: u64, list: &State<TransformerList>) -> Option<()> {
    let mut items = list.lock().unwrap();
    let pos = items.iter().position(|i| i.id == id)?;
    items.remove(pos);
    Some(())
}

#[launch]
fn rocket() -> _ {
    rocket::build()
        .manage(TransformerList::new(Vec::new()))
        .mount("/api", routes![get_all, get_by_id, create, update, delete])
}
