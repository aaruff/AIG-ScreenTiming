import datetime
import pytz
import argparse
from sys import argv
from os import remove
from os.path import dirname, abspath, join

def get_file_path(subject):
    file_name = "timing_subject_{}.csv".format(subject)
    path = join(join(dirname(dirname(abspath(__file__))), 'data'), file_name)
    return path

def remove_file(subject):
    file = get_file_path(subject)
    try:
        print(file)
        remove(file)
    except OSError:
        pass

def header(subject):
    with open(get_file_path(subject), 'a') as f:
        f.write("subject, state, phase, time\n")

def log(subject, state, phase, time):
    with open(get_file_path(subject), 'a') as f:
        row_format = "{}, {}, {}, {}\n"
        line = row_format.format(subject, state, phase, time)
        f.write(line)

if __name__ == "__main__":
    if len(argv) == 4:
        dt = datetime.datetime.now(tz=pytz.utc)
        log(argv[1], argv[2], argv[3], dt.isoformat())
    else:
        remove_file(argv[1])
        header(argv[1])
