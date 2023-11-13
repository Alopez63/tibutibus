print ("Opening GPS data CSV file")
gpsdata = open('gps.csv')
good_entries = 0
for gpsline in gpsdata:
    # let's print only lines that have a valid GSP Fix. See: https://github.com/Safecast/bGeigieNanoKit/wiki/Operations-Manual#data-log
    # 'A' = Available or OK, 'V' = Void or invalid
    splitted = gpsline.split(",")
    gps_available = splitted[12]
    if gps_available == 'V':
        print(gpsline)
        good_entries = good_entries + 1

print (good_entries)
