from http.server import HTTPServer,BaseHTTPRequestHandler

content='''<!doctype html>
<html>
    <boby>
        <h1 align="center">TCP/IP LAYER and Protocols</h1> 
       
        

<table border="1px" align="center">
    <tr><th>S.No</th><th>LAYERS</th><th>PROTOCOLS</th></tr>
    <tr><td align="center">01.</td><td align="center">Application Layer</td><td align="center">HTTP,RDP,DNS,SMTP,Telnet,SNMP</td>
    <tr><td align="center">02.</td><td align="center">Transport Layer</td><td align="center">TCP,UDP</td>
    <tr><td align="center">03.</td><td align="center">Internet Layer</td><td align="center">ICMP,IGMP,ARP,IPSec</td>
    <tr><td align="center">04.</td><td align="center">Network Layer</td><td align="center">Ethernet,Token</td>
</table>
<h2 align="right">NAME   : DHINESHKUMAR E</h2>
<h2 align="right">REF.NO : 212224220026</h2>
</boby>
</html>
'''

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Get request received...")
        self.send_response(200) 
        self.send_header("content-type", "text/html")       
        self.end_headers()
        self.wfile.write(content.encode())

print("My webserver is running") 
server_address =('',8008)
httpd = HTTPServer(server_address,MyServer)
httpd.serve_forever()