from extract.extract_emu_traffic import get_emu_traffic
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import time
import os
from os.path import join as pjoin


# result_dir = os.path.expanduser('~/projects/autoMBA/fpga/build')
result_dir = os.path.expanduser('~/projects/autoMBA/fpga/build/MBA-results')

def main():

    logs = [f for f in os.listdir(result_dir) \
            if f.endswith('log') and f.startswith('probing')]
    params = [x.split('.')[0] for x in logs]
    logs = [pjoin(result_dir, f) for f in logs]
    print(params)
    print(logs)

    fig, ax = plt.subplots()

    shapes = ['', '--']
    colors = ['r', 'b', 'g', 'c', 'm', 'y']
    assert len(colors) > len(params)
    while True:
        ax.set_ylabel('Cumulative Traffic')
        ax.set_xlabel('Cycles')

        traffics = get_emu_traffic(pjoin(result_dir, 'solo.log'))
        for dsid, traffic in traffics.items():
            matrix = np.array(traffic)
            ax.plot(matrix[:, 0], matrix[:, 1], 'k',
                    label='solo c{}'.format(dsid))
            break

        for param, f, color in zip(params, logs, colors):
            traffics = get_emu_traffic(f)
            for dsid, traffic in traffics.items():
                matrix = np.array(traffic)
                ax.plot(matrix[:, 0], matrix[:, 1], color + shapes[dsid],
                        label='{} c{}'.format(param, dsid))

        plt.tight_layout()
        plt.legend(loc='best')
        plt.show()
        # fig.canvas.draw()
        break
        time.sleep(7)
        ax.clear()


if __name__ == '__main__':
    main()
