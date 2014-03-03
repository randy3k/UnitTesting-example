import imp
# make sure newest version of test_main is loaded
from . import test_hw
imp.reload(test_hw)

# load testcases
from .test_hw import *