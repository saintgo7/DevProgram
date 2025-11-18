#[macro_use] extern crate rocket;

use rocket::serde::{json::Json, Deserialize, Serialize};
use rocket::State;
use std::sync::Mutex;

#[derive(Serialize, Deserialize, Clone)]
#[serde(crate = "rocket::serde")]
struct CreditCard {
    id: u64,
    name: String,
}

type CreditCardList = Mutex<Vec<CreditCard>>;

#[get("/creditcard")]
fn get_all(list: &State<CreditCardList>) -> Json<Vec<CreditCard>> {
    let items = list.lock().unwrap();
    Json(items.clone())
}

#[get("/creditcard/<id>")]
fn get_by_id(id: u64, list: &State<CreditCardList>) -> Option<Json<CreditCard>> {
    let items = list.lock().unwrap();
    items.iter()
        .find(|item| item.id == id)
        .map(|item| Json(item.clone()))
}

#[post("/creditcard", data = "<item>")]
fn create(item: Json<CreditCard>, list: &State<CreditCardList>) -> Json<CreditCard> {
    let mut items = list.lock().unwrap();
    items.push(item.clone());
    item
}

#[put("/creditcard/<id>", data = "<item>")]
fn update(id: u64, item: Json<CreditCard>, list: &State<CreditCardList>) -> Option<Json<CreditCard>> {
    let mut items = list.lock().unwrap();
    items.iter_mut()
        .find(|i| i.id == id)
        .map(|i| {
            *i = item.clone();
            Json(i.clone())
        })
}

#[delete("/creditcard/<id>")]
fn delete(id: u64, list: &State<CreditCardList>) -> Option<()> {
    let mut items = list.lock().unwrap();
    let pos = items.iter().position(|i| i.id == id)?;
    items.remove(pos);
    Some(())
}

#[launch]
fn rocket() -> _ {
    rocket::build()
        .manage(CreditCardList::new(Vec::new()))
        .mount("/api", routes![get_all, get_by_id, create, update, delete])
}
