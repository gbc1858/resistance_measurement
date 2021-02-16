from func import *
import time
import csv


r_test = BKPrecision2840()

starttime = time.time()
starttime_readable = time.asctime().replace(' ', '_')
timeGap = 0.05     # save every 'timegap' [s]

with open('r_measurement' + '_' + starttime_readable + '.csv', mode='w') as r_file:
    r_writer = csv.writer(r_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    r_writer.writerow(['time', 'measured_r (ohm)'])
    while True:
        current_r = r_test.get_resistance().split(',')[0]
        print(current_r + ' Ohm')
        r_writer.writerow([time.asctime().split(' ')[3], current_r])
        time.sleep(timeGap - ((time.time() - starttime) % timeGap))

