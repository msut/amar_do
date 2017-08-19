#!/usr/local/bin/python3
import sys
import collections
import shutil
from os import listdir
from os.path import isfile, join, sep

#assumes that each file is of the format <name>_<padded number>.ext


#general idea: split each file, insert into map as series_ext->digit

def sequence_files(src, dest):
    # ls, get only files
    files = [f for f in listdir(src) if isfile(join(src, f))]
    # created nested dict
    dd = collections.defaultdict(dict)
    for file in files:
        seq, ext, num = split_filename(file)
        dd[seq + ext][num] = file
    #myprint(dd)
    #print(type(dd))
    new_names = {}
    for series, _ in dd.items():
        #print('series {} size: {}'.format(series, len(dd[series])))
        curr_int = 0
        for kk in dd[series]:
            file = dd[series][kk]
            #print('{} -> {}'.format(file, replace_int(file, curr_int)))
            new_names[file] = replace_int(file, curr_int)
            curr_int = curr_int + 1
    #print(new_names)
    rename_files(src, dest, new_names)


def rename_files(src_dir, dst_dir, names):
    for old_name in names:
        new_name = names[old_name]
        src = join(src_dir, old_name)
        dst = join(dst_dir, new_name)
        print('moving {} to {}'.format(src, dst))
        shutil.copyfile(src, dst)


def get_padded_int(to_pad):
    if to_pad < 10:
        return '0' + str(to_pad)
    else:
        return str(to_pad)


def replace_int(file, new_int):
    seq, ext, num = split_filename(file)
    return seq + '_' + get_padded_int(new_int) + '.' + ext


def split_filename(file):
    #print(file)
    seq = file.split('_')
    num = int(seq[1].split('.')[0])
    ext = seq[1].split('.')[1]
    seq = seq[0]
    return(seq, ext, num)


def myprint(d):
  for k, v in d.items():
    if isinstance(v, dict):
      myprint(v)
    else:
      print("{0} : {1}".format(k, v))


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("require 2 arguments: source directory, destination directory")
    else:
        sequence_files(sys.argv[1], sys.argv[2])