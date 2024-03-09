library(lcd)
# for degree i, set the correct file path for data
data_csv_file_path <- "C:/Users/hessor/Documents/pcgaussiantesting/CG-Testing/cg_2_50/cg50_2_1_data_200.csv"
truecg_file_path <- "C:/Users/hessor/Documents/pcgaussiantesting/CG-Testing/cg_2_50/cg50_2_1.csv"
sep_file_path <- "C:/Users/hessor/Documents/pcgaussiantesting/CG-Testing/Metrics/cg50_2_1_sep_sets.csv"
# Read the data CSV file into a data frame
data_df <- read.csv(data_csv_file_path)
truecg_df <- read.csv(truecg_file_path)
sep_df <- read.csv(sep_file_path)
# Convert the data frames to a matrix
tgdata <- as.matrix(data_df)
truecg <- as.matrix(truecg_df)
sep <- as.matrix(sep_df)
colnames(truecg) <- as.character(1:50)
rownames(truecg) <- as.character(1:50)

rPvals <- data.frame(
  x = numeric(),
  y = numeric(),
  set = I(list()),
  pval = numeric()
)

for (i in 1:338) {
  # us .isseparated to see if they have a separating set
  clean_set <- gsub("[^0-9, ]", "", sep[i,'sep_set'])
  numbers_as_string <- unlist(strsplit(clean_set, ", "))
  set <- as.numeric(numbers_as_string)
  x <- as.numeric(sep[i,'x'])
  y <- as.numeric(sep[i,'y'])
  pval <- norm.ci.test(cov(tgdata), 200, x+1, y+1, set+1)
  pval <- as.numeric(pval$p.value)
  new_row <- data.frame(x = x, y = y, set = I(list(set)), pval = pval, stringsAsFactors = FALSE)
  rPvals <- rbind(rPvals, new_row)
}
saveRDS(rPvals, "C:/Users/hessor/Documents/pcgaussiantesting/CG-Testing/Metrics/cg50_2_1_rPvals.rds")