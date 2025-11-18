#[macro_use] extern crate rocket;

use rocket::serde::{json::Json, Deserialize, Serialize};
use rocket::State;
use std::sync::Mutex;

#[derive(Serialize, Deserialize, Clone)]
#[serde(crate = "rocket::serde")]
struct Wishlist {
    id: u64,
    name: String,
}

type WishlistList = Mutex<Vec<Wishlist>>;

#[get("/wishlist")]
fn get_all(list: &State<WishlistList>) -> Json<Vec<Wishlist>> {
    let items = list.lock().unwrap();
    Json(items.clone())
}

#[get("/wishlist/<id>")]
fn get_by_id(id: u64, list: &State<WishlistList>) -> Option<Json<Wishlist>> {
    let items = list.lock().unwrap();
    items.iter()
        .find(|item| item.id == id)
        .map(|item| Json(item.clone()))
}

#[post("/wishlist", data = "<item>")]
fn create(item: Json<Wishlist>, list: &State<WishlistList>) -> Json<Wishlist> {
    let mut items = list.lock().unwrap();
    items.push(item.clone());
    item
}

#[put("/wishlist/<id>", data = "<item>")]
fn update(id: u64, item: Json<Wishlist>, list: &State<WishlistList>) -> Option<Json<Wishlist>> {
    let mut items = list.lock().unwrap();
    items.iter_mut()
        .find(|i| i.id == id)
        .map(|i| {
            *i = item.clone();
            Json(i.clone())
        })
}

#[delete("/wishlist/<id>")]
fn delete(id: u64, list: &State<WishlistList>) -> Option<()> {
    let mut items = list.lock().unwrap();
    let pos = items.iter().position(|i| i.id == id)?;
    items.remove(pos);
    Some(())
}

#[launch]
fn rocket() -> _ {
    rocket::build()
        .manage(WishlistList::new(Vec::new()))
        .mount("/api", routes![get_all, get_by_id, create, update, delete])
}
