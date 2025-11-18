#[macro_use] extern crate rocket;

use rocket::serde::{json::Json, Deserialize, Serialize};
use rocket::State;
use std::sync::Mutex;

#[derive(Serialize, Deserialize, Clone)]
#[serde(crate = "rocket::serde")]
struct SMS {
    id: u64,
    name: String,
}

type SMSList = Mutex<Vec<SMS>>;

#[get("/sms")]
fn get_all(list: &State<SMSList>) -> Json<Vec<SMS>> {
    let items = list.lock().unwrap();
    Json(items.clone())
}

#[get("/sms/<id>")]
fn get_by_id(id: u64, list: &State<SMSList>) -> Option<Json<SMS>> {
    let items = list.lock().unwrap();
    items.iter()
        .find(|item| item.id == id)
        .map(|item| Json(item.clone()))
}

#[post("/sms", data = "<item>")]
fn create(item: Json<SMS>, list: &State<SMSList>) -> Json<SMS> {
    let mut items = list.lock().unwrap();
    items.push(item.clone());
    item
}

#[put("/sms/<id>", data = "<item>")]
fn update(id: u64, item: Json<SMS>, list: &State<SMSList>) -> Option<Json<SMS>> {
    let mut items = list.lock().unwrap();
    items.iter_mut()
        .find(|i| i.id == id)
        .map(|i| {
            *i = item.clone();
            Json(i.clone())
        })
}

#[delete("/sms/<id>")]
fn delete(id: u64, list: &State<SMSList>) -> Option<()> {
    let mut items = list.lock().unwrap();
    let pos = items.iter().position(|i| i.id == id)?;
    items.remove(pos);
    Some(())
}

#[launch]
fn rocket() -> _ {
    rocket::build()
        .manage(SMSList::new(Vec::new()))
        .mount("/api", routes![get_all, get_by_id, create, update, delete])
}
