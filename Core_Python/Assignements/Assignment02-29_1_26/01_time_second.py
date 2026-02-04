# 1. Convert the time entered in hh,min and sec into seconds.

hour = int(input('Enter the hour: '))
minutes = int(input('Enter the minutes: '))
seconds = int(input('Enter the seconds: '))

Total_sec = (hour * 3600) + (minutes * 60) + seconds

print('Time Converted into seconds: ',Total_sec)




'''
NOTE:
This program converts hours and minutes into seconds using multiplication
and adds them with seconds to get the total time in seconds.
'''