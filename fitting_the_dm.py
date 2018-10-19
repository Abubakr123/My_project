from scipy import optimize 
from numpy import *
import matplotlib.pyplot as plt
import numpy as np
import sys

#Import the DM file and the pulsar name as first and second arguments
dm_file = sys.argv[1]
psr_name = sys.argv[2]

#Reading the data
Data = np.loadtxt(dm_file)

MJD = Data[:,0]
DM = Data[:,1]
DM_err = Data[:,2]

#The fitting including measurements of uncertunity 
#The covariance matrix, V, for which the square root of the diagonals are
#the estimated standard-deviation for each of the fitted coefficient

p, V = np.polyfit(MJD, DM, deg=1, cov=True)
y = p[1] + p[0] * MJD
print("The slope of the fit line: ", p[0])


print("x_1: {} +/- {}".format(p[0], np.sqrt(V[0][0])))
print("x_2: {} +/- {}".format(p[1], np.sqrt(V[1][1])))

#Calculate the DM1
DM1 = p[1]/365
print("DM1 = ", DM1)


#Plot
plt.figure()
plt.xlabel("Time [MJD]")
plt.ylabel(r"DM [cm$^{-3}$pc]")
plt.title("PSR %s"%psr_name)
plt.errorbar(MJD, DM, yerr=DM_err, fmt='.k',  elinewidth=2,  mfc='k', label="data")
#plt.plot(mjd, piecewise_linear(mjd, *p), color='g', linestyle='dashed', label="fit")
plt.plot(MJD, y , color='g', linestyle='dashed', label="fit")
plt.legend(loc='upper right')
plt.grid(which='both')
plt.savefig("DM_Fitting_%s.png"%psr_name)
plt.show()

