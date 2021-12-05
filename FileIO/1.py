F = open("file.txt",'r')                                # Open file in read mode
passFile = open("pass.txt",'w')                         # Create file in write mode
failFile = open("fail.txt",'w')                         # Create file in write mode
for line in F:
    if(line.split()[2]=="P"): passFile.write(line)      # Write the line to passFile
    else: failFile.write(line)                          # Write the line to failFile    
passFile.close()                                        # Close the file
failFile.close()                                        # Close the file