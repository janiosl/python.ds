library(reticulate)
use_python("C:/Python39")
source_python("https://raw.githubusercontent.com/janiosl/python.ds/refs/heads/master/py_poo/pr_work/deost_ad.py")
#('C:/Users/janio/AppData/Local/r-miniconda/envs/r-reticulate/python.exe')

library(daltoolbox)
library(dalevents)
library(harbinger)

model <- hanr_fbiad()


data("gecco")
gecco <- gecco$gecco[16500:18000,]
series <- gecco$ph
reference <- gecco$event

plot(as.ts(series))

ph <- GeraTS(serie=series)
deost <- Evento(s=ph)

#Detection
ev_res <- deost$detector()

#Result organization as harbinger outpu
result <- data.frame(idx = 1:length(series))
result$event <- 0
result$event[deost$ev] <- 1
result$type <- ""
result$type[deost$ev] <- "anomaly"
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
