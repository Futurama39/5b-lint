'''Linter for level texts files for the browser game Battle for Dream Island 5b'''
import glob, re, importlib

def main():
    # look for any files starting with 'lint' and then
    # execute all functions that start with 'rule'
    # NOTE: all rules return bools, we try assert and then
    # print out the error if not asserted
    
    # look for files in cwd for lint files
    for file in glob.glob('*.py'):
        if re.search(r'^lint',file):
            file = file[:-3] # strip the .py
            # import the file
            importlib.import_module(file)
            

if __name__ == '__main__':
    main()
