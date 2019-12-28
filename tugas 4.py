data=[]
while(True):

    NAMA=input("Masukkan Nama: ")
    NIM=input("Masukkan NIM : ")
    Tugas=int(input(" Nilai Tugas: "))
    UTS=int(input(" Nilai UTS: "))
    UAS=int(input(" Nilai UAS: "))
    Akhir = (30 * Tugas/ 100) + (35 * UTS / 100) + (35 * UAS / 100)

    data.append([NAMA, NIM, Tugas, UTS, UAS, Akhir])
    ulangi=input("Tambah data (y/t)?")
    if ulangi.lower() == 't':
        break;

print("\nDaftar Nilai akhir\n")
print("=================================================================================")
print("|    NAMA    |    NIM      |    Tugas   |    UTS    |    UAS   |    Akhir   |")
print("=================================================================================")
for x in data:
    print("|  {0:3} |  {1:5}  | {2:9}   |   {3:6}   |   {4:4}   |  {5:5}    |".format(x[0], x[1], x[2], x[3], x[4], x[5]))
print("=================================================================================")