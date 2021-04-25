import data
from LoadData import load_data

load_data("folder_isi")

def mencari_rarity() :
  datas = data.gadget
  print(">>> carirarity")
  rarity = input("Masukkan rarity: ")
  print("\nHasil pencarian:\n")

  for array in (datas):
    if (rarity == array[4]):
      print("Nama :", array[1])
      print("Deskripsi :", array[2])
      print("Jumlah :", array[3], "buah")
      print("Rarity :", array[4])
      print("Tahun Ditemukan :", array[5] ,"\n")
