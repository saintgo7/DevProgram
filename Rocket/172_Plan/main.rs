#[macro_use] extern crate rocket;

use rocket::serde::{json::Json, Deserialize, Serialize};
use rocket::State;
use std::sync::Mutex;

#[derive(Serialize, Deserialize, Clone)]
#[serde(crate = "rocket::serde")]
struct Plan {
    id: u64,
    name: String,
}

type PlanList = Mutex<Vec<Plan>>;

#[get("/plan")]
fn get_all(list: &State<PlanList>) -> Json<Vec<Plan>> {
    let items = list.lock().unwrap();
    Json(items.clone())
}

#[get("/plan/<id>")]
fn get_by_id(id: u64, list: &State<PlanList>) -> Option<Json<Plan>> {
    let items = list.lock().unwrap();
    items.iter()
        .find(|item| item.id == id)
        .map(|item| Json(item.clone()))
}

#[post("/plan", data = "<item>")]
fn create(item: Json<Plan>, list: &State<PlanList>) -> Json<Plan> {
    let mut items = list.lock().unwrap();
    items.push(item.clone());
    item
}

#[put("/plan/<id>", data = "<item>")]
fn update(id: u64, item: Json<Plan>, list: &State<PlanList>) -> Option<Json<Plan>> {
    let mut items = list.lock().unwrap();
    items.iter_mut()
        .find(|i| i.id == id)
        .map(|i| {
            *i = item.clone();
            Json(i.clone())
        })
}

#[delete("/plan/<id>")]
fn delete(id: u64, list: &State<PlanList>) -> Option<()> {
    let mut items = list.lock().unwrap();
    let pos = items.iter().position(|i| i.id == id)?;
    items.remove(pos);
    Some(())
}

#[launch]
fn rocket() -> _ {
    rocket::build()
        .manage(PlanList::new(Vec::new()))
        .mount("/api", routes![get_all, get_by_id, create, update, delete])
}
