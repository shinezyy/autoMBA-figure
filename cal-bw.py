from extract.extract_bw import cal_bw
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('input_file', nargs=1)
parser.add_argument('-r', '--ranges', nargs=2, action='store',
        help='Cycle range', required=True)
parser.add_argument('-d', '--dsid', action='store', type=int,
        help='Cycle range')



if __name__ == '__main__':
     args = parser.parse_args()
     bw = cal_bw(args.input_file[0], float(args.ranges[0]), float(args.ranges[1]),
             args.dsid)
     print(bw)

