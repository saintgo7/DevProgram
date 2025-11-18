#[macro_use] extern crate rocket;

use rocket::serde::{json::Json, Deserialize, Serialize};
use rocket::State;
use std::sync::Mutex;

#[derive(Serialize, Deserialize, Clone)]
#[serde(crate = "rocket::serde")]
struct SSO {
    id: u64,
    name: String,
}

type SSOList = Mutex<Vec<SSO>>;

#[get("/sso")]
fn get_all(list: &State<SSOList>) -> Json<Vec<SSO>> {
    let items = list.lock().unwrap();
    Json(items.clone())
}

#[get("/sso/<id>")]
fn get_by_id(id: u64, list: &State<SSOList>) -> Option<Json<SSO>> {
    let items = list.lock().unwrap();
    items.iter()
        .find(|item| item.id == id)
        .map(|item| Json(item.clone()))
}

#[post("/sso", data = "<item>")]
fn create(item: Json<SSO>, list: &State<SSOList>) -> Json<SSO> {
    let mut items = list.lock().unwrap();
    items.push(item.clone());
    item
}

#[put("/sso/<id>", data = "<item>")]
fn update(id: u64, item: Json<SSO>, list: &State<SSOList>) -> Option<Json<SSO>> {
    let mut items = list.lock().unwrap();
    items.iter_mut()
        .find(|i| i.id == id)
        .map(|i| {
            *i = item.clone();
            Json(i.clone())
        })
}

#[delete("/sso/<id>")]
fn delete(id: u64, list: &State<SSOList>) -> Option<()> {
    let mut items = list.lock().unwrap();
    let pos = items.iter().position(|i| i.id == id)?;
    items.remove(pos);
    Some(())
}

#[launch]
fn rocket() -> _ {
    rocket::build()
        .manage(SSOList::new(Vec::new()))
        .mount("/api", routes![get_all, get_by_id, create, update, delete])
}
