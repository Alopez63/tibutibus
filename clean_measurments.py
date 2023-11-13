import datetime

# Open the measurements log file from bGeigie Nano
log_file  = 'data/bGeigie_measurements_log.csv'
gpsdata = open(log_file)

# Open or Create a file to store records that are Ok as GPS Available
output_dir = 'data'
output_file = 'clean.log' 
# creat a prefix to append to the log file name format yyyymmddhhmm
date_prefix = datetime.datetime.now()
x = date_prefix.strftime("%Y%m%d%H%M%S")
y = output_dir+'/'+x+'_'+output_file

clean_measurments = open(y, "w")
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
