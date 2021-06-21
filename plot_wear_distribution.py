import pandas as pd
import matplotlib.pyplot as plt

if __name__ == '__main__':
    #depending on how large the data set is 512GB of ram was needed,
    #thus to try and lower the usage, after counting we try and ditch the original dataset
    write = pd.read_csv('smallfileserverext4lo.csv')
    freqCount = write.value_counts()
    write=None

    write2 = pd.read_csv('smallserverf2fsloc.csv')
    freqCount2 = write2.value_counts()
    write2=None

    my_dict = {'EXT4': freqCount, 'F2FS': freqCount2}

    fig, ax = plt.subplots()

    outliers = dict(marker='o', markerfacecolor='red', markersize=5, markeredgecolor='none')
    ax.boxplot(my_dict.values(), vert=False, flierprops=outliers)

    ax.set_yticklabels(my_dict.keys())

    ax.set_xlabel("Count (writes/sector)",fontsize=12)
    ax.set_ylabel("File systems", fontsize=12)

    plt.show()

