# thesisCode
biosnoop was used to capture the all data.
To plot the read and writes, plot_locations.py was used. This supports multiple areas to change its the colors.
Normalize is used for the small file system partition, to set the beginning location of each write sector on its relative 0 starting point in case multiple partitions are used at the same time.
For write speed, either plot_write_speed.py or plot_multiple_write_speeds.py in case you want to plot speeds with one or multiple colors.
After biosnoop captured all locations, the csv is run through plot_locations.py to create a different csv that just saves all sectors that have been written to.
After this, plot_wear_distribution counts all locations, and plots the wear distribution.
The workloads are mentioned for each test in the paper.
