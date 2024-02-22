library(readr)
library(lcd)

writeResults <- function(adj, name){
  colnames(pat)<-rownames(adj)<-paste("v",1:50,sep = "")
  write.csv(pat,file=name,row.names=FALSE)
}
#  Function to calculate preformance metrics
calculateScores <- function(true, learned) {
  # compare the learned pattern to the true pattern
  comp.pat(cgpat, tg.pat)
  
  scores <- c(TPR, TDR, FPR, ACC, SHD)
  
  return(scores)
}

# data frame to add rows to
truthScores <- data.frame(
  name = character(),
  pval = numeric(), 
  samplesize = integer(),  
  degree = integer(), 
  TPR = numeric(),  
  TDR = numeric(),  
  FPR = numeric(),  
  ACC = numeric(),  
  SHD = numeric()
)

for (i in 2:3) {
  for (j in 1:30) {
    for (p in c(.005, .05)) {
      for (n in c(200, 2000)) {
        # for degree i, set the correct file path for data
        data_csv_file_path <- paste0("C:/Users/hessor/Documents/pcgaussiantesting/CG-Testing/cg_", i,"_50/cg50_", i,"_", j, "_data.csv")
        # for degree i, set the correct file path for cg pattern
        pattern_csv_file_path <- paste0("C:/Users/hessor/Documents/pcgaussiantesting/CG-Testing/cg_", i,"_50/cg50_", i,"_", j, "_pattern.csv")
        # Read the data CSV file into a data frame
        data_df <- read_csv(data_csv_file_path)
        # Read the cg pattern CSV file into a data frame
        pattern_df <- read_csv(pattern_csv_file_path)
        # Convert the data frames to a matrix
        tgdata <- as.matrix(data_df)
        cgpat <- as.matrix(pattern_df)
        
        # generate the undirected graph (independence graph)
        tgug <- naive.getug.norm(tgdata, p)
        # triangulate the ug and then create the junction tree
        tg.jtree <- ug.to.jtree(tgug)
        # get the pattern from the junction tree
        tg.pat <- learn.mec.norm(tg.jtree, cov(tgdata), n, p, "CG")
        
        scores <- calculateScores(cgpat, tg.pat)
        
      }
    }
  }
}
