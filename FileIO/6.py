import os, re
import urllib.parse
import urllib.request
url = "http://699340.youcanlearnit.net/image009.jpg"        # URL
       
def download(url, d):                                       # Define function
    if not os.path.isdir(d): os.mkdir(d)                    # Create directory if not exists
    h, f = os.path.split(url)                               # Split URL into host and file name
    a = re.findall(r'[0-9]+', f)[-1]                        # Get last number in file name
    for z in range(3):                                      # To find 3 subsequent files
        ni = str(int(a) + z)                                # Find the next image number
        if a[0] == '0':                                     # If the first digit is 0
            ni = '0' * (len(a) - len(ni)) + ni              # Add zeros to the front
        u = urllib.parse.urljoin(h, re.sub(a, ni, f))       # Join host and file name
        try:
            out = os.path.join(d, os.path.basename(u))      # Set path for download
            urllib.request.urlretrieve(u, out)              # Download the file
            print(f'Downloaded {os.path.basename(u)}')      # Print notification
        except IOError:                                     # If file not found
            print(f'Could not retrieve {u}')                # Print error
            break                                           # Break out of loop
    
download(url, '.\\images')                                  # Function Call