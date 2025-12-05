# modulES => INSTALL external packages
# ----------------------------------
# 1-module vs package
# 2-external packages download from internet
# 3-u can install packages with python package manager pip
# [4] PIP Install the Package and Its Dependencies 
# [5] Modules List "https://docs.python.org/3/py-modindex. html" 
# [6] Packages and Modules Directory "https://pypi.org/ 
# [7] PIP Manual "https://pip.pypa.io/en/stable/reference/pip_install/"
# ------------------------------
import termcolor
import pyfiglet
# print(dir(pyfiglet))
# print("-_"*10)
# print(dir(termcolor))

print(pyfiglet.figlet_format("salah"))
print(termcolor.colored(pyfiglet.figlet_format("salah"),"yellow"))
print(help(termcolor.colored))

