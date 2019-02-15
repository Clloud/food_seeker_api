import multiprocessing

bind = '127.0.0.1:5000'
# daemon = True

workers = multiprocessing.cpu_count() * 2 + 1
x_forwarded_for_header = 'X-FORWARDED-FOR'
