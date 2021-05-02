import data
from desain import help_header

def help():    
    help_header()
    role_user = data.user_login[5]

    if(role_user == "admin"):
        print("register \t", end=" "),           print("mendaftarkan pengguna baru")
        print("carirarity \t", end=" "),         print("mencari gadget dengan rarity tertentu")
        print("caritahun \t", end=" "),          print("mencari gadget berdasarkan tahun ditemukan")
        print("tambahitem \t", end=" "),         print("menambahkan item ke dalam inventori ")
        print("hapusitem \t", end=" "),          print("menghapus item pada database")
        print("ubahjumlah \t", end=" "),         print("mengubah jumlah gadget atau consumable")
        print("riwayatpinjam \t", end=" "),      print("mencetak riwayat peminjaman gadget")
        print("riwayatkembali \t", end=" "),     print("mencetak riwayat pengembalian gadget")
        print("riwayatambil \t", end=" "),       print("mencetak riwayat pengambilan consumable")
        print("save \t\t", end=" "),             print("melakukan penyimpanan data ke dalam file")
        print("help \t\t", end=" "),             print("mencetak prosedur untuk memberikan panduan")
        print("exit \t\t", end=" "),             print("keluar dari aplikasi")

    elif(role_user == "user"):
        print("carirarity \t", end=" "),         print("mencari gadget dengan rarity tertentu")
        print("caritahun \t", end=" "),          print("mencari gadget berdasarkan tahun ditemukan")
        print("pinjam \t\t", end=" "),           print("pemimjaman gadget")
        print("kembalikan \t", end=" "),         print("pengembalian gadget")
        print("minta \t\t", end=" "),            print("meminta consumable")
        print("save \t\t", end=" "),             print("melakukan penyimpanan data ke dalam file")
        print("help \t\t", end=" "),             print("mencetak prosedur untuk memberikan panduan")
        print("exit \t\t", end=" "),             print("keluar dari aplikasi")
