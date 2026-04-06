import socket #python netwroking library 

ip = input("Enter the IP address: ")

start_port = int(input("Enter start port: "))
end_port = int(input("Enter end port: "))

ports = {20:"FTP Data Transfer",21:"FTP Command Control",22:"SSH",23:"Telnet",25:"SMTP",53:"DNS",80:"HTTP",110:"POP3",143:"IMAP",443:"HTTPS",8000:"Crazy"}

print(f"Scanning {ip} from port {start_port} to {end_port}")
print()
print("----SCAN START----")
print()

open_port_count=0

for port in range(start_port,end_port+1):
    s= socket.socket(socket.AF_INET, socket.SOCK_STREAM) #creates socket object, specifies address family(we are using IPv4 addresses), AF_INET6 for IPv6, specifies type of connection(TCP in this case, SOCK_DGRAM for UDP)
    s.settimeout(1) # when ports dont respond prevent program from hanging 

    result = s.connect_ex((ip,port)) #connect_ex attempts to connect to ip address and port, 0 if success(port open), else non zero error code, if i used only connect instead then program would crash when a port is closed

    if result==0:
        open_port_count = open_port_count+1
        if port in ports:
            print(f"[+] Port {port} ({ports[port]}) is open")
        else:
            print(f"[+] Port {port} is open")

    s.close()
print(f"Total open Ports: {open_port_count}")
print()
print("----SCAN COMPLETE----")