def headers(s):
    headers = {}
    for i in s.split('\n'):
        k,v = i.split(': ')
        headers[k] = v
    return headers
    
def cookies(s):
    cookies = {}
    for i in s.split(';'):
        k,v = i.split("=")
        cookies[k] = v
    return cookies