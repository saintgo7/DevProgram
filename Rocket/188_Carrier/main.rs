#[macro_use] extern crate rocket;

use rocket::serde::{json::Json, Deserialize, Serialize};
use rocket::State;
use std::sync::Mutex;

#[derive(Serialize, Deserialize, Clone)]
#[serde(crate = "rocket::serde")]
struct Carrier {
    id: u64,
    name: String,
}

type CarrierList = Mutex<Vec<Carrier>>;

#[get("/carrier")]
fn get_all(list: &State<CarrierList>) -> Json<Vec<Carrier>> {
    let items = list.lock().unwrap();
    Json(items.clone())
}

#[get("/carrier/<id>")]
fn get_by_id(id: u64, list: &State<CarrierList>) -> Option<Json<Carrier>> {
    let items = list.lock().unwrap();
    items.iter()
        .find(|item| item.id == id)
        .map(|item| Json(item.clone()))
}

#[post("/carrier", data = "<item>")]
fn create(item: Json<Carrier>, list: &State<CarrierList>) -> Json<Carrier> {
    let mut items = list.lock().unwrap();
    items.push(item.clone());
    item
}

#[put("/carrier/<id>", data = "<item>")]
fn update(id: u64, item: Json<Carrier>, list: &State<CarrierList>) -> Option<Json<Carrier>> {
    let mut items = list.lock().unwrap();
    items.iter_mut()
        .find(|i| i.id == id)
        .map(|i| {
            *i = item.clone();
            Json(i.clone())
        })
}

#[delete("/carrier/<id>")]
fn delete(id: u64, list: &State<CarrierList>) -> Option<()> {
    let mut items = list.lock().unwrap();
    let pos = items.iter().position(|i| i.id == id)?;
    items.remove(pos);
    Some(())
}

#[launch]
fn rocket() -> _ {
    rocket::build()
        .manage(CarrierList::new(Vec::new()))
        .mount("/api", routes![get_all, get_by_id, create, update, delete])
}
