# Author: Sunny Bhaveen Chandra
# Contact: sunny.c17hawke@gmail.com

import json
import os

def create_baseFile():
	baseData = '''{
	"cells": [{"cell_type": "markdown", "metadata": {},
	"source": ["# *Merged Jupyter Notebook*"]}],
	"metadata": {
	"kernelspec": {
	"display_name": "Python 3",
	"language": "python",
	"name": "python3"},
	"language_info": {
	"codemirror_mode": {"name": "ipython","version": 3},
	"file_extension": ".py",
	"mimetype": "text/x-python",
	"name": "python",
	"nbconvert_exporter": "python",
	"pygments_lexer": "ipython3",
	"version": "3.7.4"}
	},
	
	"nbformat": 4,
	"nbformat_minor": 2}'''

	Filename = 'baseFile.ipynb'
	with open(Filename,'w+') as f:
	    f.write(baseData)

def read_file_as_json(Filename):
    with open(Filename,'r') as f:
        whole_file = f.read()
    data = json.loads(whole_file)
    return data
    
def mergeAllJupyterFile(file=None):
    if not os.path.exists('baseFile.ipynb'):
        create_baseFile()

    # read files
    base_file = read_file_as_json('baseFile.ipynb')
    next_files = read_file_as_json(file)

    FileBoundry =   {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Merged Jupyter Notebook"
   ]
   }
    
    FileBoundry['source'] = f'<hr><font color="green"><h1>from file: {file[:-6]}</h1></font>'

    base_file['cells'] = base_file['cells'] + [FileBoundry] + next_files['cells']

    Filename = 'baseFile.ipynb'
    with open(Filename,'w+') as f:
            f.write(json.dumps(base_file))
        
def create_base_for_results():
    root_logDir = os.path.join(os.curdir, "results_folder")

    def move_file_sub_log_dir():
        import time
        run_id = time.strftime("mergedFile_%Y_%m_%d-%H_%M_%S")
        
        move_to_path = os.path.join(root_logDir, run_id)
        if not os.path.isdir(move_to_path):
            os.makedirs(move_to_path)
        base_file = 'baseFile.ipynb'
        
        import shutil
        shutil.move(base_file, move_to_path)
        print(f"\n## Access merged file at \
the following location ##\n{move_to_path}")
    
    move_file_sub_log_dir()

class CleanExit(Exception):
    def __init__(self):
        print("\n## No jupyter notebooks found to merge ##")
        print("\nexiting program....")


def safelyExit():
    import sys
    try:
        sys.exit()
    except:
        raise CleanExit

def is_target_notebooks_exists(listOfFiles):
    for file in listOfFiles:
        if ".ipynb" in file:
            return True
    return False

def main():
    listOfFiles = os.listdir()

    if '.ipynb_checkpoints' in listOfFiles:
        listOfFiles.remove('.ipynb_checkpoints')
    if "mergeJupyterFiles.ipynb" in listOfFiles:
        listOfFiles.remove('mergeJupyterFiles.ipynb')
            
    if not is_target_notebooks_exists(listOfFiles):
    	safelyExit()
    	
    listOfFiles.sort()
    for file in listOfFiles:
        if ".ipynb" in file:
            mergeAllJupyterFile(file)
    create_base_for_results()
        
if __name__=="__main__":
    try:
        main()
        print("\n## Attempt Successfull!! ##")
    except Exception as e:
        print(e)