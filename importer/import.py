import csv
import sys
import os
import osf
import modgrammar

file = sys.argv[1]
data_dir = os.path.dirname(os.path.realpath(file))

with open(file) as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    next(reader, None)

    for row in reader:
        file = row[0]
        full_file = data_dir + "/" + file
        lines = [line.rstrip('\n') for line in open(full_file)]
        pod = row[2]
        number = row[3]
        is_delete = (row[4] == 'x')
        is_podcast = not (row[5] == 'x')
        is_private = (row[5] == 'x')

        if is_delete:
            continue

        if is_podcast:
            print(full_file + " (" + str(len(lines)) + ") => " + pod + " " + number)

            header, parse_lines = osf.parse_lines(lines)
            osf_lines = osf.objectify_lines(parse_lines)

            for line in osf_lines:
              if isinstance(line, modgrammar.ParseError):
                print(line)
