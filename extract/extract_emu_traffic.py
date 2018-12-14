import re


def get_emu_traffic_raw(emu_log_file: str) -> [int]:
    traffic_pattern = re.compile(
        r'Traffic time: +(\d+) dsid: (\d) traffic: +(\d+)')
    with open(emu_log_file) as f:
        for line in f:
            if traffic_pattern.match(line):
                yield line


def get_emu_traffic(emu_log_file: str) -> {int: [(int, int)]}:
    traffic_pattern = re.compile(
        r'Traffic time: +(\d+) dsid: (\d) traffic: +(\d+)')
    per_dsid_cummu_traffic = {} # type:{int: [(int, int)]}
    for i in range(0, 2):
        per_dsid_cummu_traffic[i] = []
    with open(emu_log_file) as f:
        for line in f:
            m = traffic_pattern.match(line)
            if m is None:
                continue
            cycle, dsid, traffic = \
                map(int, (m.group(1), m.group(2), m.group(3)))
            per_dsid_cummu_traffic[dsid].append((cycle, traffic))
    return per_dsid_cummu_traffic


def main():
    print(get_emu_traffic('/home/zyy/projects/autoMBA/fpga/build/emu.log'))


if __name__ == '__main__':
    main()
