library(igraph)

getInterval <- function(number, intervalSequence) {
  for (i in 1:length(intervalSequence) - 1) {
    if (number > intervalSequence[i] &&
        number <= intervalSequence[i + 1]) {
      return(i)
    }
  }
  return(-1)
}

createSymetricMat <- function(P, N) {
  rawMat <- matrix(rbinom(P * P, 1, N / (P - 1)), ncol = P)
  rawMat[row(rawMat) >= col(rawMat)] <- 0
  rawMat[lower.tri(rawMat)] = t(rawMat)[lower.tri(rawMat)]
  return(rawMat)
}

createRandomChordlessMat <- function(P, N) {
  chLMatrix <- createSymetricMat(P, N)
  K <- sample(2:P, 1)
  #message("k=",K)
  I <- c(0.999999, seq(P / K, P, by = P / K))
  for (i in 1:P) {
    for (j in 1:P) {
      #if (j > i) {
        if (getInterval(i, I) > getInterval(j, I)) {
          chLMatrix[i, j] <- 0
        }
      #}
    }
  }
  
  return(chLMatrix)
}

writeResults <- function(){
  N_values = c(3)
  P_values = c(50)
  for(n in N_values){
    for(p in P_values){
      for(i in 1:30){
        cg<-createRandomChordlessMat(p,n)
        colnames(cg)<-rownames(cg)<-paste("v",1:p,sep = "")
        write.csv(cg,file=paste("cg",p,"_",n,"_",i,".csv",sep = ""),row.names=FALSE)
      }
    }
  }
}

writeResults()
# for 1-30 cgs 
# for pval = .05 & .5
# for sample = 200 & 2000
# learned_cg =  gaussian_pc(data_i_j_csv)
#   pattern = pat_i_j 
#   complex

# create a data frame of results
#     | sample size | pval | ACC | TRR | TDR | FPR | SHD
# cg1 | 200         | .05
# cg1 | 200         | .5
# cg1 | 2000        | .05
# cg1 | 2000        | .5 
# .
# .
# .