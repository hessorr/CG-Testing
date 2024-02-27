library(readr)
library(lcd)


writeResults <- function(adj, name){
  # colnames(adj)<-rownames(adj)<-paste("v",1:50,sep = "")
  write.csv(adj,file=name,row.names=FALSE)
}

#### For each CG, generate data with tgdata ####

# for all both 2 degrees and 3 degrees
for (i in 2:3) {
  # for all 30 cgs with either 2 degree or 3 degree
  for (j in 1:30) {
    # for sample size 200 and 2000
    for (z in c(200, 2000)) {
        # for degree i and cg j, set the correct file path
        csv_file_path <- paste0("C:/Users/hessor/Documents/pcgaussiantesting/CG-Testing/cg_", i,"_50/cg50_", i,"_", j, ".csv")
        
        # Read the CSV file into a data frame
        df <- read_csv(csv_file_path)
        
        # Convert the data frame to a matrix
        toy.graph <- as.matrix(df)
        tgdata <- rnorm.cg(z, toy.graph, get.normal.dist(toy.graph))
        
        # Declare name of file
        name <- paste0("C:/Users/hessor/Documents/pcgaussiantesting/CG-Testing/cg_", i,"_50/cg50_", i,"_", j, "_data_", z,".csv")
        
        # send info to write results
        writeResults(tgdata, name)
    }
  }
}
