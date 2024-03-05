library(readr)
library(cglearn)

# data frame to add rows to
rLearnedScoresStable <- data.frame(
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

# data frame to add rows to
rLearnedScoresOriginal <- data.frame(
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
        # for degree i, set the correct file path for cg pattern
        pattern_csv_file_path <- paste0("C:/Users/hessor/Documents/pcgaussiantesting/CG-Testing/cg_", i,"_50/cg50_", i,"_", j, "_pattern.csv")
        pythonS_csv_file_path <- paste0("C:/Users/hessor/Documents/pcgaussiantesting/CG-Testing/LearnedP/cg50_", i,"_", j, "_learned_", n, "_stable.csv")
        pythonO_csv_file_path <- paste0("C:/Users/hessor/Documents/pcgaussiantesting/CG-Testing/LearnedP/cg50_", i,"_", j, "_learned_", n, "_Original.csv")
        
        # Read the data CSV file into a data frame
        pattern_df <- read_csv(pattern_csv_file_path)
        pythonS_df <- read_csv(pythonS_csv_file_path)
        pythonO_df <- read_csv(pythonO_csv_file_path)
        
        # Convert the data frames to a matrix
        truecgpat <- as.matrix(pattern_df)
        pythonLearnedCGS <- as.matrix(pythonS_df)
        pythonLearnedCGO <- as.matrix(pythonO_df)
        
        # change the cgs column names to match the data's column names, and insert rownames so it plays nice with tg.pat format
        colnames(cgpat) <- as.character(1:50)
        rownames(cgpat) <- as.character(1:50)
        
        # get the metrics for the performance of the learned cg
        scoresS <- comp.cgs1(truecgpat, pythonLearnedCGS)
        scoresO <- comp.cgs1(truecgpat, pythonLearnedCGO)
        # add the metrics to the scores data frame
        rLearnedScoresStable[nrow(rLearnedScoresStable) + 1,] = c(name, p, n, i, scoresS['TPR'], scoresS['TDR'], scoresS['FPR'],scoresS['ACC'], scoresS['SHD'])
        rLearnedScoresOriginal[nrow(rLearnedScoresOriginal) + 1,] = c(name, p, n, i, scoresO['TPR'], scoresO['TDR'], scoresO['FPR'],scoresO['ACC'], scoresO['SHD'])
        
      }
    }
  }
}

# after each cg has been learned and the metrics are calculated, save the results into a csv
write.csv(rLearnedScoresStable,file="C:/Users/hessor/Documents/pcgaussiantesting/CG-Testing/Metrics/python_pc_learned_stable_cg_metrics_testing_rcomp_pat01.csv",row.names=FALSE)

write.csv(rLearnedScoresOriginal,file="C:/Users/hessor/Documents/pcgaussiantesting/CG-Testing/Metrics/python_pc_learned_original_cg_metrics_testing_rcomp_pat01.csv",row.names=FALSE)
