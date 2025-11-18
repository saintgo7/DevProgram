#[macro_use] extern crate rocket;

use rocket::serde::{json::Json, Deserialize, Serialize};
use rocket::State;
use std::sync::Mutex;

#[derive(Serialize, Deserialize, Clone)]
#[serde(crate = "rocket::serde")]
struct Calendar {
    id: u64,
    name: String,
}

type CalendarList = Mutex<Vec<Calendar>>;

#[get("/calendar")]
fn get_all(list: &State<CalendarList>) -> Json<Vec<Calendar>> {
    let items = list.lock().unwrap();
    Json(items.clone())
}

#[get("/calendar/<id>")]
fn get_by_id(id: u64, list: &State<CalendarList>) -> Option<Json<Calendar>> {
    let items = list.lock().unwrap();
    items.iter()
        .find(|item| item.id == id)
        .map(|item| Json(item.clone()))
}

#[post("/calendar", data = "<item>")]
fn create(item: Json<Calendar>, list: &State<CalendarList>) -> Json<Calendar> {
    let mut items = list.lock().unwrap();
    items.push(item.clone());
    item
}

#[put("/calendar/<id>", data = "<item>")]
fn update(id: u64, item: Json<Calendar>, list: &State<CalendarList>) -> Option<Json<Calendar>> {
    let mut items = list.lock().unwrap();
    items.iter_mut()
        .find(|i| i.id == id)
        .map(|i| {
            *i = item.clone();
            Json(i.clone())
        })
}

#[delete("/calendar/<id>")]
fn delete(id: u64, list: &State<CalendarList>) -> Option<()> {
    let mut items = list.lock().unwrap();
    let pos = items.iter().position(|i| i.id == id)?;
    items.remove(pos);
    Some(())
}

#[launch]
fn rocket() -> _ {
    rocket::build()
        .manage(CalendarList::new(Vec::new()))
        .mount("/api", routes![get_all, get_by_id, create, update, delete])
}
