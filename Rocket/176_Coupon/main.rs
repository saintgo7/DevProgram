#[macro_use] extern crate rocket;

use rocket::serde::{json::Json, Deserialize, Serialize};
use rocket::State;
use std::sync::Mutex;

#[derive(Serialize, Deserialize, Clone)]
#[serde(crate = "rocket::serde")]
struct Coupon {
    id: u64,
    name: String,
}

type CouponList = Mutex<Vec<Coupon>>;

#[get("/coupon")]
fn get_all(list: &State<CouponList>) -> Json<Vec<Coupon>> {
    let items = list.lock().unwrap();
    Json(items.clone())
}

#[get("/coupon/<id>")]
fn get_by_id(id: u64, list: &State<CouponList>) -> Option<Json<Coupon>> {
    let items = list.lock().unwrap();
    items.iter()
        .find(|item| item.id == id)
        .map(|item| Json(item.clone()))
}

#[post("/coupon", data = "<item>")]
fn create(item: Json<Coupon>, list: &State<CouponList>) -> Json<Coupon> {
    let mut items = list.lock().unwrap();
    items.push(item.clone());
    item
}

#[put("/coupon/<id>", data = "<item>")]
fn update(id: u64, item: Json<Coupon>, list: &State<CouponList>) -> Option<Json<Coupon>> {
    let mut items = list.lock().unwrap();
    items.iter_mut()
        .find(|i| i.id == id)
        .map(|i| {
            *i = item.clone();
            Json(i.clone())
        })
}

#[delete("/coupon/<id>")]
fn delete(id: u64, list: &State<CouponList>) -> Option<()> {
    let mut items = list.lock().unwrap();
    let pos = items.iter().position(|i| i.id == id)?;
    items.remove(pos);
    Some(())
}

#[launch]
fn rocket() -> _ {
    rocket::build()
        .manage(CouponList::new(Vec::new()))
        .mount("/api", routes![get_all, get_by_id, create, update, delete])
}
