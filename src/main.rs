use actix_web::{get, web, App, HttpServer, Responder};

#[get("/")]
async fn index() -> impl Responder {
    "Hello, Rust Web!"
}

#[actix_web::main]
async fn main() -> std::io::Result<()> {
    // Vous pouvez spécifier l'adresse IP et le port à utiliser en tant qu'arguments de ligne de commande
    // ou en utilisant des variables d'environnement pour la configuration dynamique.
    let address = match std::env::var("SERVER_ADDRESS") {
        Ok(val) => val,
        Err(_) => String::from("127.0.0.1:8080"), // Adresse et port par défaut
    };

    HttpServer::new(|| {
        App::new().service(index)
    })
    .bind(address)?
    .run()
    .await
}

