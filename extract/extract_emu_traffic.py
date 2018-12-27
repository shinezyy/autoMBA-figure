import re


def get_emu_traffic_raw(emu_log_file: str) -> [int]:
    traffic_pattern = re.compile(
        r'Traffic time: +(\d+) dsid: (\d) traffic: +(\d+)')
    with open(emu_log_file) as f:
        for line in f:
            if traffic_pattern.match(line):
                yield line


def get_emu_traffic(emu_log_file: str, origin=True) -> {int: [(int, int)]}:
    traffic_pattern = re.compile(
        r'Traffic time: +(\d+) dsid: (\d) traffic: +(\d+)')
    per_dsid_cummu_traffic = {} # type:{int: [(int, int)]}
    per_dsid_start = {}
    with open(emu_log_file) as f:
        for line in f:
            m = traffic_pattern.match(line)
            if m is None:
                continue
            cycle, dsid, traffic = \
                map(int, (m.group(1), m.group(2), m.group(3)))

            if dsid not in per_dsid_cummu_traffic:
                per_dsid_cummu_traffic[dsid] = []
                per_dsid_start[dsid] = traffic

            if origin:
                traffic -= per_dsid_start[dsid]

            per_dsid_cummu_traffic[dsid].append((cycle, traffic))
    return per_dsid_cummu_traffic


def get_range_traffic(emu_log_file: str, start, end,
        origin=True) ->{int: [(int, int)]}:
    traffic_pattern = re.compile(
        r'Traffic time: +(\d+) dsid: (\d) traffic: +(\d+)')
    per_dsid_cummu_traffic = {} # type:{int: [(int, int)]}
    per_dsid_start = {}
    with open(emu_log_file) as f:
        for line in f:
            m = traffic_pattern.match(line)
            if m is None:
                continue
            cycle, dsid, traffic = \
                map(int, (m.group(1), m.group(2), m.group(3)))
            if cycle < start or cycle > end:
                continue
            if dsid not in per_dsid_cummu_traffic:
                per_dsid_cummu_traffic[dsid] = []
                per_dsid_start[dsid] = traffic

            if origin:
                traffic -= per_dsid_start[dsid]

            per_dsid_cummu_traffic[dsid].append((cycle, traffic))
    return per_dsid_cummu_traffic




def main():
    print(get_emu_traffic('/home/zyy/projects/autoMBA/fpga/build/emu.log'))


if __name__ == '__main__':
    main()
