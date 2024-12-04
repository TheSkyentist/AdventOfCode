## Advent of Code 2024

These are my solutions for Advent of Code 2024 in Python, Julia, and Rust along with automation for downloading from the website and running all available days.

All of the project dependencies are managed through [pixi](https://pixi.sh/latest/). Once installed, you can run all of the solutions for the released puzzles using `pixi run src/main.sh`. This will run all the solutions where available.

To run a specific solution for a specific day with a specific language, substitute `DAY` for the day in December you want to solve for:
```sh
pixi r python src/main.py DAY # Python
pixi r julia --project="." src/main.jl DAY # Julia
pixi r cargo run -- DAY # Rust
```

