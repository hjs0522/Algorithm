n = int(input())
URLs = []
for _ in range(n):
    URLs.append(input())

for idx,URL in enumerate(URLs):
    port = '<default>'
    path = '<dafault>'
    
    protocol_idx = URL.find('://')
    protocol = URL[:protocol_idx]
    URL = URL[protocol_idx+3:]
    # :이 나온다는건 포트번호가 존재하고 : 이전까지만 호스트이라는 뜻
    host_idx = URL.find(':')
    host = URL
    if host_idx != -1:
        host = URL[:host_idx]
        URL = URL[host_idx+1:]
        port_idx = URL.find('/')
        if port_idx != -1:
            port = URL[:port_idx]
            path = URL[port_idx+1:]
            print('URL #' + str(idx+1))
            print('Protocol = ' + protocol)
            print('Host     = ' + host)
            print('Port     = ' + port)
            print('Path     = ' + path)
            print()
            continue
        
        port = URL
        print('URL #' + str(idx+1))
        print('Protocol = ' + protocol)
        print('Host     = ' + host)
        print('Port     = ' + port)
        print('Path     = ' + path)
        print()
        continue
    
    host_idx = URL.find('/')
    if host_idx != -1:
        host = URL[:host_idx]
        path = URL[host_idx+1:]
       
    print('URL #' + str(idx+1))
    print('Protocol = ' + protocol)
    print('Host     = ' + host)
    print('Port     = ' + port)
    print('Path     = ' + path)
    print()
    