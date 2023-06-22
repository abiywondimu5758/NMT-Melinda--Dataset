# import re
def remove_newlines(fname):
    modified=[]
    flist = open(fname, encoding='UTF-8').read()
    print(flist)
    for sub in flist:
      modified = sub.replace("\n","")
      # print(modified)
    with open('new_output.txt', 'w') as file: # file where we write the cleaned data
      file.write(modified)
    print('Output file created successfully!')

remove_newlines("out_new.txt") 
