import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import csv

if __name__ == '__main__':
    irisdf = pd.read_csv('fullfileserverext4.csv')

    # time range on what time you want the speed
    minRange = 0
    maxRange = 2700
    speedy = irisdf[irisdf['TIME(s)'].between(minRange, maxRange)]

    write = irisdf[(irisdf['T'] == 'W')]
    maxTime = write['TIME(s)'].max()
    minTime = write['TIME(s)'].min()

    # with the given range and measure points on the plot we want to calculate the speed.
    multiplier = 1
    givenRange = np.linspace(0, (int(maxTime)+30), ((int(maxTime)+30)*multiplier))
    df = pd.DataFrame(columns=['Time'])
    for x in givenRange:
        new_row = {'Time': x}
        df = df.append(new_row, ignore_index=True)

    dftest = pd.DataFrame(columns=['MB','MB/s'])


    for x in givenRange:
       df2 = write[write['TIME(s)'].between(x-(0.5/multiplier), x+(0.5/multiplier))]
       new_row = {'MB': (df2['BYTES'].sum(axis=0)/1000000),'MB/s': (df2['BYTES'].sum(axis=0) / (1000000/multiplier))}
       dftest = dftest.append(new_row, ignore_index=True)
    df['MB'] = dftest['MB']
    df['writespeed'] = dftest['MB/s']

    #select the areas you want to color
    first = df[df['Time'].between(0,195)]
    delete1 = df[df['Time'].between(195,2800)]
    # second = df[df['Time'].between(171,339)]
    # delete2 = df[df['Time'].between(337,350)]
    # third = df[df['Time'].between(348,511)]
    # delete3 = df[df['Time'].between(509,522)]
    # fourth = df[df['Time'].between(520,683)]
    # delete4 = df[df['Time'].between(681,695)]
    # fifth = df[df['Time'].between(693,856)]
    # delete5 = df[df['Time'].between(854, 867)]
    # sixth = df[df['Time'].between(865, 1200)]

    ax = first.plot.line(x='Time', y='writespeed', c='blue', label='Allocating speed')
    delete1.plot.line(ax=ax, x='Time', y='writespeed', color="red",  label='Write speed')
    # second.plot.line(ax=ax, x='Time', y='writespeed', color="orange", label='Second')
    # delete2.plot.line(ax=ax, x='Time', y='writespeed', color="red",label='_nolegend_')
    # third.plot.line(ax=ax, x='Time', y='writespeed', color="pink",  label='Third')
    # delete3.plot.line(ax=ax, x='Time', y='writespeed', color="red",label='_nolegend_')
    # fourth.plot.line(ax=ax, x='Time', y='writespeed', color="purple",  label='Fourth')
    # delete4.plot.line(ax=ax, x='Time', y='writespeed', color="red",label='_nolegend_')
    # fifth.plot.line(ax=ax, x='Time', y='writespeed', color="green",  label='Fifth')
    # delete5.plot.line(ax=ax, x='Time', y='writespeed', color="red", label='_nolegend_')
    # sixth.plot.line(ax=ax, x='Time', y='writespeed', color="yellow", label='Sixth')

    ax.set_ylabel("Speed (MB/s)",fontsize=12)
    ax.set_xlabel("Time (seconds)",fontsize=12)

    plt.show()