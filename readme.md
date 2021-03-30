this repository can convert xlsx data and csv data to CALDAV format ics file.

How to use:

1. python3 csvReader.py/excelReader.py 
2. python3 things_main.py/class_main.py

The original code is downloaded from [gill blog](https://chanjh.com/post/0031/). I modified it to work with python3 and add the csvReader.py and things_main.py, to fullfill my personal need.

If the last thing is 24:00, there will be error, since 24:00 does not exist, and 00:00 is regarded as the next day. For now, I will get rid of the error manually.
