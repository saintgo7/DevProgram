#[macro_use] extern crate rocket;

use rocket::serde::{json::Json, Deserialize, Serialize};
use rocket::State;
use std::sync::Mutex;

#[derive(Serialize, Deserialize, Clone)]
#[serde(crate = "rocket::serde")]
struct Appointment {
    id: u64,
    name: String,
}

type AppointmentList = Mutex<Vec<Appointment>>;

#[get("/appointment")]
fn get_all(list: &State<AppointmentList>) -> Json<Vec<Appointment>> {
    let items = list.lock().unwrap();
    Json(items.clone())
}

#[get("/appointment/<id>")]
fn get_by_id(id: u64, list: &State<AppointmentList>) -> Option<Json<Appointment>> {
    let items = list.lock().unwrap();
    items.iter()
        .find(|item| item.id == id)
        .map(|item| Json(item.clone()))
}

#[post("/appointment", data = "<item>")]
fn create(item: Json<Appointment>, list: &State<AppointmentList>) -> Json<Appointment> {
    let mut items = list.lock().unwrap();
    items.push(item.clone());
    item
}

#[put("/appointment/<id>", data = "<item>")]
fn update(id: u64, item: Json<Appointment>, list: &State<AppointmentList>) -> Option<Json<Appointment>> {
    let mut items = list.lock().unwrap();
    items.iter_mut()
        .find(|i| i.id == id)
        .map(|i| {
            *i = item.clone();
            Json(i.clone())
        })
}

#[delete("/appointment/<id>")]
fn delete(id: u64, list: &State<AppointmentList>) -> Option<()> {
    let mut items = list.lock().unwrap();
    let pos = items.iter().position(|i| i.id == id)?;
    items.remove(pos);
    Some(())
}

#[launch]
fn rocket() -> _ {
    rocket::build()
        .manage(AppointmentList::new(Vec::new()))
        .mount("/api", routes![get_all, get_by_id, create, update, delete])
}
