#[macro_use] extern crate rocket;

use rocket::serde::{json::Json, Deserialize, Serialize};
use rocket::State;
use std::sync::Mutex;

#[derive(Serialize, Deserialize, Clone)]
#[serde(crate = "rocket::serde")]
struct Balance {
    id: u64,
    name: String,
}

type BalanceList = Mutex<Vec<Balance>>;

#[get("/balance")]
fn get_all(list: &State<BalanceList>) -> Json<Vec<Balance>> {
    let items = list.lock().unwrap();
    Json(items.clone())
}

#[get("/balance/<id>")]
fn get_by_id(id: u64, list: &State<BalanceList>) -> Option<Json<Balance>> {
    let items = list.lock().unwrap();
    items.iter()
        .find(|item| item.id == id)
        .map(|item| Json(item.clone()))
}

#[post("/balance", data = "<item>")]
fn create(item: Json<Balance>, list: &State<BalanceList>) -> Json<Balance> {
    let mut items = list.lock().unwrap();
    items.push(item.clone());
    item
}

#[put("/balance/<id>", data = "<item>")]
fn update(id: u64, item: Json<Balance>, list: &State<BalanceList>) -> Option<Json<Balance>> {
    let mut items = list.lock().unwrap();
    items.iter_mut()
        .find(|i| i.id == id)
        .map(|i| {
            *i = item.clone();
            Json(i.clone())
        })
}

#[delete("/balance/<id>")]
fn delete(id: u64, list: &State<BalanceList>) -> Option<()> {
    let mut items = list.lock().unwrap();
    let pos = items.iter().position(|i| i.id == id)?;
    items.remove(pos);
    Some(())
}

#[launch]
fn rocket() -> _ {
    rocket::build()
        .manage(BalanceList::new(Vec::new()))
        .mount("/api", routes![get_all, get_by_id, create, update, delete])
}
