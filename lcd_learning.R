library(readr)
library(cglearn)

# data frame to add rows to
rLearnedScores <- data.frame(
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
        data_csv_file_path <- paste0("C:/Users/hessor/Documents/pcgaussiantesting/CG-Testing/cg_", i,"_50/cg50_", i,"_", j, "_data_", n,".csv")
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
        # set the name of the cg
        name <- paste0("cg50_", i,"_", j)
        # change the cgs column names to match the data's column names, and insert rownames so it plays nice with tg.pat format
        colnames(cgpat) <- as.character(1:50)
        rownames(cgpat) <- as.character(1:50)
        # get the metrics for the performance of the learned cg
        scores <- comp.cgs(cgpat, tg.pat)
        # add the metrics to the scores data frame
        rLearnedScores[nrow(rLearnedScores) + 1,] = c(name, p, n, i, scores['TPR'], scores['TDR'], scores['FPR'],scores['ACC'], scores['SHD'])
      }
    }
  }
}

# after each cg has been learned and the metrics are calculated, save the results into a csv
write.csv(rLearnedScores,file="C:/Users/hessor/Documents/pcgaussiantesting/CG-Testing/Metrics/r_lcd_learned_cg_metrics.csv",row.names=FALSE)
