#[macro_use] extern crate rocket;

use rocket::serde::{json::Json, Deserialize, Serialize};
use rocket::State;
use std::sync::Mutex;

#[derive(Serialize, Deserialize, Clone)]
#[serde(crate = "rocket::serde")]
struct Theme {
    id: u64,
    name: String,
}

type ThemeList = Mutex<Vec<Theme>>;

#[get("/theme")]
fn get_all(list: &State<ThemeList>) -> Json<Vec<Theme>> {
    let items = list.lock().unwrap();
    Json(items.clone())
}

#[get("/theme/<id>")]
fn get_by_id(id: u64, list: &State<ThemeList>) -> Option<Json<Theme>> {
    let items = list.lock().unwrap();
    items.iter()
        .find(|item| item.id == id)
        .map(|item| Json(item.clone()))
}

#[post("/theme", data = "<item>")]
fn create(item: Json<Theme>, list: &State<ThemeList>) -> Json<Theme> {
    let mut items = list.lock().unwrap();
    items.push(item.clone());
    item
}

#[put("/theme/<id>", data = "<item>")]
fn update(id: u64, item: Json<Theme>, list: &State<ThemeList>) -> Option<Json<Theme>> {
    let mut items = list.lock().unwrap();
    items.iter_mut()
        .find(|i| i.id == id)
        .map(|i| {
            *i = item.clone();
            Json(i.clone())
        })
}

#[delete("/theme/<id>")]
fn delete(id: u64, list: &State<ThemeList>) -> Option<()> {
    let mut items = list.lock().unwrap();
    let pos = items.iter().position(|i| i.id == id)?;
    items.remove(pos);
    Some(())
}

#[launch]
fn rocket() -> _ {
    rocket::build()
        .manage(ThemeList::new(Vec::new()))
        .mount("/api", routes![get_all, get_by_id, create, update, delete])
}
