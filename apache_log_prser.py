import sys,os,time
import glob


###

def final_report(logfile,in_response):
    count = 0
    for line in logfile:
        split_line = line.split()
        apache_status = split_line[8]
        if  apache_status == in_response:
            #print(line)
            count += 1
    return count
        

####

def read_dir(in_dir,in_response,in_time):
    secs = 60*int(in_time)
    count = 0
    for in_file in glob.glob(in_dir + "/*.log", recursive=True):
        if  (time.time() - os.stat(in_file).st_mtime) < int(secs):
            in_file = open(in_file, 'r')
            log_report = final_report(in_file,in_response)
            in_file.close()
            count += log_report
    return (count)






if __name__ == "__main__":
    if not len(sys.argv) > 3:
        sys.exit(1)
    in_dir = sys.argv[1]    ####Pass log directory as 1st argument
    in_response = sys.argv[2]   ## Pass response code as second argument
    in_time = sys.argv[3]   ### Pass minuutes in 3rd argument

    print(""" 
##############################################################################################################
Usage : apache_log_prser.py <log_path> <response_code> <time_in_mins>
    E.g. : python3 apache_log_prser.py ./apache_logs 300 10
    Assumptions : 
            1. Log file should be in this format :
             127.0.0.1 user-identifier frank [10/Oct/2000:13:55:36 +0000] "GET /apache_pb.gif HTTP/1.0" 200 2326
            2. http_code should exist in 8th column
            3. Use python 3
            4. Logfile structure (It can read any number of log files in a directory recursively)
            5. Pass the time in minutes
            6. Logfiles should be with .log extension
                Example
├── apache_logs
│   ├── logfile01.log
│   ├── logfile02.log
│   └── logfile03.log
└── count_http1.py
################################################################################################################        
    """)

    if os.path.exists(in_dir):
        print("Path exists and is readable")
    else:
        print ("You must specify a valid path to parse")
        sys.exit(1)
    log_status = read_dir(in_dir,in_response,in_time)
    print("In last",in_time, "minutes total http ",in_response," resonse code found in ",in_dir," is : ",log_status)


    
    
