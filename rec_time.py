import time
import logging
import argparse
from sys import argv
from os import remove
from os.path import dirname, abspath, join

def get_file_path(subject_id):
    file_name = "timing_subject_{}.csv".format(subject_id)
    path = join(join(dirname(dirname(abspath(__file__))), 'data'), file_name)
    return path

def remove_file(subject_id):
    file = get_file_path(subject_id)
    try:
        print(file)
        remove(file)
    except OSError:
        pass

def header(subject_id):
    with open(get_file_path(subject_id), 'a') as f:
        f.write("subject, action, screen, timestamp\n")

def log(subject_id, timer_state, screen_id):
    with open(get_file_path(subject_id), 'a') as f:
        f.write("{}, {}, {}, {}\n".format(subject_id, timer_state,
              screen_id, str(time.time())))

if __name__ == "__main__":
    if len(argv) == 4:
        log(argv[1], argv[2], argv[3])
    else:
        remove_file(argv[1])
        header(argv[1])
