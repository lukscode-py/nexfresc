#import nmap3
import nmap3
geral_np = nmap3.Nmap()
geral_tcp_ip = nmap3.NmapScanTechniques()
def scan_portas(host):
    return geral_np.scan_top_ports(host)

def scan_ip(ip):
    return geral_tcp_ip.nmap_tcp_scan(ip)
