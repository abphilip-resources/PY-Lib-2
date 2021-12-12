import os
from zipfile import ZipFile

def zip(d, ex, out):                                            # Define function   
    with ZipFile(out, 'w') as o:                                # Open zip file
        for root, dirs, files in os.walk(d):                    # Walk through directory
            r = os.path.relpath(root, d)                        # Get relative path
            for z in files:                                     # For each file
                n, e = os.path.splitext(z)                      # Split file name and extension
                if e.lower() in ex:                             # If extension is in the list
                    o.write(os.path.join(root, z),
                        arcname=os.path.join(r, z))             # Write file to zip
                    
zip('./organize', ['.jpeg','.txt','.m4a'], 'organize.zip')      # Function Call