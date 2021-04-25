# import library

import os
import sys
import math
import time
import argparse
import datetime

# import function
from RegisterAkmal      import register
from Login              import login
from LoadData           import load_data
from MenambahItem       import tambah_item
from MenghapusItem    import mengapus_gadget
from MeminjamGadget     import pinjam
from Exit import exit
from SaveData import save_data
import data

def call_procedure(input_user):
    if   (input_user == "register"):
        return register()
    # elif (input_user == "carirarity"):
    # elif (input_user == "caritahun"):
    elif (input_user == "tambahitem"):
        return tambah_item()
    elif (input_user == "hapusitem"):
        return mengapus_gadget()
    # elif (input_user == "ubahjumlah"):
    elif (input_user == "pinjam"):
        return pinjam();
    # elif (input_user == "kembalikan"):
    # elif (input_user == "minta"):
    # elif (input_user == "riwayatpinjam"):
    # elif (input_user == "riwayatkembali"):
    # elif (input_user == "riwayatambil"):
    elif (input_user == "save"):
        return save_data()
    # elif (input_user == "help"):
    elif (input_user == "exit"):
        return exit()
    else:
        print("coba ketik 'help")

# fungsi memamnggil procedure berdasarkan input user

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

# login user
login()

# program memulai meminta input dari user
while True :
    input_user = input("Masukkan perintah : ")
    print()
    call_procedure(input_user)
    print("\n")