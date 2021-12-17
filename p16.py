from aocd import submit, data as transmission

# transmission = '8A004A801A8002F478'              # 16 | 16
# transmission = '620080001611562C8802118E34'      # 12 | 12
# transmission = 'C0015000016115A2E0802F182340'    # 23 | 23
# transmission = 'A0016C880162017C3686B18A3D4780'  # 31 | 31

packet = ''.join(format(int(hex_digit, 16), '04b') for hex_digit in transmission)
version_sum = 0

# import pudb;pu.db

def read_packet(packet):
    global version_sum
    version = int(packet[0:3], 2)
    type_id = int(packet[3:6], 2)

    version_sum += version
    packet_length = 6

    if type_id == 4:
        groups = zip(*[iter(packet[6:])]*5)
        value = ''
        while groups:
            packet_length += 5
            group = next(groups)
            value += ''.join(group[1:])
            if group[0] == '0':
                break
        # return int(value, 2), packet_length
        return packet_length
    else:
        length_type_id = int(packet[6], 2)
        if length_type_id == 0:
            bit_length = int(packet[7:7+15], 2)
            sub_packets = packet[7+15:7+15+bit_length]
            bits_read = 0
            while bits_read != bit_length:
                bits_read += read_packet(sub_packets[bits_read:])

            return 7 + 15 + bits_read
        elif length_type_id == 1:
            n_sub_packets = int(packet[7:7+11], 2)
            bits_read = 0
            for _ in range(n_sub_packets):
                packet_length = read_packet(packet[7+11+bits_read:])
                bits_read += packet_length

            return 7 + 11 + bits_read

read_packet(packet)
submit(version_sum)
