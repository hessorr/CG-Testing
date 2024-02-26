library(cglearn)

set.seed(100)
p.value <- .5
n <- 4000
is.chaingraph(toy.graph)
toy.graph <- toy.graph
tgdata <- rnorm.cg(n, toy.graph, get.normal.dist(toy.graph))
tgug <- naive.getug.norm(tgdata, p.value)
tg.jtree <- ug.to.jtree(tgug)
tg.pat <- learn.mec.norm(tg.jtree, cov(tgdata), n, p.value, "CG")
comp.skel(skeleton(toy.graph), skeleton(tg.pat))
# check comp.pat and compare the formulas for SHD
scores <- comp.cgs1(pattern(toy.graph), tg.pat)
# shd is correct here. use this code that is more reliable to compute needed metrics. This only has TP and SHD
comp.pat(pattern(toy.graph), tg.pat)

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

print(scores)
curcgscores <- c('current', .05, 200, 2, scores['TPR'], scores['TDR'], scores['FPR'],scores['ACC'], scores['SHD'])
rLearnedScores[nrow(rLearnedScores) + 1,] = c("current", .05, 200, 2, scores['TPR'], scores['TDR'], scores['FPR'],scores['ACC'], scores['SHD'])
rLearnedScores[nrow(rLearnedScores) + 1,] = c("current", .05, 200, 2, scores['TPR'], scores['TDR'], scores['FPR'],scores['ACC'], scores['SHD'])

print(rLearnedScores)
print(colnames(tgdata))
print(rownames(tgdata))