library(readr)

# for all both 2 degrees and 3 degrees
for (i in 2:3) {
  # for all 30 cgs with either 2 degree or 3 degree
  for (j in 1:30) {
    for (z in c("_pattern","")) {
      # for degree i and cg j, set the correct file path
      csv_file_path <- paste0("C:/Users/hessor/Documents/pcgaussiantesting/CG-Testing/cg_", i,"_50/cg50_", i,"_", j, z, ".csv")
      
      # Read the CSV file into a data frame
      df <- read_csv(csv_file_path)

      # Change the column names of the data frame to 1, 2, 3, ..., 50
      colnames(df) <- as.character(1:50)

      # Overwrite the original CSV file with the modified data frame, without row names
      write.csv(df, csv_file_path, col.names = TRUE, row.names=FALSE)
    }
  }
}