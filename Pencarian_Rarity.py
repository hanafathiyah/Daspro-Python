import data
from LoadData import load_data

load_data("folder_isi")

def mencari_rarity() :
  datas = data.gadget
  print(">>> carirarity")
  rarity = input("Masukkan rarity: ")
  print("\nHasil pencarian:\n")

  rarity_benar = False
  i = 0
  while rarity_benar == False and i < len(datas):
    if (rarity == datas[i][4]):
      print("Nama :", datas[i][1])
      print("Deskripsi :", datas[i][2])
      print("Jumlah :", datas[i][3], "buah")
      print("Rarity :", datas[i][4])
      print("Tahun Ditemukan :", datas[i][5] ,"\n")
      i += 1
    else:
      i += 1
