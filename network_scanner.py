import scapy.all as scapy
import optparse

from scapy.layers.inet import IP, ICMP

LINUX_TTL = 64


def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-t", "--target", dest="target", help="target IP/ IP range")
    args_options, arguments = parser.parse_args()
    return args_options


def create_packet(ip):
    arp_request = scapy.ARP(pdst=ip)  # create a ARP request object by scapy
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")  # we have set the destination
    arp_request_broadcast = broadcast / arp_request
    return arp_request_broadcast


def transmit_packet(packet):
    success_list, failure_list = scapy.srp(packet, timeout=1)
    return success_list


def get_os(ip_addr):
    ans = scapy.sr1(IP(dst=str(ip_addr)) / ICMP(), timeout=1, verbose=0)
    if not ans:
        return "Not responding, probably Using Firewall"
    if ans.ttl <= LINUX_TTL:
        return "Linux/Unix"
    else:
        return "Windows"


def parse_response(success_list):
    return [
        {
            "ip": success[1].psrc,
            "mac": success[1].hwsrc,
        } for success in success_list
    ]


def print_analysis(element_entries):
    print("IP\t\t\tMAC Address\t\t\tOPERATING SYSTEM")
    print("."*100)
    for element in entries:
        print(element["ip"] + "\t\t" + element['mac'] + "\t\t" + get_os(element["ip"]) + "\n")


options = get_arguments()

if options.target:
    broadcast_packets = create_packet(options.target)
    success_packets = transmit_packet(broadcast_packets)
    entries = parse_response(success_packets)
    print_analysis(entries)
