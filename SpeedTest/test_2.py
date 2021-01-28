import os
import matplotlib.pylab as plt
path = os.path.dirname(__file__)



file_stream = open(path+'\\SpeedTest_Vodafone_new_settings.txt', 'r')


time = []
dwnl = []
upl = []
header = True
for row in file_stream:
    if header:
        header = False
        continue
    row = row.split()
    time.append(row[1])
    dwnl.append(float(row[2]))
    upl.append(float(row[3]))

plt.plot(time, dwnl, time, upl)
plt.show()