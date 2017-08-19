#!/usr/local/bin/python3
import sys
import random

def make_files(dir, name, ext, count):
    padded = ['0{0}'.format(x) if x < 10 else '{}'.format(x) for x in range(100)]
    random.shuffle(padded)
    print('Creating {0} files named like {1}_XX.{2} in {3}'.format(count, name, ext, dir))
    for num in range(count):
        filename = '{0}_{1}.{2}'.format(name, padded[num], ext)
        print('creating {}'.format(filename))
        path = dir + filename
        file = open(path, 'w+')
        file.write('original name: {0}'.format(filename))
        file.close()


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("require 4 arguments: directory, series name, extension, number of files")
    else:
        make_files(sys.argv[1], sys.argv[2], sys.argv[3], int(sys.argv[4]))