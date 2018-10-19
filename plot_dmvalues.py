import matplotlib.pyplot as plt
import numpy as np
import sys

#Import the DM file and the pulsar name as arguments
dm_file = sys.argv[1]
psr_name = sys.argv[2]

#Read the data file
Data = np.loadtxt(dm_file)

MJD = Data[:,0]
DM = Data[:,1]
DM_err = Data[:,2]



#Plot
plt.figure()
plt.xlabel("Time [MJD]")
plt.ylabel(r"DM [cm$^{-3}$pc]")
plt.title("PSR %s"%psr_name)
plt.errorbar(MJD, DM, yerr=DM_err, fmt='.k',  elinewidth=2,  mfc='k')
plt.grid(which='both')
plt.savefig("DM_%s.png"%psr_name)
plt.show()

