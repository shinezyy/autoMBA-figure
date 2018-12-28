#!/usr/bin/env python3


from __future__ import print_function
import sys
import os
import re

import inspect
file_path = os.path.dirname(os.path.realpath(
        inspect.getfile(inspect.currentframe())))
sys.path.insert(0, os.path.join(file_path, '../'))

from extract.extract_emu_traffic import get_range_traffic


def cal_bw(log_file: str, start, end, dsid=None) -> float:
    nCores = 4
    traffics = get_range_traffic(log_file, start, end)
    if dsid is None:
        total_bw = 0
        for d in traffics:
            per_id_log = traffics[d]
            bw = float(per_id_log[-1][1] - per_id_log[0][1])/(
                    per_id_log[-1][0] - per_id_log[0][0]) * 1000
            # print(bw)
            total_bw += bw
        return total_bw
    else:
        per_id_log = traffics[dsid]
        return float(per_id_log[-1][1] - per_id_log[0][1])/(
                per_id_log[-1][0] - per_id_log[0][0]) * 1000


if __name__ == '__main__':

    four_mix_total = \
            cal_bw('../openocd/cp/results/4-run-stream-12.log',
                    3e9, 1.9e10)

    four_bind_total = \
            cal_bw('../openocd/cp/results/4-run-stream-bind-12.log',
                    2.1e9, 2.1e10)

    four_bind_total_control = \
            cal_bw('../openocd/cp/results/4-run-stream-bind-12.log',
                    2.1e9, 8.8e9)

    four_bind_total_after = \
            cal_bw('../openocd/cp/results/4-run-stream-bind-12.log',
                    1.1e10, 2.1e10)

    four_bind_high = \
            cal_bw('../openocd/cp/results/4-run-stream-bind-12.log',
                    2.1e9, 8.9e9, 4)

    solo_bind = \
            cal_bw('../openocd/cp/results/solo-bind-stream-12.log',
                    7.5e9, 1.2e10, 4)

    print(four_mix_total, four_bind_total, four_bind_total_control,
            four_bind_total_after, four_bind_high, solo_bind)
