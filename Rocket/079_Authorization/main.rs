#[macro_use] extern crate rocket;

use rocket::serde::{json::Json, Deserialize, Serialize};
use rocket::State;
use std::sync::Mutex;

#[derive(Serialize, Deserialize, Clone)]
#[serde(crate = "rocket::serde")]
struct Authorization {
    id: u64,
    name: String,
}

type AuthorizationList = Mutex<Vec<Authorization>>;

#[get("/authorization")]
fn get_all(list: &State<AuthorizationList>) -> Json<Vec<Authorization>> {
    let items = list.lock().unwrap();
    Json(items.clone())
}

#[get("/authorization/<id>")]
fn get_by_id(id: u64, list: &State<AuthorizationList>) -> Option<Json<Authorization>> {
    let items = list.lock().unwrap();
    items.iter()
        .find(|item| item.id == id)
        .map(|item| Json(item.clone()))
}

#[post("/authorization", data = "<item>")]
fn create(item: Json<Authorization>, list: &State<AuthorizationList>) -> Json<Authorization> {
    let mut items = list.lock().unwrap();
    items.push(item.clone());
    item
}

#[put("/authorization/<id>", data = "<item>")]
fn update(id: u64, item: Json<Authorization>, list: &State<AuthorizationList>) -> Option<Json<Authorization>> {
    let mut items = list.lock().unwrap();
    items.iter_mut()
        .find(|i| i.id == id)
        .map(|i| {
            *i = item.clone();
            Json(i.clone())
        })
}

#[delete("/authorization/<id>")]
fn delete(id: u64, list: &State<AuthorizationList>) -> Option<()> {
    let mut items = list.lock().unwrap();
    let pos = items.iter().position(|i| i.id == id)?;
    items.remove(pos);
    Some(())
}

#[launch]
fn rocket() -> _ {
    rocket::build()
        .manage(AuthorizationList::new(Vec::new()))
        .mount("/api", routes![get_all, get_by_id, create, update, delete])
}
