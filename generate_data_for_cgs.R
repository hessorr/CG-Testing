library(readr)
library(lcd)

# for each CG, generate data with tgdata

# for all both 2 degrees and 3 degrees
# for (i in 2:3) {
#   # for all 30 cgs with either 2 degree or 3 degree
#   for (j in 1:30) {
#     if (i == 2) {
#       csv_file_path <- paste0("C:/Users/hessor/Documents/pcgaussiantesting/CG-Testing/cg_2_50/cg50_2_", j, ".csv")
#       
#       # Read the CSV file into a data frame
#       df <- read_csv(csv_file_path)
#       
#       # Convert the data frame to a matrix
#       adj_matrix <- as.matrix(df)
#       
#       
#       # Declare name of file
#       name <- paste0("C:/Users/hessor/Documents/pcgaussiantesting/CG-Testing/cg_2_50/cg50_2_", j, "_data.dat")
#       
#       # send info to write results
#       writeResults(pat, name)
#       
#     } else if (i == 3) {
#       csv_file_path <- paste0("C:/Users/hessor/Documents/pcgaussiantesting/CG-Testing/cg_3_50/cg50_3_", j, ".csv")
#       
#       # Read the CSV file into a data frame
#       df <- read_csv(csv_file_path)
#       
#       # Convert the data frame to a matrix
#       adj_matrix <- as.matrix(df)
#       
#       # Get the pattern of the adj matrix
#       pat <- pattern(adj_matrix)
#       
#       # Declare name of file
#       name <- paste0("C:/Users/hessor/Documents/pcgaussiantesting/CG-Testing/cg_3_50/cg50_3_", j, "_data.dat")
#       
#       # send info to write results
#       writeResults(pat, name)
#     }
#   }
# }

csv_file_path <- paste0("C:/Users/hessor/Documents/pcgaussiantesting/CG-Testing/cg_2_50/cg50_2_1.csv")

# Read the CSV file into a data frame
df <- read_csv(csv_file_path)

# Convert the data frame to a matrix
adj_matrix <- as.matrix(df)

tgdata <- rnorm.cg(200, adj_matrix, get.normal.dist(adj_matrix))
print(class(tgdata))
print(class(adj_matrix))
# to get the type of a var use class()