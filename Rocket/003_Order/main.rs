#[macro_use] extern crate rocket;

use rocket::serde::{json::Json, Deserialize, Serialize};
use rocket::State;
use std::sync::Mutex;

#[derive(Serialize, Deserialize, Clone)]
#[serde(crate = "rocket::serde")]
struct Order {
    id: u64,
    name: String,
}

type OrderList = Mutex<Vec<Order>>;

#[get("/order")]
fn get_all(list: &State<OrderList>) -> Json<Vec<Order>> {
    let items = list.lock().unwrap();
    Json(items.clone())
}

#[get("/order/<id>")]
fn get_by_id(id: u64, list: &State<OrderList>) -> Option<Json<Order>> {
    let items = list.lock().unwrap();
    items.iter()
        .find(|item| item.id == id)
        .map(|item| Json(item.clone()))
}

#[post("/order", data = "<item>")]
fn create(item: Json<Order>, list: &State<OrderList>) -> Json<Order> {
    let mut items = list.lock().unwrap();
    items.push(item.clone());
    item
}

#[put("/order/<id>", data = "<item>")]
fn update(id: u64, item: Json<Order>, list: &State<OrderList>) -> Option<Json<Order>> {
    let mut items = list.lock().unwrap();
    items.iter_mut()
        .find(|i| i.id == id)
        .map(|i| {
            *i = item.clone();
            Json(i.clone())
        })
}

#[delete("/order/<id>")]
fn delete(id: u64, list: &State<OrderList>) -> Option<()> {
    let mut items = list.lock().unwrap();
    let pos = items.iter().position(|i| i.id == id)?;
    items.remove(pos);
    Some(())
}

#[launch]
fn rocket() -> _ {
    rocket::build()
        .manage(OrderList::new(Vec::new()))
        .mount("/api", routes![get_all, get_by_id, create, update, delete])
}
