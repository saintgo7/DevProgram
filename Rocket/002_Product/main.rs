#[macro_use] extern crate rocket;

use rocket::serde::{json::Json, Deserialize, Serialize};
use rocket::State;
use std::sync::Mutex;

#[derive(Serialize, Deserialize, Clone)]
#[serde(crate = "rocket::serde")]
struct Product {
    id: u64,
    name: String,
}

type ProductList = Mutex<Vec<Product>>;

#[get("/product")]
fn get_all(list: &State<ProductList>) -> Json<Vec<Product>> {
    let items = list.lock().unwrap();
    Json(items.clone())
}

#[get("/product/<id>")]
fn get_by_id(id: u64, list: &State<ProductList>) -> Option<Json<Product>> {
    let items = list.lock().unwrap();
    items.iter()
        .find(|item| item.id == id)
        .map(|item| Json(item.clone()))
}

#[post("/product", data = "<item>")]
fn create(item: Json<Product>, list: &State<ProductList>) -> Json<Product> {
    let mut items = list.lock().unwrap();
    items.push(item.clone());
    item
}

#[put("/product/<id>", data = "<item>")]
fn update(id: u64, item: Json<Product>, list: &State<ProductList>) -> Option<Json<Product>> {
    let mut items = list.lock().unwrap();
    items.iter_mut()
        .find(|i| i.id == id)
        .map(|i| {
            *i = item.clone();
            Json(i.clone())
        })
}

#[delete("/product/<id>")]
fn delete(id: u64, list: &State<ProductList>) -> Option<()> {
    let mut items = list.lock().unwrap();
    let pos = items.iter().position(|i| i.id == id)?;
    items.remove(pos);
    Some(())
}

#[launch]
fn rocket() -> _ {
    rocket::build()
        .manage(ProductList::new(Vec::new()))
        .mount("/api", routes![get_all, get_by_id, create, update, delete])
}
