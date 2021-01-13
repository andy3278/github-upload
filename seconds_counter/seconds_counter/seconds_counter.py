import time 
str_seconds = input("Please enter the number of seconds you wish to convert")
total_secs = int(str_seconds)

if (total_secs // 3600 )< 24 :
    hours = total_secs // 3600
    years = 0 
    days = 0
    secs_still_remaining = total_secs % 3600
    minutes =  secs_still_remaining // 60
    secs_finally_remaining = secs_still_remaining  % 60
elif (total_secs // 31557600 ) <1 :
    years = 0 
    hours = total_secs // 3600
    days = hours // 24 
    secs_still_remaining = total_secs - days * 86400 
    hours = secs_still_remaining // 3600
    secs_still_remaining =  total_secs - days * 86400 - hours * 3600 
    minutes =  secs_still_remaining // 60 
    secs_finally_remaining = secs_still_remaining  % 60
else:
    years = total_secs // 31557600
    days = (total_secs - years * 31557600 ) // 86400
    secs_still_remaining = total_secs - days * 86400 - years * 31557600
    hours = secs_still_remaining // 3600
    secs_still_remaining =  total_secs - days * 86400 - hours * 3600 - years * 31557600
    minutes =  secs_still_remaining // 60 
    secs_finally_remaining = secs_still_remaining  % 60
print("Years=", years, "Days=", days, "Hrs=", hours, "mins=", minutes, "secs=", secs_finally_remaining)
