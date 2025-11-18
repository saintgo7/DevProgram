#[macro_use] extern crate rocket;

use rocket::serde::{json::Json, Deserialize, Serialize};
use rocket::State;
use std::sync::Mutex;

#[derive(Serialize, Deserialize, Clone)]
#[serde(crate = "rocket::serde")]
struct Survey {
    id: u64,
    name: String,
}

type SurveyList = Mutex<Vec<Survey>>;

#[get("/survey")]
fn get_all(list: &State<SurveyList>) -> Json<Vec<Survey>> {
    let items = list.lock().unwrap();
    Json(items.clone())
}

#[get("/survey/<id>")]
fn get_by_id(id: u64, list: &State<SurveyList>) -> Option<Json<Survey>> {
    let items = list.lock().unwrap();
    items.iter()
        .find(|item| item.id == id)
        .map(|item| Json(item.clone()))
}

#[post("/survey", data = "<item>")]
fn create(item: Json<Survey>, list: &State<SurveyList>) -> Json<Survey> {
    let mut items = list.lock().unwrap();
    items.push(item.clone());
    item
}

#[put("/survey/<id>", data = "<item>")]
fn update(id: u64, item: Json<Survey>, list: &State<SurveyList>) -> Option<Json<Survey>> {
    let mut items = list.lock().unwrap();
    items.iter_mut()
        .find(|i| i.id == id)
        .map(|i| {
            *i = item.clone();
            Json(i.clone())
        })
}

#[delete("/survey/<id>")]
fn delete(id: u64, list: &State<SurveyList>) -> Option<()> {
    let mut items = list.lock().unwrap();
    let pos = items.iter().position(|i| i.id == id)?;
    items.remove(pos);
    Some(())
}

#[launch]
fn rocket() -> _ {
    rocket::build()
        .manage(SurveyList::new(Vec::new()))
        .mount("/api", routes![get_all, get_by_id, create, update, delete])
}
