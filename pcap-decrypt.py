#!/usr/bin/env python3
import sys
import argparse
import json
import pprint
import ipaddress
import pyshark
from msmart.lan import lan
from msmart.command import appliance_response
from msmart.security import security


def convert_device_id_int(device_id: str):
    old = bytearray.fromhex(device_id)
    new = reversed(old)
    return int(bytearray(new).hex(), 16)


def get_type(i: int):
    if i == 32:  # 0x20
        return 'get'
    elif i == 34:  # 0x22
        return 'reply'
    elif i == 35:  # 0x23
        return 'set'
    else:
        return 'unknown'


def get_operational_mode(i: int):
    # auto = 1 cool = 2 dry = 3 heat = 4 fan_only = 5
    if i == 1:
        return 'Auto'
    elif i == 2:
        return 'Cool'
    elif i == 3:
        return 'Dry'
    elif i == 4:
        return 'Heat'
    elif i == 5:
        return 'Fan_only'
    else:
        return 'Unknown'


def get_fan_speed(i: int):
    # Auto = 101 102 High = 80 Medium = 60 Low = 40 Silent = 20
    if i == 101 or i == 102:
        return 'Auto'
    elif i == 80:
        return 'High'
    elif i == 60:
        return 'Medium'
    elif i == 40:
        return 'Low'
    elif i == 20:
        return 'Silent'
    else:
        return 'unknown'


parser = argparse.ArgumentParser(
    description=(
        "Decipher Midea's Msmart local binary protocol from "
        "Wireshark / pcap-ng captures"))
parser.add_argument("pcapfile", type=str, help="path to pcapng dump")

parser.add_argument('-f', "--fiter_type", type=str, dest="fiter_type", help='fliter type from midea message',
                    default='all', choices=['all', 'get', 'reply', 'set', 'unknown', 'error'])
parser.add_argument("--tcp-raw", action='store_true')
parser.add_argument("--msg-raw", action='store_true')
args = parser.parse_args()
cap = pyshark.FileCapture(
    args.pcapfile, display_filter=("tcp && data.len == 104 && data[:2] == 5a5a"))

_security = security()

for packet in cap:
    packet.data.raw_mode = True
    tcp_data = packet.data.data
    tcp_data_bytes = bytearray.fromhex(tcp_data)
    tcp_data_len = int(tcp_data_bytes[4:5].hex(), 16)
    if len(tcp_data_bytes) != tcp_data_len:
        continue
    device_id = tcp_data_bytes[20:26].hex()
    midea_data = tcp_data_bytes[40:88]
    reply = _security.aes_decrypt(midea_data)

    msg_type_hex = 255
    msg_type = 'error'

    if len(reply) >= 20:
        msg_type_hex = reply[1]
        msg_type = get_type(msg_type_hex)

    if args.fiter_type != 'all':
        if msg_type != args.fiter_type:
            continue

    print("\n### No.{0} {1} {2} => {3}".format(
        packet.number, packet.sniff_time, packet.ip.src, packet.ip.dst))
    if (not ipaddress.ip_address(packet.ip.src).is_private
            or not ipaddress.ip_address(packet.ip.dst).is_private):
        print("NOT LOCAL: packet to/from Midea Cloud")

    print("Message Type:\t %s %s applianceId: -hex: %s -int: %d" %
          (msg_type.upper(), hex(msg_type_hex), device_id, convert_device_id_int(device_id)))

    if len(reply) >= 20:
        response = appliance_response(reply)
        print("Decoded Data:\t {}".format({
            'power_state': response.power_state,
            'operational_mode': get_operational_mode(response.operational_mode),
            'target_temperature': response.target_temperature,
            'fan_speed': get_fan_speed(response.fan_speed),
            'swing_mode': response.swing_mode,
            'eco_mode': response.eco_mode,
            'turbo_mode': response.turbo_mode,
            'indoor_temperature': response.indoor_temperature,
            'outdoor_temperature': response.outdoor_temperature,
        }))
    else:
         print("Decoded Data:\t Can't Decoded")

    if args.tcp_raw:
        print("TCP RAW:\t %s" % tcp_data)
    if args.msg_raw:
        print("Message RAW:\t %s" % reply.hex())
