import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import csv

if __name__ == '__main__':
    irisdf = pd.read_csv('Throughputf2fs.csv')

    #time range on what time you want the speed
    minRange = 0
    maxRange = 200
    speedRange = irisdf[irisdf['TIME(s)'].between(minRange, maxRange)]

    writes = speedRange[(speedRange['T'] == 'W')]


    iops = len(speedRange.index)
    maxTime = writes['TIME(s)'].max()
    minTime = writes['TIME(s)'].min()

    #with the given range and measure points on the plot we want to calculate the speed.
    multiplier = 1
    givenRange = np.linspace(0, (int(maxTime)+30), ((int(maxTime)+30)*multiplier))
    df = pd.DataFrame(columns=['Time'])

    for x in givenRange:
        new_row = {'Time': x}
        df = df.append(new_row, ignore_index=True)

    dftest = pd.DataFrame(columns=['MB','MB/s'])

    for x in givenRange:
       df2 = writes[writes['TIME(s)'].between(x-(0.5/multiplier), x+(0.5/multiplier))]
       new_row = {'MB': (df2['BYTES'].sum(axis=0)/1000000),'MB/s': (df2['BYTES'].sum(axis=0) / (1000000/multiplier))}
       dftest = dftest.append(new_row, ignore_index=True)

    df['MB'] = dftest['MB']
    df['writespeed'] = dftest['MB/s']

    print("iops: ", iops)
    print('total written prac: ', writes['BYTES'].sum(axis=0))
    print('total time: ', (maxTime - minTime))
    print("practically written: ", df['MB'].sum(axis=0))
    print("practically MB/s: ", (df['MB'].sum(axis=0)) / (maxTime - minTime))

    ax = df.plot.line(x='Time', y='writespeed', c='red')
    ax.set_xlabel("Time (seconds)",fontsize=12)
    ax.set_ylabel("Speed (MB/s)",fontsize=12)

    plt.show()