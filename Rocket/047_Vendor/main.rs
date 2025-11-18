#[macro_use] extern crate rocket;

use rocket::serde::{json::Json, Deserialize, Serialize};
use rocket::State;
use std::sync::Mutex;

#[derive(Serialize, Deserialize, Clone)]
#[serde(crate = "rocket::serde")]
struct Vendor {
    id: u64,
    name: String,
}

type VendorList = Mutex<Vec<Vendor>>;

#[get("/vendor")]
fn get_all(list: &State<VendorList>) -> Json<Vec<Vendor>> {
    let items = list.lock().unwrap();
    Json(items.clone())
}

#[get("/vendor/<id>")]
fn get_by_id(id: u64, list: &State<VendorList>) -> Option<Json<Vendor>> {
    let items = list.lock().unwrap();
    items.iter()
        .find(|item| item.id == id)
        .map(|item| Json(item.clone()))
}

#[post("/vendor", data = "<item>")]
fn create(item: Json<Vendor>, list: &State<VendorList>) -> Json<Vendor> {
    let mut items = list.lock().unwrap();
    items.push(item.clone());
    item
}

#[put("/vendor/<id>", data = "<item>")]
fn update(id: u64, item: Json<Vendor>, list: &State<VendorList>) -> Option<Json<Vendor>> {
    let mut items = list.lock().unwrap();
    items.iter_mut()
        .find(|i| i.id == id)
        .map(|i| {
            *i = item.clone();
            Json(i.clone())
        })
}

#[delete("/vendor/<id>")]
fn delete(id: u64, list: &State<VendorList>) -> Option<()> {
    let mut items = list.lock().unwrap();
    let pos = items.iter().position(|i| i.id == id)?;
    items.remove(pos);
    Some(())
}

#[launch]
fn rocket() -> _ {
    rocket::build()
        .manage(VendorList::new(Vec::new()))
        .mount("/api", routes![get_all, get_by_id, create, update, delete])
}
