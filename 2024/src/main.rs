mod rust; // Import the `days` module
use rust::download::download; // Expose the `download` function from the `download` module
use rust::run_day; // Expose the `run_day` function from the `days` module


fn main() {
    // Parse command-line arguments
    let args: Vec<String> = std::env::args().collect();
    if args.len() < 2 {
        eprintln!("Usage: {} <day> [--year <year>]", args[0]);
        std::process::exit(1);
    }

    // Get the day
    let day: u32 = args[1].parse().unwrap_or_else(|_| {
        eprintln!("Invalid day: {}", args[1]);
        std::process::exit(1);
    });

    // Get the year (default to 2024 if not provided)
    let mut year = 2024;
    if args.len() > 3 && args[2] == "--year" {
        year = args[3].parse().unwrap_or_else(|_| {
            eprintln!("Invalid year: {}", args[3]);
            std::process::exit(1);
        });
    }

    // Download data
    download(day, year);

    // Run the solution for the specified day
    run_day(day);
}
