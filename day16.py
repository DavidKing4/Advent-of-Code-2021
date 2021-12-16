f = open("input16.txt")
data = f.read()[:-1]


class BITS:
    binary: str
    data_len: int
    pc: int

    def __init__(self, data_stream) -> None:
        self.data_len = 4 * len(data_stream)
        spec = f"#0{self.data_len + 2}b"
        self.binary = format(int(data_stream, 16), spec)[2:]
        self.pc = 0

    def read_n(self, n):
        data = self.binary[self.pc : self.pc + n]
        self.pc += n
        return data

    def read_packet(self):
        version = int(self.read_n(3), 2)
        type_id = int(self.read_n(3), 2)
        match type_id:
            case 4:
                literal = ""
                while self.read_n(1) == "1":
                    literal += self.read_n(4)
                literal += self.read_n(4)
                literal = int(literal, 2)
                return [(version, type_id, literal)]
            case _:
                len_type_id = self.read_n(1)
                packets = []
                if len_type_id == "0":
                    t = self.read_n(15)
                    len_sub_packets = int(t, 2)
                    pc_start = self.pc
                    while self.pc - pc_start < len_sub_packets - 1:
                        packets.append(self.read_packet())
                elif len_type_id == "1":
                    no_sub_packets = int(self.read_n(11), 2)
                    for _ in range(no_sub_packets):
                        packets.append(self.read_packet())
                match type_id:
                    case 0:
                        val = 0
                        for x in packets:
                            val += x[0][2]
                    case 1:
                        val = 1
                        for x in packets:
                            val *= x[0][2]
                    case 2:
                        val = min([x[0][2] for x in packets])
                    case 3:
                        val = max([x[0][2] for x in packets])
                    case 5:
                        val = 1 if packets[0][0][2] > packets[1][0][2] else 0
                    case 6:
                        val = 1 if packets[0][0][2] < packets[1][0][2] else 0
                    case 7:
                        val = 1 if packets[0][0][2] == packets[1][0][2] else 0
                    case _:
                        raise ValueError(f"type_id {type_id} unknown")
                packets = [(version, type_id, val)] + packets
                return packets


def flatten(data):
    if isinstance(data, list):
        return [x for y in data for x in flatten(y)]
    else:
        return [data]


def part1(data):
    Bits = BITS(data)
    packets = Bits.read_packet()
    packets = flatten(packets)
    count = 0
    for x in packets:
        count += x[0]
    return(count)

def part2(data):
    Bits = BITS(data)
    packets = Bits.read_packet()
    return(packets[0][2]) 


print(part1(data))
print(part2(data))
