#[macro_use] extern crate rocket;

use rocket::serde::{json::Json, Deserialize, Serialize};
use rocket::State;
use std::sync::Mutex;

#[derive(Serialize, Deserialize, Clone)]
#[serde(crate = "rocket::serde")]
struct OAuth {
    id: u64,
    name: String,
}

type OAuthList = Mutex<Vec<OAuth>>;

#[get("/oauth")]
fn get_all(list: &State<OAuthList>) -> Json<Vec<OAuth>> {
    let items = list.lock().unwrap();
    Json(items.clone())
}

#[get("/oauth/<id>")]
fn get_by_id(id: u64, list: &State<OAuthList>) -> Option<Json<OAuth>> {
    let items = list.lock().unwrap();
    items.iter()
        .find(|item| item.id == id)
        .map(|item| Json(item.clone()))
}

#[post("/oauth", data = "<item>")]
fn create(item: Json<OAuth>, list: &State<OAuthList>) -> Json<OAuth> {
    let mut items = list.lock().unwrap();
    items.push(item.clone());
    item
}

#[put("/oauth/<id>", data = "<item>")]
fn update(id: u64, item: Json<OAuth>, list: &State<OAuthList>) -> Option<Json<OAuth>> {
    let mut items = list.lock().unwrap();
    items.iter_mut()
        .find(|i| i.id == id)
        .map(|i| {
            *i = item.clone();
            Json(i.clone())
        })
}

#[delete("/oauth/<id>")]
fn delete(id: u64, list: &State<OAuthList>) -> Option<()> {
    let mut items = list.lock().unwrap();
    let pos = items.iter().position(|i| i.id == id)?;
    items.remove(pos);
    Some(())
}

#[launch]
fn rocket() -> _ {
    rocket::build()
        .manage(OAuthList::new(Vec::new()))
        .mount("/api", routes![get_all, get_by_id, create, update, delete])
}
