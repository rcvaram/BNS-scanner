from urllib.request import urlopen
from prettytable import PrettyTable

import scapy.all as scapy
from scapy.modules import nmap
import optparse

NMAP_OS_FINGERPRINT_URL = 'https://raw.githubusercontent.com/nmap/nmap/9efe1892/nmap-os-fingerprints'


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
    open('nmap-os-fingerprints', 'wb').write(
        urlopen(NMAP_OS_FINGERPRINT_URL).read())
    scapy.conf.nmap_base = 'nmap-os-fingerprints'
    score, guess = nmap.nmap_fp(ip_addr)
    return {"score": round(score, 2), "guess": guess[0]}


def parse_response(success_list):
    return [
        {
            "ip": success[1].psrc,
            "mac": success[1].hwsrc,
            "os": get_os(success[1].psrc)
        } for success in success_list
    ]


def print_analysis(element_entries):
    result_table = PrettyTable()
    result_table.field_names = ["IP", "MAC Address", "GUESS OPERATING SYSTEM", "SCORE"]
    for element in element_entries:
        result_table.add_row([element["ip"], element['mac'], element['os'].get('guess'), element['os'].get('score')])

    result_table.sortby = "IP"
    print(result_table)


options = get_arguments()

if options.target:
    broadcast_packets = create_packet(options.target)
    success_packets = transmit_packet(broadcast_packets)
    entries = parse_response(success_packets)
    print_analysis(entries)
