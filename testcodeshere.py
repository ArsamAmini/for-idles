import time

WINDOW_TIME = 10
MAX_REQUESTS = 5
request_times = {} # this is the dic , 'ip_address' : [89327492,028028408,0138103480,30291481023489]

def rate_limit(ip_address):
    current_time = time.time()
    if ip_address not in request_times:
        request_times[ip_address] = []
        print(request_times)
    request_times[ip_address] = [t for t in request_times[ip_address] if current_time - t < WINDOW_TIME]
    print(request_times)
    if len(request_times[ip_address]) < MAX_REQUESTS:
        request_times[ip_address].append(current_time)
        return False
    else:
        return True

i = 0
while i<10:
    ip = "localhost"
    if rate_limit(ip):
        print("Too much requests")
        i += 1
        time.sleep(4)
    else:
        print("you have access")
        i += 1
        time.sleep(4)
