#[macro_use] extern crate rocket;

use rocket::serde::{json::Json, Deserialize, Serialize};
use rocket::State;
use std::sync::Mutex;

#[derive(Serialize, Deserialize, Clone)]
#[serde(crate = "rocket::serde")]
struct Category {
    id: u64,
    name: String,
}

type CategoryList = Mutex<Vec<Category>>;

#[get("/category")]
fn get_all(list: &State<CategoryList>) -> Json<Vec<Category>> {
    let items = list.lock().unwrap();
    Json(items.clone())
}

#[get("/category/<id>")]
fn get_by_id(id: u64, list: &State<CategoryList>) -> Option<Json<Category>> {
    let items = list.lock().unwrap();
    items.iter()
        .find(|item| item.id == id)
        .map(|item| Json(item.clone()))
}

#[post("/category", data = "<item>")]
fn create(item: Json<Category>, list: &State<CategoryList>) -> Json<Category> {
    let mut items = list.lock().unwrap();
    items.push(item.clone());
    item
}

#[put("/category/<id>", data = "<item>")]
fn update(id: u64, item: Json<Category>, list: &State<CategoryList>) -> Option<Json<Category>> {
    let mut items = list.lock().unwrap();
    items.iter_mut()
        .find(|i| i.id == id)
        .map(|i| {
            *i = item.clone();
            Json(i.clone())
        })
}

#[delete("/category/<id>")]
fn delete(id: u64, list: &State<CategoryList>) -> Option<()> {
    let mut items = list.lock().unwrap();
    let pos = items.iter().position(|i| i.id == id)?;
    items.remove(pos);
    Some(())
}

#[launch]
fn rocket() -> _ {
    rocket::build()
        .manage(CategoryList::new(Vec::new()))
        .mount("/api", routes![get_all, get_by_id, create, update, delete])
}
