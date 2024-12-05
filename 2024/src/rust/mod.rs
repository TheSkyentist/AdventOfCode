pub mod download;
pub mod day1;
// Add more days as needed

pub fn run_day(day: u32) {
    match day {
        1 => day1::solve(),
        // Add more days here
        _ => eprintln!("No Rust solution implemented for day {}", day),
    }
}
