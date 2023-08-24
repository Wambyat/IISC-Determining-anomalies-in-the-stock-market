import time

t = 1692785642
# conver to this format 23 Aug 2023 09:28:20 GMT
print(time.strftime('%a, %d %b %Y %H:%M:%S GMT', time.gmtime(t)))