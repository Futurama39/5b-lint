'''Linter for level texts files for the browser game BFDIA 5b'''
import glob
import re
import importlib
import logging

errors = []
# all errs get accumulated globally and then outed from the list


class Level:
    def __init__(self, rawlevel) -> None:
        # TODO: encase in a try-except and raise relevant errors
        # on not solving the class
        self.name = rawlevel[0]
        self.dim_line = rawlevel[1]
        self.nesc_deaths = rawlevel[-2]
        # look thru the bottom for a two digit number above [-2]
        # that's the dialogue count number and anything between it
        # and nesc_deaths is the dialogue
        for line_1, cont in enumerate(rawlevel):
            if re.match(r'[0-9]{2}', cont):
                self.lines_count = cont
                break
        self.dialogue = rawlevel[line_1+1:-3]
        # now everything between dialogue and dim_line is the level & entity ID
        for line_2, cont in enumerate(rawlevel[2:]):
            if re.search(r',', cont):
                # , is not a valid level char so we assume that
                # it only occurs in entity data, so the first time after
                # line 2 we see it we assume that's the entity list
                self.level = rawlevel[2:line_2-1]
                break
        self.dialogue = rawlevel[line_2:line_1-1]

        # TODO: rescue from failed load and try to diagnose it


def assemble_level_list(file: list) -> list:
    # outs a list of Level classes, oredered
    # should be global
    level_list = []
    index_start = 0
    for line_1, cont in enumerate(file):
        if cont == '':  # this is the level separator
            level_list.append(Level(file[index_start:line_1]))
            index_start = line_1 + 1
    return level_list


def main():
    # look for any files starting with 'lint' and then
    # execute main() in every file
    # NOTE: all rules return bools, we try assert and then
    # print out the error if not asserted

    # look for files in cwd for lint files
    for file in glob.glob('*.py'):
        if re.search(r'^lint', file):
            file = file[:-3]  # strip the .py
            # import the file
            module = importlib.import_module(file)
            module.main()


def loc_levels() -> list:
    # first try loading levels.txt from cwd if not found ask for any file
    try:
        with open('levels.txt', 'r') as f:
            return f.readlines()
    except FileNotFoundError:
        pass
    # let user locate the file and load all of it
    while True:
        path = input('Insert a path to your levels file to be linted:')
        try:
            with open(path, 'r') as f:
                return f.readlines()
                # needs entirety of file, gonna treat it
        except FileNotFoundError:
            logging.error('IMPORT TXT NOT FOUND')
            print('file not found please try again')


if __name__ == '__main__':
    main()
