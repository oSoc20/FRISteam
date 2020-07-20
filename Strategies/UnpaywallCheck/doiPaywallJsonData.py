# -*- coding: utf-8 -*-
"""
Author Baudouin Martelee
FRISteam

"""
#Import packages
import os
import pandas as pd
import json
import glob
import requests
import sys

#3 lines of code tot get the import form other files working
PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))
