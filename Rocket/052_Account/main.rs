#[macro_use] extern crate rocket;

use rocket::serde::{json::Json, Deserialize, Serialize};
use rocket::State;
use std::sync::Mutex;

#[derive(Serialize, Deserialize, Clone)]
#[serde(crate = "rocket::serde")]
struct Account {
    id: u64,
    name: String,
}

type AccountList = Mutex<Vec<Account>>;

#[get("/account")]
fn get_all(list: &State<AccountList>) -> Json<Vec<Account>> {
    let items = list.lock().unwrap();
    Json(items.clone())
}

#[get("/account/<id>")]
fn get_by_id(id: u64, list: &State<AccountList>) -> Option<Json<Account>> {
    let items = list.lock().unwrap();
    items.iter()
        .find(|item| item.id == id)
        .map(|item| Json(item.clone()))
}

#[post("/account", data = "<item>")]
fn create(item: Json<Account>, list: &State<AccountList>) -> Json<Account> {
    let mut items = list.lock().unwrap();
    items.push(item.clone());
    item
}

#[put("/account/<id>", data = "<item>")]
fn update(id: u64, item: Json<Account>, list: &State<AccountList>) -> Option<Json<Account>> {
    let mut items = list.lock().unwrap();
    items.iter_mut()
        .find(|i| i.id == id)
        .map(|i| {
            *i = item.clone();
            Json(i.clone())
        })
}

#[delete("/account/<id>")]
fn delete(id: u64, list: &State<AccountList>) -> Option<()> {
    let mut items = list.lock().unwrap();
    let pos = items.iter().position(|i| i.id == id)?;
    items.remove(pos);
    Some(())
}

#[launch]
fn rocket() -> _ {
    rocket::build()
        .manage(AccountList::new(Vec::new()))
        .mount("/api", routes![get_all, get_by_id, create, update, delete])
}
