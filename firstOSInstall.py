import os
from time import ctime

print("OS installed on : "+ctime(os.stat("C:Windows")[-1]))