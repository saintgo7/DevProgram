#[macro_use] extern crate rocket;

use rocket::serde::{json::Json, Deserialize, Serialize};
use rocket::State;
use std::sync::Mutex;

#[derive(Serialize, Deserialize, Clone)]
#[serde(crate = "rocket::serde")]
struct Table {
    id: u64,
    name: String,
}

type TableList = Mutex<Vec<Table>>;

#[get("/table")]
fn get_all(list: &State<TableList>) -> Json<Vec<Table>> {
    let items = list.lock().unwrap();
    Json(items.clone())
}

#[get("/table/<id>")]
fn get_by_id(id: u64, list: &State<TableList>) -> Option<Json<Table>> {
    let items = list.lock().unwrap();
    items.iter()
        .find(|item| item.id == id)
        .map(|item| Json(item.clone()))
}

#[post("/table", data = "<item>")]
fn create(item: Json<Table>, list: &State<TableList>) -> Json<Table> {
    let mut items = list.lock().unwrap();
    items.push(item.clone());
    item
}

#[put("/table/<id>", data = "<item>")]
fn update(id: u64, item: Json<Table>, list: &State<TableList>) -> Option<Json<Table>> {
    let mut items = list.lock().unwrap();
    items.iter_mut()
        .find(|i| i.id == id)
        .map(|i| {
            *i = item.clone();
            Json(i.clone())
        })
}

#[delete("/table/<id>")]
fn delete(id: u64, list: &State<TableList>) -> Option<()> {
    let mut items = list.lock().unwrap();
    let pos = items.iter().position(|i| i.id == id)?;
    items.remove(pos);
    Some(())
}

#[launch]
fn rocket() -> _ {
    rocket::build()
        .manage(TableList::new(Vec::new()))
        .mount("/api", routes![get_all, get_by_id, create, update, delete])
}
