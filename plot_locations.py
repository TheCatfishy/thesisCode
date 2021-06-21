import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import csv

if __name__ == '__main__':
    irisdf = pd.read_csv('WriteExampleExt4.csv')
    #plot locations of each read and write possibly in different colors to show different multiple writes.
    write = irisdf[(irisdf['T'] == 'W')]
    read = irisdf[(irisdf['T'] == 'R')]

    first = read[read['TIME(s)'].between(0,197)]
    delete1 = write[write['TIME(s)'].between(197,697)]
    second = read[read['TIME(s)'].between(197,697)]
    delete2 = write[write['TIME(s)'].between(0,197)]
    # third = irisdf[irisdf['TIME(s)'].between(348,511)]
    # delete3 = irisdf[irisdf['TIME(s)'].between(511,520)]
    # fourth = irisdf[irisdf['TIME(s)'].between(520,683)]
    # delete4 = irisdf[irisdf['TIME(s)'].between(683,693)]
    # fifth = irisdf[irisdf['TIME(s)'].between(693,856)]
    # delete5 = irisdf[irisdf['TIME(s)'].between(856, 865)]
    # sixth = irisdf[irisdf['TIME(s)'].between(865, 1200)]

    ax = delete2.plot.scatter( x='TIME(s)', y='NormSector', color="red", s=2, label='Allocate write')
    first.plot.scatter(ax=ax,x='TIME(s)', y = 'NormSector', color="blue",s=2,label='Allocate read')
    delete1.plot.scatter(ax=ax, x='TIME(s)', y='NormSector', color="red", s=2, label='Write')
    # second.plot.scatter(ax=ax,x='TIME(s)', y = 'NormSector',alpha=0.3, color="blue",s=1,label='Read')
    # third.plot.scatter(ax=ax,x='TIME(s)', y = 'NormSector', color="pink",s=2,label='Third')
    # delete3.plot.scatter(ax=ax,x='TIME(s)', y= 'NormSector', color="red",s=2,label='_nolegend_')
    # fourth.plot.scatter(ax=ax,x='TIME(s)', y= 'NormSector', color="purple",s=2,label='Fourth')
    # delete4.plot.scatter(ax=ax,x='TIME(s)', y= 'NormSector', color="red",s=2,label='_nolegend_')
    # fifth.plot.scatter(ax=ax,x='TIME(s)', y= 'NormSector', color="green",s=2,label='Fifth')
    # delete5.plot.scatter(ax=ax, x='TIME(s)', y='NormSector', color="red", s=2,label='_nolegend_')
    # sixth.plot.scatter(ax=ax, x='TIME(s)', y='NormSector', color="yellow", s=2, label='Sixth')

    ax.set_xlabel("Time (seconds)", fontsize = 12)
    ax.set_ylabel("Location (sector)", fontsize = 12)
    plt.show()