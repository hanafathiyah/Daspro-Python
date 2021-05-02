# import library

import os
import sys
import math
import time
import argparse
import datetime

# import function
from Register               import register
from Login                  import login
from Pencarian_Rarity       import mencari_rarity
from Pencarian_Tahun        import mencari_tahun
from LoadData               import load_data
from MenambahItem           import tambah_item
from MenghapusItem          import mengapus_item
from Mengubahitem           import mengubah_jumlah_item
from MeminjamGadget         import pinjam
from MengembalikanGadget    import mengembalikan_gadget
from MemintaConsumable      import minta_consume
from RiwayatPinjam          import riwayatpinjam
from RiwayatKembali         import riwayatkembali
from RiwayatAmbil           import riwayatambil
from SaveData               import save_data
from Help                   import help
from Exit                   import exit
from desain                 import kantongajaib_header
from color                  import yellow
import data


# fungsi untuk memanggil procedure berdasarkan input user
def call_procedure(input_user):
    if   (input_user == "register"):            return register()
    elif (input_user == "carirarity"):          return mencari_rarity()
    elif (input_user == "caritahun"):           return mencari_tahun()
    elif (input_user == "tambahitem"):          return tambah_item()
    elif (input_user == "hapusitem"):           return mengapus_item()
    elif (input_user == "ubahjumlah"):          return mengubah_jumlah_item()
    elif (input_user == "pinjam"):              return pinjam()
    elif (input_user == "kembalikan"):          return mengembalikan_gadget()
    elif (input_user == "minta"):               return minta_consume()
    elif (input_user == "riwayatpinjam"):       return riwayatpinjam()
    elif (input_user == "riwayatkembali"):      return riwayatkembali()
    elif (input_user == "riwayatambil"):        return riwayatambil()
    elif (input_user == "save"):                return save_data()
    elif (input_user == "help"):                return help()
    elif (input_user == "exit"):                return exit()
    else:                                       return print("coba ketik 'help'")


# pengaturan untuk membaca argumen pada saat pemanggilan program
parser = argparse.ArgumentParser()
parser.add_argument("nama_folder", metavar="<nama_folder>")

try:
    args = parser.parse_args()
except:
    print("\nTidak ada nama folder yang diberikan!")
    print("Usage: python kantongajaib.py <nama_folder>\n")
    quit()

print("\nLoading . . .", end="")
time.sleep(2)
print("\n\n")

# argumen tersimpan dalam variable directory
directory = args.nama_folder
load_data(directory)
os.system("cls")


# login user
kantongajaib_header()
print("Selamat datang di",yellow("Kantong Ajaib")+",","silakan",yellow("login"),"menggunakan akun Anda!\n")
login()

# program memulai meminta input dari user
while True :
    input_user = input(yellow("Masukkan perintah : "))
    print()
    os.system("cls")
    call_procedure(input_user)
    print("\n")
