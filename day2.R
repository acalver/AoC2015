library(tidyverse)

data <- read_delim("data/day2.txt", delim = "\n", show_col_types = FALSE, col_names = F) |> 
  separate_wider_delim(cols = X1, delim = "x", names = c("height", "width", "depth")) |> 
  mutate(across(everything(), as.integer))
         
         
rowwise(data) |> 
  mutate(area = 2 * (height * width + width * depth + height * depth),
         slack = min( height * width,  width * depth,   height * depth),
         total = area + slack) |> 
  ungroup() |> 
  summarise(sum(total))

######################## Part 2 ############################

