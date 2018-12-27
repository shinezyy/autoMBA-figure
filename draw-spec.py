from extract.extract_emu_traffic import get_emu_traffic
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import time
import os
import sys
from os.path import join as pjoin


# result_dir = os.path.expanduser('~/projects/autoMBA/fpga/build')
# result_dir = os.path.expanduser('~/projects/autoMBA-figure/openocd/cp/results')
# result_dir = './openocd/cp/results'

def main(log_file):

    # logs = [f for f in os.listdir(result_dir) \
    #         if f.endswith('log')]
    logs = [log_file]
    params = [log_file.split('/')[-2] for x in logs]
    # logs = [pjoin(result_dir, f) for f in logs]
    # print(params)
    # print(logs)

    fig, ax = plt.subplots()

    # shapes = ['', '--', 'v', '.', '+']
    shapes = [''] * 6
    colors = ['r', 'y', 'g', 'c', 'b', 'm', 'k']
    assert len(colors) > len(params)
    while True:
        ax.set_ylabel('Cumulative Traffic')
        ax.set_xlabel('Cycles')

        # traffics = get_emu_traffic(pjoin(result_dir, 'solo.log'))
        # for dsid, traffic in traffics.items():
        #     matrix = np.array(traffic)
        #     ax.plot(matrix[:, 0], matrix[:, 1], 'r',
        #             label='solo c{}'.format(dsid))
        #     break

        for param, f in zip(params, logs):
            if f != log_file:
                continue
            traffics = get_emu_traffic(f)
            for dsid, traffic in traffics.items():
                matrix = np.array(traffic)
                # print(matrix)
                ax.plot(matrix[:, 0], matrix[:, 1], colors[dsid] + shapes[dsid],
                        label='{} c{}'.format(param, dsid))

        plt.tight_layout()
        plt.legend(loc='best')
        plt.show()
        # fig.canvas.draw()
        break
        time.sleep(3)
        ax.clear()


if __name__ == '__main__':
    main(sys.argv[1])
