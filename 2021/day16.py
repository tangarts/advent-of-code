
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

import pytest
from math import prod
from typing import Tuple
from advent_of_code.core import parse_input

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
    packet = packet[5:]
    return btoi("".join(subpackets)), packet

# print(parse_literal("101111111000101000"))


ID = {
    0: sum,
    1: prod,
    2: min,
    3: max,
    5: lambda val: 1 if val[1] > val[2] else 0,
    6: lambda val: 1 if val[1] < val[2] else 0,
    7: lambda val: 1 if val[1] == val[2] else 0,
}



def process_packet(binary_packet: str):
    literal = []
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
                value, subversion, subpacket = process_packet(subpacket)
                print("id 0 with value ", value)
                version += subversion
                # value = ID[type_id](literal)
        elif length_type_id == "1":
            subpacket_num, packet = btoi(packet[:11]), packet[11:]
            for _ in range(subpacket_num):
                value, subversion, packet = process_packet(packet)
                print("id 1 with value ", value)
                version += subversion
                literal.append(value)
                # value = ID[type_id](literal)

    return value, version, packet

def test_packet_sum():
    _, version_sum, _ = process_packet(hex_to_bin("8A004A801A8002F478"))
    assert version_sum == 16
    _, version_sum, _ = process_packet(hex_to_bin("620080001611562C8802118E34"))
    assert version_sum == 12
    _, version_sum, _ = process_packet(hex_to_bin("C0015000016115A2E0802F182340"))
    assert version_sum == 23


# print(process_packet(hex_to_bin(day16)))  # 871
def test_bit_value():
    value, _, _ = process_packet(hex_to_bin("C200B40A82")) 
    assert value == 3
    value, _, _ = process_packet(hex_to_bin("04005AC33890")) 
    assert value == 54
    value, _, _ = process_packet(hex_to_bin("880086C3E88112")) 
    assert value == 7
    value, _, _ = process_packet(hex_to_bin("CE00C43D881120")) 
    assert value == 9
# print(process_packet(hex_to_bin("D8005AC2A8F0")))
# print(process_packet(hex_to_bin("F600BC2D8F")))
print(process_packet(hex_to_bin("9C0141080250320F1802104A08")))
