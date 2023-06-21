from pathlib import Path

Path(r"C:\ProgramFiles\app.py")

#This is called an absolute path because you are calling the entire file path,
#if you use the r function you don't have to type two \\ everytime and only
#have to use one \ , this makes the code cleaner and this is called a raw path

Path()

#When writing out his function with no file location it will represent the 
#current file you're in.

Path("ecommerce")

#Say you had a file inside of this file, you could call the file inside of this
#file by the method above and you don't have to write out an absolute file.

Path() / "ecommerce" / "__init__.py"

#This is another way of calling a file path