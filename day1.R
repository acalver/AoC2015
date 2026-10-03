library(tidyverse)
conflicted::conflicts_prefer(dplyr::filter)
                            
data <- read_file("data/day1.txt")

data <- str_replace_all(data, "\\(", "1")
data <- str_replace_all(data, "\\)", "-1")
data <- regmatches(data, gregexpr("[-]?\\d", data))[[1]]
data <- as.integer(data)

sum(data)

############ Part 2 ####################

floor = 0
for (i in seq(length(data))) {
  
  floor = floor + data[i]
  
  if (floor < 0) { break}
  
  
}

print(i)