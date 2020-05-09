#!/usr/bin/env python3

import sys
import argparse
import json
import pprint
import ipaddress
try:
    import pyshark
except ImportError:
    print("ERROR: can't import pyshark. pip3 install pyshark", file=sys.stderr)
    sys.exit(1)

def convert_device_id_int(device_id: str):
    old = bytearray.fromhex(device_id)
    new = reversed(old)
    return int(bytearray(new).hex(), 16)

def get_macs(packet):
    """Get the MAC addresses from a PyShark packet.
    Returns (source MAC, destination MAC)
    """
    if "eth" in packet:
        return (packet.eth.src, packet.eth.dst)
    elif "wlan" in packet:
        return (packet.wlan.ta, packet.wlan.addr)
    raise Exception("Cannot find a MAC address.")

parser = argparse.ArgumentParser(
    description=(
        "Decipher Midea's Msmart local binary protocol from "
        "Wireshark / pcap-ng captures"))
parser.add_argument("pcapfile", type=str, help="path to pcapng dump")
# parser.add_argument("--print-headers", action='store_true')
parser.add_argument("--print-raw", action='store_true')
args = parser.parse_args()

cap = pyshark.FileCapture(
    args.pcapfile, display_filter=("tcp && data.len > 0 && data[:2] == 5a5a"))

for packet in cap:
    packet.data.raw_mode = True
    tcp_data = packet.data.data
    tcp_data_bytes = bytearray.fromhex(tcp_data)
    tcp_data_len = int(tcp_data_bytes[4:5].hex(), 16)
    if len(tcp_data_bytes) != tcp_data_len:
        continue
    device_id = tcp_data_bytes[20:26].hex()
    mac_src, mac_dst = get_macs(packet)

    print("\n### {0} => {1} ({2} => {3})".format(
        packet.ip.src, packet.ip.dst, mac_src, mac_dst))
    if (not ipaddress.ip_address(packet.ip.src).is_private
            or not ipaddress.ip_address(packet.ip.dst).is_private):
        print("NOT LOCAL: packet to/from Midea Cloud")
    print("DeviceId: hex: %s int: %d" % (device_id, convert_device_id_int(device_id)))
    
    if args.print_raw:
        print("RAW: %s" % tcp_data)