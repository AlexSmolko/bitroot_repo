n_output_fiLe = open('myfile.txt', 'w')
n_output_fiLe.write('Hello file world!\n')
n_output_fiLe.close()

# n_output_fiLe = open('myfile.txt', 'r')
# print(n_output_fiLe.read())
# n_output_fiLe.close()

with open('myfile.txt') as myfile:
     r_myfile = myfile.read()
     print(r_myfile)


"""Notices: Yes, if we run the first script it's will create the file exact in the same directory in which was created 
the script. But if we change the directory path to the filename passed to open, this will create the file in that
directory which finds on that path which we specify. Of cource if the path was specified correctly.:)"""