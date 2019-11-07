import os
import time
import sys

readmedata = input("please input whatever data you would like in your readme, do not include \" or \' ")
readme = "echo '"+readmedata+"\'>> README.md"
os.system(readme)

