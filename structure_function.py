import numpy as np
import matplotlib.pyplot as plt
import sys
import pandas as pd
from pandas import Series
#read the data from dmvals.dat file
name = np.loadtxt('dmvals.dat')
MJD = np.array(name[ :,0])
DM = np.array(name[ :,1])
DM_err = np.array(name[ :,2])


#check the np.interpolation
'''
plt.figure()#(figsize=(13,10))
plt.errorbar(MJD, DM, yerr=DM_err, fmt='*')
interpF = np.interp(np.linspace(56600,60000,1000),MJD,DM)
plt.plot(np.linspace(56600,60000,1000),interpF)
plt.xlim(xmax=58200)
plt.show()

'''

#calculate the structure function and the weights
weights = []
SF = []
SF_err = []
tau =[]
lag = 15
for i in range(len(MJD)):
    i = i+lag
    tau.append(i)
    for j in range(len(MJD)):
        print i, j, i+j
#      while j < len(i):
        w = (DM_err[i+j])**2  + (DM_err[j])**2
        wi = 1/np.array(w)
        weights.append(wi)

        sf = np.sum( ((DM[i+j] - DM[i])**2) * wi)/np.sum(wi)
        SF.append(sf)

        sf_err = (2*np.sqrt(sf))/np.sum(wi)
        SF_err.append(sf_err)

print"SF = ", SF
print"SF_err = ", SF_err

print"SF = ", np.shape(SF)
print"SF_err = ", np.shape(SF_err)



SF = [x for x in SF if str(x) != 'nan']
print"SF", SF


#tdiff =15
#tau =[]
#for i in range(1, len(MJD)+1):
#  tau.append( MJD[i] +i ) # np.arange(1, len(np_clean), tdiff )

l=len(tau)

print len(tau)
print np.shape(SF)
print np.shape(SF_err)

SF=SF[ :l]
SF_err=SF_err[ :l]
z=tau[ :l]  

print SF
print SF_err


#convert the lists to numpy array=======================================================
SF = np.array(SF)
SF_err = np.array(SF_err)

zdiff = 15
z = np.arange(1, len(MJD)+1, zdiff) #start at 1, to avoid error from log(0)
SF = np.arange(1, len(SF)+1)
SF_err = np.arange(1, len(SF_err)+1)

print"tau = ", z

#adjest the result to have the same length
SF=SF[z]
SF_err=SF_err[z]



print"SF = ", SF
print"SF_err = ", SF_err

print np.shape(SF)
print np.shape(SF_err)

#============================================================================

logA = np.log(z) #no need for list comprehension since all z values >= 1
logB = np.log(SF)
print np.shape(logA)
print np.shape(logB)


m, c = np.polyfit(logA, logB, 1) # fit log(y) = m*log(x) + c
y_fit = np.exp(m*logA + c) # calculate the fitted values of y 


#plots
fig=plt.figure()
ax=plt.gca() 
plt.errorbar(z, SF, yerr = SF_err , marker='o', ms=5, ls='dotted', color ='b', label='SF')
plt.plot(z, y_fit, ':', color='r', label="Fitting")
ax.set_xscale('log')
ax.set_yscale('log')
plt.xlabel("Lag [days]")
plt.ylabel(r"SF [DMu$^2$]")
plt.legend(loc='best')
plt.grid(which='both')
ax.set_title('The Structure Function')
plt.savefig("The_Structure_Function.png")
plt.show()


slope, intercept = np.polyfit(logA, logB, 1)
print "the slope , intercept: ", slope, intercept


