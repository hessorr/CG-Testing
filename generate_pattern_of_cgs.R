library(readr)
library(cglearn)

writeResults <- function(pat, name){
  colnames(pat)<-rownames(pat)<-paste("v",1:50,sep = "")
  write.csv(pat,file=name,row.names=FALSE)
}

# for all both 2 degrees and 3 degrees
for (i in 2:3) {
  # for all 30 cgs with either 2 degree or 3 degree
  for (j in 1:30) {
    if (i == 2) {
      csv_file_path <- paste0("C:/Users/hessor/Documents/pcgaussiantesting/CG-Testing/cg_2_50/cg50_2_", j, ".csv")
      
      # Read the CSV file into a data frame
      df <- read_csv(csv_file_path)
      
      # Convert the data frame to a matrix
      adj_matrix <- as.matrix(df)
      
      # Get the pattern of the adj matrix
      pat <- pattern(adj_matrix)
      
      # Declare name of file
      name <- paste0("C:/Users/hessor/Documents/pcgaussiantesting/CG-Testing/cg_2_50/cg50_2_", j, "_pattern.csv")
      
      # send info to write results
      writeResults(pat, name)
      
    } else if (i == 3) {
      csv_file_path <- paste0("C:/Users/hessor/Documents/pcgaussiantesting/CG-Testing/cg_3_50/cg50_3_", j, ".csv")
      
      # Read the CSV file into a data frame
      df <- read_csv(csv_file_path)
      
      # Convert the data frame to a matrix
      adj_matrix <- as.matrix(df)
      
      # Get the pattern of the adj matrix
      pat <- pattern(adj_matrix)
      
      # Declare name of file
      name <- paste0("C:/Users/hessor/Documents/pcgaussiantesting/CG-Testing/cg_3_50/cg50_3_", j, "_pattern.csv")
      
      # send info to write results
      writeResults(pat, name)
    }
  }
}