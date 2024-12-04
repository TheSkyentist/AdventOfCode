//! Module for downloading AoC data.

// Modules to use
use reqwest::blocking::Client;

pub fn download(day: u32, year: u32) -> bool {

    // File where data will be stored
    let file: String = format!("data/input{}.rs.txt", day);

    // Check if file exists
    if std::path::Path::new(&file).exists() {
        println!("Rust data for day {} already exists.", day);
        return true;
    }

    // URL to download data from
    let url: String = format!("https://adventofcode.com/{}/day/{}/input", year, day);

    // Get session cookie
    let session: String = std::fs::read_to_string("aoc_2024_session.txt").unwrap();

    // Define Client
    let client = Client::new();

    // Send request
    let response = client.get(&url)
        .header("cookie", format!("session={}", session))
        .send();
    

    match response {
        Ok(r) => {
            // Check if request was successful
            if r.status().is_success() {
                // Write data to file
                std::fs::write(&file, r.text().unwrap()).unwrap();
                println!("Rust data for day {} downloaded successfully.", day);
                return true;
            } else {
                eprintln!("Rust data for day {} not available.", day);
                return false;
            }
        },
        // Otherwise print the error
        Err(e) => {
            eprintln!("Error downloading Rust data for day {}: {}", day, e);
            return false;
        }
    }

}
