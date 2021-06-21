import pandas as pd

if __name__ == '__main__':
    irisdf = pd.read_csv('WriteExampleF2FS.csv')
    startSector = 0
    irisdf['NormSector'] = irisdf['SECTOR'] - startSector
    irisdf.to_csv("WriteExampleF2FS.csv", index=False)