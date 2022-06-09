import os
import sys
from subprocess import check_output, check_call
import pip

#install halo package if it's not there
def package_install(package):
    FNULL = open(os.devnull, 'w')
    check_call([sys.executable, "-m", "pip", "install", package], stdout=FNULL)

#check halo package for spinner
try:
    pip.main(['install', 'halo'])
    import halo
except ImportError as e:
    package_install('halo')
    import halo