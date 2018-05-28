# missing_references
Identifies pair of .cpp and .h files which hare same name but are not referenced direclty. 
This is considered bad coding style practice.

https://google.github.io/styleguide/cppguide.html#Header_Files

The code is python script.

Requires configuring the fillowing variables:

* path - string variable of your source location. Note in windows you need to escape the '\' backslash with two '\\' backslashes

* projects - dict of strings, eachone representing the directory of your project, in case you have several sub-projects/dll project etc.

