# Import packages
using HTTP

function download(day::Int, year::Int = 2024) :: Nothing
    """
    Download the input for the given day and year
    """

    # Get the input file
    file :: String = "data/input$day.jl.txt"

    # Check if input file already exists
    if isfile(file)
        println("Julia data for day $day already downloaded.")
        return
    end
    
    # Get the URL
    url = "https://adventofcode.com/$year/day/$day/input"

    # Open session cookie from file
    session_cookie :: String = ""
    open("aoc_$(year)_session.txt") do file
        session_cookie = strip(readline(file))
    end

    # Download response
    try
        response = HTTP.get(url, ["cookie" => "session=$session_cookie"])
        open(file, "w") do file
            write(file, String(response.body))
        end
        println("Julia data for day $day downloaded.")
    catch e
        if isa(e, HTTP.StatusError) && e.response.status == 404
            println("Julia data for day $day not available.")
        else
            println("Error downloading Julia data for day $day with error $e.")
        end
    end
end