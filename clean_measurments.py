# Open the measurements log file from bGeigie Nano
log_file  = 'data/bGeigie_measurements_log.csv'
gpsdata = open(log_file)

# Open or Create a file to store records that are Ok as GPS Available
output_file = 'data/clean.log'
clean_measurments = open(output_file, "w")
good_entries = 0
for gpsline in gpsdata:
    # let's print only lines that have a valid GSP Fix. See: https://github.com/Safecast/bGeigieNanoKit/wiki/Operations-Manual#data-log
    # 'A' = Available or OK, 'V' = Void or invalid
    splitted = gpsline.split(",")
    if len(splitted) > 12:
        gps_available = splitted[12]
        if gps_available == 'A':
            print(gpsline)
            clean_measurments.write(gpsline)
            good_entries = good_entries + 1

print (good_entries)