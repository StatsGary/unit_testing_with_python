import sys
import os
# Append to sys path
for p in sys.path:
    print(p)

print(os.getcwd() + '/tests')

from .. import calc_root
# Set environment variable to enable directory switching
# sys.path.append('./app')
# import app.calc 
