#[macro_use] extern crate rocket;

use rocket::serde::{json::Json, Deserialize, Serialize};
use rocket::State;
use std::sync::Mutex;

#[derive(Serialize, Deserialize, Clone)]
#[serde(crate = "rocket::serde")]
struct Widget {
    id: u64,
    name: String,
}

type WidgetList = Mutex<Vec<Widget>>;

#[get("/widget")]
fn get_all(list: &State<WidgetList>) -> Json<Vec<Widget>> {
    let items = list.lock().unwrap();
    Json(items.clone())
}

#[get("/widget/<id>")]
fn get_by_id(id: u64, list: &State<WidgetList>) -> Option<Json<Widget>> {
    let items = list.lock().unwrap();
    items.iter()
        .find(|item| item.id == id)
        .map(|item| Json(item.clone()))
}

#[post("/widget", data = "<item>")]
fn create(item: Json<Widget>, list: &State<WidgetList>) -> Json<Widget> {
    let mut items = list.lock().unwrap();
    items.push(item.clone());
    item
}

#[put("/widget/<id>", data = "<item>")]
fn update(id: u64, item: Json<Widget>, list: &State<WidgetList>) -> Option<Json<Widget>> {
    let mut items = list.lock().unwrap();
    items.iter_mut()
        .find(|i| i.id == id)
        .map(|i| {
            *i = item.clone();
            Json(i.clone())
        })
}

#[delete("/widget/<id>")]
fn delete(id: u64, list: &State<WidgetList>) -> Option<()> {
    let mut items = list.lock().unwrap();
    let pos = items.iter().position(|i| i.id == id)?;
    items.remove(pos);
    Some(())
}

#[launch]
fn rocket() -> _ {
    rocket::build()
        .manage(WidgetList::new(Vec::new()))
        .mount("/api", routes![get_all, get_by_id, create, update, delete])
}
