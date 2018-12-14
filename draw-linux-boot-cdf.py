from extract.extract_emu_traffic import get_emu_traffic
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import time
import os
from os.path import join as pjoin


result_dir = os.path.expanduser('~/projects/autoMBA/fpga/build/MBA-results')

def main():
    fig, ax = plt.subplots()
    while True:
        ax.set_ylabel('Cumulative Traffic')
        ax.set_xlabel('Cycles')

        traffics = get_emu_traffic(pjoin(result_dir, 'solo.log'))
        for dsid, traffic in traffics.items():
            matrix = np.array(traffic)
            ax.plot(matrix[:, 0], matrix[:, 1], label='solo c{}'.format(dsid))
            break

        traffics = get_emu_traffic(pjoin(result_dir, 'probing-50-75.log'))
        for dsid, traffic in traffics.items():
            matrix = np.array(traffic)
            ax.plot(matrix[:, 0], matrix[:, 1],
                    label='probing 50-75 c{}'.format(dsid))

        traffics = get_emu_traffic(pjoin(result_dir, 'probing-75-87.log'))
        for dsid, traffic in traffics.items():
            matrix = np.array(traffic)
            ax.plot(matrix[:, 0], matrix[:, 1],
                    label='probing 75-87 c{}'.format(dsid))

        traffics = get_emu_traffic(pjoin(result_dir, 'pausing-normal.log'))
        for dsid, traffic in traffics.items():
            matrix = np.array(traffic)
            ax.plot(matrix[:, 0], matrix[:, 1],
                    label='pausing normal c{}'.format(dsid))

        traffics = get_emu_traffic(pjoin(result_dir, 'pausing-radical.log'))
        for dsid, traffic in traffics.items():
            matrix = np.array(traffic)
            ax.plot(matrix[:, 0], matrix[:, 1],
                    label='pausing radical c{}'.format(dsid))

        plt.tight_layout()
        plt.legend(loc='best')
        fig.canvas.draw()
        break
        time.sleep(7)
        ax.clear()


if __name__ == '__main__':
    main()
