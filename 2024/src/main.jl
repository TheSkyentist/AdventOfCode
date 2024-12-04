# Packages
using ArgParse
include("julia/download.jl")

# Function to parse arguments
function parse_input()
    parser = ArgParseSettings(description="Advent of Code 2024 in Julia")

    @add_arg_table! parser begin
        "day"
        arg_type = Int
        help = "Day to solve"

        "--year"
        arg_type = Int
        default = 2024
        help = "Year of Advent of Code"
    end

    return parse_args(ARGS, parser)
end

# Function to dynamically load and run the solve function
function main()
    
    # Parse arguments
    args = parse_input()
    day = args["day"]
    year = args["year"]


    # Download data (implement this function as needed)
    download(day, year)

    # Build module file path
    module_path = joinpath("src","julia", "day$day.jl")

    # Check if the file exists
    if !isfile(module_path)
        println("Julia code for day $day not found.")
        return
    end

    # Dynamically include the module
    include("julia/day$day.jl")
    module_name = Symbol("Day")
    solution_module = eval(module_name)

    # Check if the solve function exists
    if !isdefined(solution_module, :solve)
        println("Julia code for day $day does not have a solve function.")
        return
    end

    # Call the solve function using Base.invokelatest
    Base.invokelatest(getfield(solution_module, :solve))
end

# Run the main function
main()
