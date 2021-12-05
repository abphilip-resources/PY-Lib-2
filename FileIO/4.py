import os                                                                   
from pathlib import Path                
os.chdir('./Python/Automation/IO/organize')        # Change directory to the directory of the files                       

S = {                                              # Dictionary of categories and their filetype suffixes
    "documents": ['.pdf','.rtf','.txt'],
    "audio":['.m4a','.m4b','.mp3'],
    "videos": ['.mov','.avi','.mp4'],
    "images": ['.jpg','.jpeg','.png']
}

def pick(k):
    for c,s in S.items():                          # Iterate through the dictionary
        for z in s:
            if(z==k): return c                     # Returns the key of the dictionary i.e. the category
    return 'misc'                                  # If filetype doesn't exist in our dictionary return misc

for z in os.scandir():
    if(z.is_dir()): continue                       # If the file is a directory, skip it
    p = Path(z)                                    # Create a path object for the file
    f = p.suffix.lower()                           # Get the filetype
    n = Path(pick(f))                              # Create a new path object for the category
    if not n.is_dir(): n.mkdir()                   # If the category directory doesn't exist, create it
    p.rename(n.joinpath(p))                        # Add the file to the directory by renaming file path object