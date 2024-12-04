module Solver

    __precompile__()

    # Include submodules
    include("day1.jl")

    # Use submodules
    using .Day1

    # Export desired functionality
    export run_day

    # Map days to solver functions
    function run_day(day::Int)
        if day == 1
            Day1.solve()
        else
            println("No solution implemented for day $day")
        end
    end

end
