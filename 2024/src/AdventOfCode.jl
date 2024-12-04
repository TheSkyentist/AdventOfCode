module AdventOfCode

    # Packages
    include("julia/download.jl")
    include("julia/solver.jl")

    # Import packages
    using ArgParse
    using .Download
    using .Solver

    export main

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
        if Download.download(day, year)

            # # Run the solver
            Solver.run_day(day)
        
        end
    end
end