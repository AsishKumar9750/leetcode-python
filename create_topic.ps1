# create_hashing.ps1

$root = "Hashing"

$topics = @(
    
    "Majority_Element",
    "Two_Sum",
    "Sort_Array_by_Increasing_Frequency",
    "Group_Anagrams",
    "Top_K_Frequent_Elements",
    "Longest_Consecutive_Sequence",
    "Subarray_Sum_Equals_K",
    "Find_All_Duplicates_in_an_Array",
    "Single_Number"
)

# Create Hashing folder if it doesn't exist
if (!(Test-Path $root)) {
    New-Item -ItemType Directory -Path $root | Out-Null
}

foreach ($topic in $topics) {
    $folder = Join-Path $root $topic

    if (!(Test-Path $folder)) {
        New-Item -ItemType Directory -Path $folder | Out-Null
    }

    New-Item -ItemType File -Path (Join-Path $folder "solution.py") -Force | Out-Null
    New-Item -ItemType File -Path (Join-Path $folder "README.md") -Force | Out-Null
}

Write-Host "✅ Hashing topics created successfully!"