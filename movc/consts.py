__author__ = 'pg'

import os
from os.path import *

### valid ranges for year and month
ALLOWED_YEARS = range(2016, 2100)
ALLOWED_MONTHS = range(1, 13)

### mapper path
BASEDIR = dirname(dirname(realpath(__file__)))
MAPPING_FILE = os.path.join(BASEDIR, "config", "mapping.csv")

