#[macro_use] extern crate rocket;

use rocket::serde::{json::Json, Deserialize, Serialize};
use rocket::State;
use std::sync::Mutex;

#[derive(Serialize, Deserialize, Clone)]
#[serde(crate = "rocket::serde")]
struct Email {
    id: u64,
    name: String,
}

type EmailList = Mutex<Vec<Email>>;

#[get("/email")]
fn get_all(list: &State<EmailList>) -> Json<Vec<Email>> {
    let items = list.lock().unwrap();
    Json(items.clone())
}

#[get("/email/<id>")]
fn get_by_id(id: u64, list: &State<EmailList>) -> Option<Json<Email>> {
    let items = list.lock().unwrap();
    items.iter()
        .find(|item| item.id == id)
        .map(|item| Json(item.clone()))
}

#[post("/email", data = "<item>")]
fn create(item: Json<Email>, list: &State<EmailList>) -> Json<Email> {
    let mut items = list.lock().unwrap();
    items.push(item.clone());
    item
}

#[put("/email/<id>", data = "<item>")]
fn update(id: u64, item: Json<Email>, list: &State<EmailList>) -> Option<Json<Email>> {
    let mut items = list.lock().unwrap();
    items.iter_mut()
        .find(|i| i.id == id)
        .map(|i| {
            *i = item.clone();
            Json(i.clone())
        })
}

#[delete("/email/<id>")]
fn delete(id: u64, list: &State<EmailList>) -> Option<()> {
    let mut items = list.lock().unwrap();
    let pos = items.iter().position(|i| i.id == id)?;
    items.remove(pos);
    Some(())
}

#[launch]
fn rocket() -> _ {
    rocket::build()
        .manage(EmailList::new(Vec::new()))
        .mount("/api", routes![get_all, get_by_id, create, update, delete])
}
