from math import prod

from aocd import data as transmission


class PacketDecoder:
    @staticmethod
    def calculate_value(type_id, values):
        if type_id == 0:
            return sum(values)
        elif type_id == 1:
            return prod(values)
        elif type_id == 2:
            return min(values)
        elif type_id == 3:
            return max(values)
        elif type_id == 5:
            return 1 if values[0] > values[1] else 0
        elif type_id == 6:
            return 1 if values[0] < values[1] else 0
        elif type_id == 7:
            return 1 if values[0] == values[1] else 0

    @staticmethod
    def get_binary(transmission):
        return ''.join(format(int(hex_digit, 16), '04b') for hex_digit in transmission)

    def read_packets(self, transmission):
        self.version_sum = 0
        packet = self.get_binary(transmission)
        _, self.value = self._read_packet(packet)

    def _read_packet(self, packet):
        version = int(packet[0:3], 2)
        type_id = int(packet[3:6], 2)
        values = []

        self.version_sum += version

        if type_id == 4:
            bits_read = 6
            groups = zip(*[iter(packet[6:])]*5)
            value = ''
            while groups:
                bits_read += 5
                group = next(groups)
                value += ''.join(group[1:])
                if group[0] == '0':
                    break

            return bits_read, int(value, 2)
        else:
            length_type_id = int(packet[6], 2)
            if length_type_id == 0:
                bit_length = int(packet[7:7+15], 2)
                sub_packets = packet[7+15:7+15+bit_length]
                bits_read = 0
                while bits_read != bit_length:
                    new_bits_read, value = self._read_packet(sub_packets[bits_read:])
                    bits_read += new_bits_read
                    values.append(value)

                value = self.calculate_value(type_id, values)

                return 7 + 15 + bits_read, value
            elif length_type_id == 1:
                n_sub_packets = int(packet[7:7+11], 2)
                bits_read = 0
                for _ in range(n_sub_packets):
                    new_bits_read, value = self._read_packet(packet[7+11+bits_read:])
                    bits_read += new_bits_read
                    values.append(value)

                value = self.calculate_value(type_id, values)

                return 7 + 11 + bits_read, value


pd = PacketDecoder()
pd.read_packets(transmission)
print('Part 1:', pd.version_sum)
print('Part 2:', pd.value)
