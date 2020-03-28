import multiprocessing

workers = multiprocessing.cpu_count() * 2 + 1
timeout = 300
forwarded_allow_ips = '*'
secure_scheme_headers = {'X-Forwarded-Proto': 'https'}
