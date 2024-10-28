library(reticulate)
use_python("C:/Python39")
source_python("https://raw.githubusercontent.com/janiosl/python.ds/refs/heads/master/py_poo/pr_work/deost_ad.py")
#('C:/Users/janio/AppData/Local/r-miniconda/envs/r-reticulate/python.exe')

library(daltoolbox)
library(dalevents)
library(harbinger)

#Unused model - Creating just to activate Harbinger evaluation and plot funcions
model <- hanr_fbiad()

#Dataset
data("gecco")
gecco <- gecco$gecco[16500:18000,]
plot(as.ts(gecco[,1:9]))

#Select variable to univariate analysis
series <- gecco$ph
reference <- gecco$event

plot(as.ts(series))

#Create DeoST objects
ph <- GeraTS(serie=series)
deost <- Evento(s=ph)

#Detection
ev_idx <- deost$detect()[[1]]
print(deost)

#Result organization as harbinger output
#Adjust index from Python pattern to R pattern (start from 1 instead of from 0)
ev_idx <- ev_idx+1
n = length(series)

create_harb_res <- function(ev_idx, n){
  result <- data.frame(idx = 1:n)
  result$event <- 0
  result$event[ev_idx] <- 1
  result$type <- ""
  result$type[ev_idx] <- "anomaly"
  return (result)
}

result <- create_harb_res(ev_idx, n)

head(result)
#Evaluate
evaluation <- evaluate(model,
                       result$event,
                       reference)

evaluation$confMatrix
evaluation$accuracy
evaluation$F1

#Visual analysis
grf <- har_plot(model,
                series,
                result,
                reference)

plot(grf)
