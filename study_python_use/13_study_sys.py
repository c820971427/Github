import sys
import os

__version__ = 'v1.0'
current_path = os.path.abspath(os.path.dirname(__file__))
print(os.getcwd())
print(current_path)
print(__version__)
print(__name__)

for index, value in enumerate(sys.argv):
    print(f'第%d个参数是： %s' % (index, value))
