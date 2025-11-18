#[macro_use] extern crate rocket;

use rocket::serde::{json::Json, Deserialize, Serialize};
use rocket::State;
use std::sync::Mutex;

#[derive(Serialize, Deserialize, Clone)]
#[serde(crate = "rocket::serde")]
struct Certificate {
    id: u64,
    name: String,
}

type CertificateList = Mutex<Vec<Certificate>>;

#[get("/certificate")]
fn get_all(list: &State<CertificateList>) -> Json<Vec<Certificate>> {
    let items = list.lock().unwrap();
    Json(items.clone())
}

#[get("/certificate/<id>")]
fn get_by_id(id: u64, list: &State<CertificateList>) -> Option<Json<Certificate>> {
    let items = list.lock().unwrap();
    items.iter()
        .find(|item| item.id == id)
        .map(|item| Json(item.clone()))
}

#[post("/certificate", data = "<item>")]
fn create(item: Json<Certificate>, list: &State<CertificateList>) -> Json<Certificate> {
    let mut items = list.lock().unwrap();
    items.push(item.clone());
    item
}

#[put("/certificate/<id>", data = "<item>")]
fn update(id: u64, item: Json<Certificate>, list: &State<CertificateList>) -> Option<Json<Certificate>> {
    let mut items = list.lock().unwrap();
    items.iter_mut()
        .find(|i| i.id == id)
        .map(|i| {
            *i = item.clone();
            Json(i.clone())
        })
}

#[delete("/certificate/<id>")]
fn delete(id: u64, list: &State<CertificateList>) -> Option<()> {
    let mut items = list.lock().unwrap();
    let pos = items.iter().position(|i| i.id == id)?;
    items.remove(pos);
    Some(())
}

#[launch]
fn rocket() -> _ {
    rocket::build()
        .manage(CertificateList::new(Vec::new()))
        .mount("/api", routes![get_all, get_by_id, create, update, delete])
}
