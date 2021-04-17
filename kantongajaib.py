# import library

import os
import sys
import math
import time
import argparse
import datetime

# import function
from LoadData import load_data
import MenambahItem
import data

# pengaturan untuk membaca argumen pada saat pemanggilan program
parser = argparse.ArgumentParser()
parser.add_argument("nama_folder", metavar="<nama_folder>")

try:
    args = parser.parse_args()
except:
    print("\nTidak ada nama folder yang diberikan!")
    print("Usage: python kantongajaib.py <nama_folder>\n")
    quit()

print("\nLoading...\n\n")
time.sleep(2)

# argumen tersimpan dalam variable directory
directory = args.nama_folder
load_data(directory)

# tes print data
print(data.header_gadget)
for test in data.gadget:
    print(test)
