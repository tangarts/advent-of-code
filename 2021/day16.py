
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

from advent_of_code.core import parse_input


day16 = parse_input('data/input16.txt', sep="\n", parser=str, test=False)[0]

test = "8A004A801A8002F478"
test_input = parse_input(test, sep=" ", parser=str)[0]
print(test_input)


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


def bin_to_int(binary_string: str):
    return int(binary_string, 2)


def split_binary_string(binary_string: str):
    version = binary_string[:3]
    type_id = binary_string[3:6]
    packet = binary_string[6:]
    return version, type_id, packet


def process_packet(binary_packet: str, versions=0):
    # binary_packet = hex_to_bin(packet)
    version, type_id, packet = split_binary_string(binary_packet)
    versions += bin_to_int(version)
    # literal
    if bin_to_int(type_id) == 4:
        # parse_literal(packet)
        return packet
    # operator
    length_type_id = packet[0]
    if length_type_id == "0":
        total_subpacket_length = bin_to_int(packet[1:16])
        subpackets = length_type_id, bin_to_int(packet[1:16]), packet[16:16 + total_subpacket_length]
        return subpackets
    elif length_type_id == "1":
        subpacket_length: int = bin_to_int(packet[1:12])
        return length_type_id, subpacket_length, packet[12:12 + subpacket_length * 11]

    # process_packet(packet)
    return ""



assert process_packet(hex_to_bin("38006F45291200"))[1] == 27
print(process_packet(hex_to_bin("EE00D40C823060")))
