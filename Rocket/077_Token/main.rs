#[macro_use] extern crate rocket;

use rocket::serde::{json::Json, Deserialize, Serialize};
use rocket::State;
use std::sync::Mutex;

#[derive(Serialize, Deserialize, Clone)]
#[serde(crate = "rocket::serde")]
struct Token {
    id: u64,
    name: String,
}

type TokenList = Mutex<Vec<Token>>;

#[get("/token")]
fn get_all(list: &State<TokenList>) -> Json<Vec<Token>> {
    let items = list.lock().unwrap();
    Json(items.clone())
}

#[get("/token/<id>")]
fn get_by_id(id: u64, list: &State<TokenList>) -> Option<Json<Token>> {
    let items = list.lock().unwrap();
    items.iter()
        .find(|item| item.id == id)
        .map(|item| Json(item.clone()))
}

#[post("/token", data = "<item>")]
fn create(item: Json<Token>, list: &State<TokenList>) -> Json<Token> {
    let mut items = list.lock().unwrap();
    items.push(item.clone());
    item
}

#[put("/token/<id>", data = "<item>")]
fn update(id: u64, item: Json<Token>, list: &State<TokenList>) -> Option<Json<Token>> {
    let mut items = list.lock().unwrap();
    items.iter_mut()
        .find(|i| i.id == id)
        .map(|i| {
            *i = item.clone();
            Json(i.clone())
        })
}

#[delete("/token/<id>")]
fn delete(id: u64, list: &State<TokenList>) -> Option<()> {
    let mut items = list.lock().unwrap();
    let pos = items.iter().position(|i| i.id == id)?;
    items.remove(pos);
    Some(())
}

#[launch]
fn rocket() -> _ {
    rocket::build()
        .manage(TokenList::new(Vec::new()))
        .mount("/api", routes![get_all, get_by_id, create, update, delete])
}
