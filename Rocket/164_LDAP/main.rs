#[macro_use] extern crate rocket;

use rocket::serde::{json::Json, Deserialize, Serialize};
use rocket::State;
use std::sync::Mutex;

#[derive(Serialize, Deserialize, Clone)]
#[serde(crate = "rocket::serde")]
struct LDAP {
    id: u64,
    name: String,
}

type LDAPList = Mutex<Vec<LDAP>>;

#[get("/ldap")]
fn get_all(list: &State<LDAPList>) -> Json<Vec<LDAP>> {
    let items = list.lock().unwrap();
    Json(items.clone())
}

#[get("/ldap/<id>")]
fn get_by_id(id: u64, list: &State<LDAPList>) -> Option<Json<LDAP>> {
    let items = list.lock().unwrap();
    items.iter()
        .find(|item| item.id == id)
        .map(|item| Json(item.clone()))
}

#[post("/ldap", data = "<item>")]
fn create(item: Json<LDAP>, list: &State<LDAPList>) -> Json<LDAP> {
    let mut items = list.lock().unwrap();
    items.push(item.clone());
    item
}

#[put("/ldap/<id>", data = "<item>")]
fn update(id: u64, item: Json<LDAP>, list: &State<LDAPList>) -> Option<Json<LDAP>> {
    let mut items = list.lock().unwrap();
    items.iter_mut()
        .find(|i| i.id == id)
        .map(|i| {
            *i = item.clone();
            Json(i.clone())
        })
}

#[delete("/ldap/<id>")]
fn delete(id: u64, list: &State<LDAPList>) -> Option<()> {
    let mut items = list.lock().unwrap();
    let pos = items.iter().position(|i| i.id == id)?;
    items.remove(pos);
    Some(())
}

#[launch]
fn rocket() -> _ {
    rocket::build()
        .manage(LDAPList::new(Vec::new()))
        .mount("/api", routes![get_all, get_by_id, create, update, delete])
}
