#[macro_use] extern crate rocket;

use rocket::serde::{json::Json, Deserialize, Serialize};
use rocket::State;
use std::sync::Mutex;

#[derive(Serialize, Deserialize, Clone)]
#[serde(crate = "rocket::serde")]
struct GST {
    id: u64,
    name: String,
}

type GSTList = Mutex<Vec<GST>>;

#[get("/gst")]
fn get_all(list: &State<GSTList>) -> Json<Vec<GST>> {
    let items = list.lock().unwrap();
    Json(items.clone())
}

#[get("/gst/<id>")]
fn get_by_id(id: u64, list: &State<GSTList>) -> Option<Json<GST>> {
    let items = list.lock().unwrap();
    items.iter()
        .find(|item| item.id == id)
        .map(|item| Json(item.clone()))
}

#[post("/gst", data = "<item>")]
fn create(item: Json<GST>, list: &State<GSTList>) -> Json<GST> {
    let mut items = list.lock().unwrap();
    items.push(item.clone());
    item
}

#[put("/gst/<id>", data = "<item>")]
fn update(id: u64, item: Json<GST>, list: &State<GSTList>) -> Option<Json<GST>> {
    let mut items = list.lock().unwrap();
    items.iter_mut()
        .find(|i| i.id == id)
        .map(|i| {
            *i = item.clone();
            Json(i.clone())
        })
}

#[delete("/gst/<id>")]
fn delete(id: u64, list: &State<GSTList>) -> Option<()> {
    let mut items = list.lock().unwrap();
    let pos = items.iter().position(|i| i.id == id)?;
    items.remove(pos);
    Some(())
}

#[launch]
fn rocket() -> _ {
    rocket::build()
        .manage(GSTList::new(Vec::new()))
        .mount("/api", routes![get_all, get_by_id, create, update, delete])
}
