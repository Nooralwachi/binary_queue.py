# binary_queue.py

Given a file named binary_queue that contains different binaries and their status

binary created_at status

b1 10:05:04 10/15/2020 running

b2 14:05:06 10/15/2020 queued

b3 10:06:04 10/15/2020 running

b4 11:07:24 10/15/2020 succeeded

b5 10:10:11 10/15/2020 failed

b6 13:05:00 10/15/2020 succeeded

b7 11:05:40 10/15/2020 queued

b8 12:05:04 10/15/2020 running

b9 12:04:04 10/15/2020 queued

b10 13:05:24 10/15/2020 failed
 
please update the file by removing the binaries that are completed (succeeded or failed) and moving all the queued binaries to the top of file (sorted by creation time)
