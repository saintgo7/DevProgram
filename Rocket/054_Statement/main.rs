#[macro_use] extern crate rocket;

use rocket::serde::{json::Json, Deserialize, Serialize};
use rocket::State;
use std::sync::Mutex;

#[derive(Serialize, Deserialize, Clone)]
#[serde(crate = "rocket::serde")]
struct Statement {
    id: u64,
    name: String,
}

type StatementList = Mutex<Vec<Statement>>;

#[get("/statement")]
fn get_all(list: &State<StatementList>) -> Json<Vec<Statement>> {
    let items = list.lock().unwrap();
    Json(items.clone())
}

#[get("/statement/<id>")]
fn get_by_id(id: u64, list: &State<StatementList>) -> Option<Json<Statement>> {
    let items = list.lock().unwrap();
    items.iter()
        .find(|item| item.id == id)
        .map(|item| Json(item.clone()))
}

#[post("/statement", data = "<item>")]
fn create(item: Json<Statement>, list: &State<StatementList>) -> Json<Statement> {
    let mut items = list.lock().unwrap();
    items.push(item.clone());
    item
}

#[put("/statement/<id>", data = "<item>")]
fn update(id: u64, item: Json<Statement>, list: &State<StatementList>) -> Option<Json<Statement>> {
    let mut items = list.lock().unwrap();
    items.iter_mut()
        .find(|i| i.id == id)
        .map(|i| {
            *i = item.clone();
            Json(i.clone())
        })
}

#[delete("/statement/<id>")]
fn delete(id: u64, list: &State<StatementList>) -> Option<()> {
    let mut items = list.lock().unwrap();
    let pos = items.iter().position(|i| i.id == id)?;
    items.remove(pos);
    Some(())
}

#[launch]
fn rocket() -> _ {
    rocket::build()
        .manage(StatementList::new(Vec::new()))
        .mount("/api", routes![get_all, get_by_id, create, update, delete])
}
