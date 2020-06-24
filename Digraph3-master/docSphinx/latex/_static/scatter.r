# scatter plot RB April 2008
test.mat <- matrix(scan("compolg.prn"),ncol=7,byrow=T)
lim1 <- max(test.mat)
lim2 <- min(test.mat)
choose12<-c(1,2)
choose23<-c(2,3)
choose13<-c(1,3)
choose21<-c(2,1)
test.labels <- scan("criteriaLabels.prn",what="character")
valprop <- matrix(scan("val_prlg.prn"),ncol=2,byrow=T)
pdf("/tmp/tmp1z82x9ni/similarityPlot-officeChoice.pdf",width=6,height=6,bg="cornsilk",title="PCA of Criteria Correlation Index")
par(mfrow=c(2,2))
plot(test.mat[,choose12],xlab=paste("axis 1:",valprop[choose12,2][1]*100,"%"),ylab=paste("axis 2:",valprop[choose12,2][2]*100,"%"),type="n",asp=1)
abline(h=0,v=0,col="grey",lty="dotted")
title(sub=paste("total inertia:",(valprop[choose12,2][1]+valprop[choose12,2][2])*100,"%"),main="factors 1 and 2",col="blue")
text(test.mat[,choose12],labels=test.labels,col="red3",cex=1.0)
plot(test.mat[,choose12],xlab=paste("axis 2:",valprop[choose23,2][1]*100,"%"),ylab=paste("axis 3:",valprop[choose23,2][2]*100,"%"),type="n",asp=1)
abline(h=0,v=0,col="grey",lty="dotted")
title(sub=paste("total inertia:",(valprop[choose23,2][1]+valprop[choose23,2][2])*100,"%"),main="factors 2 and 3",col="blue")
text(test.mat[,choose23],labels=test.labels,col="red3",cex=1.0)
plot(test.mat[,choose12],xlab=paste("axis 1:",valprop[choose13,2][1]*100,"%"),ylab=paste("axis 3:",valprop[choose13,2][2]*100,"%"),type="n",asp=1)
abline(h=0,v=0,col="grey",lty="dotted")
title(sub=paste("total inertia:",(valprop[choose13,2][1]+valprop[choose13,2][2])*100,"%"),main="factors 1 and 3",col="blue")
text(test.mat[,choose13],labels=test.labels,col="red3",cex=1.0)
barplot(valprop[1:nrow(valprop)-1,2]*100,names.arg=c(1:6),main="Axis inertia (in %)",col="orangered")
dev.off()
