import pandas as pd
import csv

if __name__ == '__main__':
    irisdf = pd.read_csv('smallwritedeletef2fs.csv')

    write = irisdf[(irisdf['T'] == 'W')]
    WriteLocations = pd.DataFrame(columns=['SECTOR','BYTES'])

    WriteLocations['SECTOR'] = write['SECTOR']
    WriteLocations['BYTES'] = write['BYTES']

    #we want to append the location of each write to a csv file to later plot the wear distribution
    with open('smallwritedeletef2fsloc.csv', mode='a') as employee_file:
        employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        employee_writer.writerow(['Sector'])

        for index, row in WriteLocations.iterrows():
            startSector = row['SECTOR']
            sectorRange = range(int(row['BYTES'] / 512))
            for x in sectorRange:
                employee_writer.writerow([startSector + x])