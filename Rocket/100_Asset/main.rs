#[macro_use] extern crate rocket;

use rocket::serde::{json::Json, Deserialize, Serialize};
use rocket::State;
use std::sync::Mutex;

#[derive(Serialize, Deserialize, Clone)]
#[serde(crate = "rocket::serde")]
struct Asset {
    id: u64,
    name: String,
}

type AssetList = Mutex<Vec<Asset>>;

#[get("/asset")]
fn get_all(list: &State<AssetList>) -> Json<Vec<Asset>> {
    let items = list.lock().unwrap();
    Json(items.clone())
}

#[get("/asset/<id>")]
fn get_by_id(id: u64, list: &State<AssetList>) -> Option<Json<Asset>> {
    let items = list.lock().unwrap();
    items.iter()
        .find(|item| item.id == id)
        .map(|item| Json(item.clone()))
}

#[post("/asset", data = "<item>")]
fn create(item: Json<Asset>, list: &State<AssetList>) -> Json<Asset> {
    let mut items = list.lock().unwrap();
    items.push(item.clone());
    item
}

#[put("/asset/<id>", data = "<item>")]
fn update(id: u64, item: Json<Asset>, list: &State<AssetList>) -> Option<Json<Asset>> {
    let mut items = list.lock().unwrap();
    items.iter_mut()
        .find(|i| i.id == id)
        .map(|i| {
            *i = item.clone();
            Json(i.clone())
        })
}

#[delete("/asset/<id>")]
fn delete(id: u64, list: &State<AssetList>) -> Option<()> {
    let mut items = list.lock().unwrap();
    let pos = items.iter().position(|i| i.id == id)?;
    items.remove(pos);
    Some(())
}

#[launch]
fn rocket() -> _ {
    rocket::build()
        .manage(AssetList::new(Vec::new()))
        .mount("/api", routes![get_all, get_by_id, create, update, delete])
}
