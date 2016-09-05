#!/usr/bin/python

import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cm as cm
import glob, json, time
from datetime import datetime

D= glob.glob("/home/tabbott/eskom/*.json")
numFiles=np.shape(D)[0]
D.sort()

# start the plot
fig, ax = plt.subplots(nrows=1,ncols=1,figsize=(17,7))  # create figure & 1 axis

colours = [ np.multiply(cm.jet(x),0.9) for x in np.linspace(0.0, 1.0, numFiles) ]

# load all files, plot as we go
for n,fname in enumerate(D):
    #print '  Loading file ',n,', filename ',fname
    with open(fname) as data_file:
        filestamp=int(fname.split('.')[0].split('-')[-1])
        data = json.load(data_file)
        dataarray=np.empty((0,3))
        for d in data:
            dataarray = np.vstack((dataarray,np.array([int(d['Timestamp'][6:-2])/1000,d['Forecast'],d['MaxAvailable']])))
        
        if n==0:
            starttime = np.floor(dataarray[0,0] / 86400.0)     # capture the start time, only on the first file
        dataarray[:,0] = dataarray[:,0] / 86400.0 - starttime
        spaceout=0.08

        # the lines
        ax.plot(dataarray[:,0],dataarray[:,2]/1000-spaceout*(numFiles-n),lw=2,alpha=((n+0.1)/numFiles)**0.5,color=colours[n],label=time.strftime("%d-%m %H:%M", time.localtime(filestamp)) )
        ax.plot(dataarray[:,0],dataarray[:,1]/1000-spaceout*(numFiles-n),lw=2,alpha=((n+0.1)/numFiles)**0.5,color=colours[n])

        # the dots - start of each line
        ax.plot(dataarray[0,0],dataarray[0,2]/1000-spaceout*(numFiles-n),ms=8,alpha=((n+0.1)/numFiles)**0.5,marker='.',color=colours[n])
        ax.plot(dataarray[0,0],dataarray[0,1]/1000-spaceout*(numFiles-n),ms=8,alpha=((n+0.1)/numFiles)**0.5,marker='.',color=colours[n])
        ax.plot(dataarray[-1,0],dataarray[-1,2]/1000-spaceout*(numFiles-n),ms=8,alpha=((n+0.1)/numFiles)**0.5,marker='.',color=colours[n])
        ax.plot(dataarray[-1,0],dataarray[-1,1]/1000-spaceout*(numFiles-n),ms=8,alpha=((n+0.1)/numFiles)**0.5,marker='.',color=colours[n])

ax.grid(True);
ax.legend(loc=0);
ax.set_xlabel('SAST days');
ax.set_ylabel('GW'); 
ax.set_title('Eskom demand and supply curves, plotted on %s from %i files' %  (datetime.now(),numFiles))
start, stop = ax.get_xlim()
ticks = np.arange(np.floor(start), stop+0.5, 0.25)
ax.set_xticks(ticks)


fig.savefig('latestgraph.png', bbox_inches='tight')   # save the figure to file
plt.close(fig)

