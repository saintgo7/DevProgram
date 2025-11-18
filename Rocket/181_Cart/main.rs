#[macro_use] extern crate rocket;

use rocket::serde::{json::Json, Deserialize, Serialize};
use rocket::State;
use std::sync::Mutex;

#[derive(Serialize, Deserialize, Clone)]
#[serde(crate = "rocket::serde")]
struct Cart {
    id: u64,
    name: String,
}

type CartList = Mutex<Vec<Cart>>;

#[get("/cart")]
fn get_all(list: &State<CartList>) -> Json<Vec<Cart>> {
    let items = list.lock().unwrap();
    Json(items.clone())
}

#[get("/cart/<id>")]
fn get_by_id(id: u64, list: &State<CartList>) -> Option<Json<Cart>> {
    let items = list.lock().unwrap();
    items.iter()
        .find(|item| item.id == id)
        .map(|item| Json(item.clone()))
}

#[post("/cart", data = "<item>")]
fn create(item: Json<Cart>, list: &State<CartList>) -> Json<Cart> {
    let mut items = list.lock().unwrap();
    items.push(item.clone());
    item
}

#[put("/cart/<id>", data = "<item>")]
fn update(id: u64, item: Json<Cart>, list: &State<CartList>) -> Option<Json<Cart>> {
    let mut items = list.lock().unwrap();
    items.iter_mut()
        .find(|i| i.id == id)
        .map(|i| {
            *i = item.clone();
            Json(i.clone())
        })
}

#[delete("/cart/<id>")]
fn delete(id: u64, list: &State<CartList>) -> Option<()> {
    let mut items = list.lock().unwrap();
    let pos = items.iter().position(|i| i.id == id)?;
    items.remove(pos);
    Some(())
}

#[launch]
fn rocket() -> _ {
    rocket::build()
        .manage(CartList::new(Vec::new()))
        .mount("/api", routes![get_all, get_by_id, create, update, delete])
}
