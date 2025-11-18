#[macro_use] extern crate rocket;

use rocket::serde::{json::Json, Deserialize, Serialize};
use rocket::State;
use std::sync::Mutex;

#[derive(Serialize, Deserialize, Clone)]
#[serde(crate = "rocket::serde")]
struct Refund {
    id: u64,
    name: String,
}

type RefundList = Mutex<Vec<Refund>>;

#[get("/refund")]
fn get_all(list: &State<RefundList>) -> Json<Vec<Refund>> {
    let items = list.lock().unwrap();
    Json(items.clone())
}

#[get("/refund/<id>")]
fn get_by_id(id: u64, list: &State<RefundList>) -> Option<Json<Refund>> {
    let items = list.lock().unwrap();
    items.iter()
        .find(|item| item.id == id)
        .map(|item| Json(item.clone()))
}

#[post("/refund", data = "<item>")]
fn create(item: Json<Refund>, list: &State<RefundList>) -> Json<Refund> {
    let mut items = list.lock().unwrap();
    items.push(item.clone());
    item
}

#[put("/refund/<id>", data = "<item>")]
fn update(id: u64, item: Json<Refund>, list: &State<RefundList>) -> Option<Json<Refund>> {
    let mut items = list.lock().unwrap();
    items.iter_mut()
        .find(|i| i.id == id)
        .map(|i| {
            *i = item.clone();
            Json(i.clone())
        })
}

#[delete("/refund/<id>")]
fn delete(id: u64, list: &State<RefundList>) -> Option<()> {
    let mut items = list.lock().unwrap();
    let pos = items.iter().position(|i| i.id == id)?;
    items.remove(pos);
    Some(())
}

#[launch]
fn rocket() -> _ {
    rocket::build()
        .manage(RefundList::new(Vec::new()))
        .mount("/api", routes![get_all, get_by_id, create, update, delete])
}
