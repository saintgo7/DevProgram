#[macro_use] extern crate rocket;

use rocket::serde::{json::Json, Deserialize, Serialize};
use rocket::State;
use std::sync::Mutex;

#[derive(Serialize, Deserialize, Clone)]
#[serde(crate = "rocket::serde")]
struct Template {
    id: u64,
    name: String,
}

type TemplateList = Mutex<Vec<Template>>;

#[get("/template")]
fn get_all(list: &State<TemplateList>) -> Json<Vec<Template>> {
    let items = list.lock().unwrap();
    Json(items.clone())
}

#[get("/template/<id>")]
fn get_by_id(id: u64, list: &State<TemplateList>) -> Option<Json<Template>> {
    let items = list.lock().unwrap();
    items.iter()
        .find(|item| item.id == id)
        .map(|item| Json(item.clone()))
}

#[post("/template", data = "<item>")]
fn create(item: Json<Template>, list: &State<TemplateList>) -> Json<Template> {
    let mut items = list.lock().unwrap();
    items.push(item.clone());
    item
}

#[put("/template/<id>", data = "<item>")]
fn update(id: u64, item: Json<Template>, list: &State<TemplateList>) -> Option<Json<Template>> {
    let mut items = list.lock().unwrap();
    items.iter_mut()
        .find(|i| i.id == id)
        .map(|i| {
            *i = item.clone();
            Json(i.clone())
        })
}

#[delete("/template/<id>")]
fn delete(id: u64, list: &State<TemplateList>) -> Option<()> {
    let mut items = list.lock().unwrap();
    let pos = items.iter().position(|i| i.id == id)?;
    items.remove(pos);
    Some(())
}

#[launch]
fn rocket() -> _ {
    rocket::build()
        .manage(TemplateList::new(Vec::new()))
        .mount("/api", routes![get_all, get_by_id, create, update, delete])
}
