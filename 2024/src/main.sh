#!/bin/bash

# Calculate the number of days since December 1st in UTC-5
days_since() {
    local year=${1:-2024} # Default year to 2024 if not provided

    # Get the current date and time in UTC-5
    now=$(TZ=UTC-5 date +%Y-%m-%dT%H:%M:%S)
    
    # Get December 1st of the specified year in UTC-5
    dec_1st=$(TZ=UTC-5 date -d "$year-12-01T00:00:00" +%Y-%m-%dT%H:%M:%S)

    # Calculate the difference in days
    diff=$(( ($(date -d "$now" +%s) - $(date -d "$dec_1st" +%s)) / 86400 ))
    echo $((diff + 1)) # Add 1 to include today
}

# Year to calculate days for
YEAR=2024

# Get the number of days since December 1st
DAYS=$(days_since $YEAR)

# Cap at 31
if (( DAYS > 31 )); then
    DAYS=31
fi

# Iterate over the days and perform actions
for (( day=1; day<=DAYS; day++ )); do
    printf "%.0s-" {1..80}
    echo
    echo "Processing Day $day"
    echo

    # Run the scripts
    python src/main.py $day
    echo 
    julia --project="." src/main.jl $day
    echo
    cargo run -- $day
    echo



done
