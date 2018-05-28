import fnmatch
import os
import re

# CONFIGURE INPUT VARIABLES
path = 'C:\\_src\\'  #root of the project
projects = ['DirectoryA', 'DirectoryB', 'DirectoryC']  # sub-directories holding the sub-projects

pattern_cpp = '*.cpp'
pattern_h = '*.h'

#######################################################################################################################
#######################################################################################################################


def print_info():
    for project, files in result_matrix.iteritems():
        print ("===================================================")
        print ("I                                                  ")
        print ("I PROJECT: \t" + project)
        print ("I___________________________________________________")
        for file, lines in files.iteritems():
            print ("I")
            print ("I SOURCE FILE:      " + file)
            for line in lines:
                print ("I   - NOT INCLUDED: " + line)
        print ("I                                                  ")
        print ("===================================================")
        print


result_matrix = {}

for prj in projects:
    p_path = path + prj + "\\"
    listOfFiles = os.listdir(p_path)

    file_matrix = {}
    for source_file in listOfFiles:
        if fnmatch.fnmatch(source_file, pattern_cpp):
            if source_file == "StdAfx.cpp":
                continue

            source_file_name = re.split('\.', source_file)[0]

            for header_file in listOfFiles:
                if fnmatch.fnmatch(header_file, pattern_h):
                    if re.split('\.', header_file)[0] == source_file_name:
                        scanExpression = '#include \"' + header_file + '\"'
                        input_file = open(p_path + source_file)
                        files_linked = False

                        for line in input_file:
                            result = re.match(scanExpression, line)
                            if result:
                                files_linked = True
                        input_file.close()

                        if not files_linked:
                            if source_file not in file_matrix:
                                file_matrix[source_file] = [header_file]
                            else:
                                file_matrix[source_file].append(header_file)

    if len(file_matrix) != 0:
        result_matrix[prj] = file_matrix


print_info()
