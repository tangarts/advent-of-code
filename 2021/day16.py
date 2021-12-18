
# Every packet begins with a standard header:
# the first three bits encode the packet version,
# and the next three bits encode the packet type ID.
# These two values are numbers;
# all numbers encoded in any packet are represented as binary with the most significant bit first.
# For example, a version encoded as the binary sequence 100 represents the number 4.

# Packets with type ID 4 represent a literal value.
# Literal value packets encode a single binary number.
# To do this, the binary number is padded with leading zeroes until its length is a multiple of four bits,
# and then it is broken into groups of four bits.
# Each group is prefixed by a 1 bit except the last group, which is prefixed by a 0 bit.
# These groups of five bits immediately follow the packet header.

from typing import Tuple
from advent_of_code.core import parse_input
from advent_of_code.debug import trace1

day16 = parse_input('data/input16.txt', sep="\n", parser=str, test=False)[0]

test = "8A004A801A8002F478"
test_input = parse_input(test, sep=" ", parser=str)[0]

def hex_to_bin(hexstring) -> str:
    htob = {"0": "0000",
            "1": "0001",
            "2": "0010",
            "3": "0011",
            "4": "0100",
            "5": "0101",
            "6": "0110",
            "7": "0111",
            "8": "1000",
            "9": "1001",
            "A": "1010",
            "B": "1011",
            "C": "1100",
            "D": "1101",
            "E": "1110",
            "F": "1111"}

    return "".join(htob[char] for char in hexstring)


def btoi(binary_string: str) -> int:
    "convert binary string to integer"
    return int(binary_string, 2)

def split_binary_string(binary_string: str) -> Tuple[int, int, str]:
    version = binary_string[:3]
    type_id = binary_string[3:6]
    packet = binary_string[6:]
    return btoi(version), btoi(type_id), packet

def parse_literal(packet: str) -> Tuple[int, str]:
    ""
    subpackets = []
    while packet[0] == "1":
        subpackets.append("".join(packet[1:5]))
        packet = packet[5:]
    subpackets.append(packet[1:5])
    return btoi("".join(subpackets)), packet[5:]

# print(parse_literal("101111111000101000"))

def process_packet(binary_packet: str):
    # binary_packet = hex_to_bin(packet)
    version, type_id, packet = split_binary_string(binary_packet)
    # literal
    if type_id == 4:
        value, packet = parse_literal(packet)
    # operators
    else:
        length_type_id, packet = packet[0], packet[1:]
        if length_type_id == "0":
            length, packet = btoi(packet[:15]), packet[15:]
            subpacket, packet = packet[:length], packet[length:]
            while subpacket:
                subversion, subpacket = process_packet(subpacket)
                version += subversion
        elif length_type_id == "1":
            subpacket_num, packet = btoi(packet[:11]), packet[11:]
            for i in range(subpacket_num):
                #subversion, _ = process_packet(packet[11*i:11*(i+1)])
                subversion, packet = process_packet(packet)
                version += subversion
    print(version, packet)
    return version, packet



# id of 0
# print(process_packet(hex_to_bin("38006F45291200")))
print(process_packet(hex_to_bin("EE00D40C823060")))
# print(process_packet(hex_to_bin("8A004A801A8002F478")))
# print(process_packet(hex_to_bin("620080001611562C8802118E34")))
# print(process_packet(hex_to_bin("C0015000016115A2E0802F182340")))
# print(process_packet(hex_to_bin(day16))) # 871

