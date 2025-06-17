## NILAI SISWA ##

#----MEMBUAT DATA BUATAN (DUMMY) NILAI SISWA---#

daftar_nilai_siswa = [
    {
        'NAMA' : 'SARAH',
        'NRP' : 50020012, 
        'KELAS' : 'A',
        'MATEMATIKA' : 80,
        'KIMIA' : 92,
        'STATISTIK' : 87,
        'PEMROGRAMAN' : 82
    },
    {
        'NAMA' : 'AMELIA',
        'NRP' : 50020013,
        'KELAS' : 'B',
        'MATEMATIKA' : 70,
        'KIMIA' : 83,
        'STATISTIK' : 94,
        'PEMROGRAMAN' : 79
    },
    {
        'NAMA' : 'BAYU',
        'NRP' : 50020014,
        'KELAS' : 'B',
        'MATEMATIKA' : 92,
        'KIMIA' : 81,
        'STATISTIK' : 84,
        'PEMROGRAMAN' : 88
    },
    {
        'NAMA' : 'DIKA',
        'NRP' : 50020015,
        'KELAS' : 'A',
        'MATEMATIKA' : 91,
        'KIMIA' : 79,
        'STATISTIK' : 85,
        'PEMROGRAMAN' : 85
    },
    {
        'NAMA' : 'EMIL',
        'NRP' : 50020016,
        'KELAS' : 'A',
        'MATEMATIKA' : 82,
        'KIMIA' : 82,
        'STATISTIK' : 92,
        'PEMROGRAMAN' : 86
    }
]

daftar_siswa_terhapus = [] #database dari data yang akan terhapus

def create_data():
    while True:
        menu_option = int(input('''
    MENAMBAH DAFTAR NILAI
    1. Tambah Data Siswa
    2. Kembali ke Menu Utama
                
    Input Opsi (1-2): '''))

        if menu_option == 1:
            # Cek duplikat NRP
            while True:
                nrp_input = input('\nMasukkan NRP (8 angka): ')
                if nrp_input.isdigit() and len(nrp_input) == 8:  #isdigit digunakan untuk mengecek apakah string (nrp_input) berisi digit (0-9) dan panjang karakter angka harus 8
                    nrp_baru = int(nrp_input)

                    nrp_ada =  False #apabila belum ditemukan
                    for siswa in daftar_nilai_siswa:
                        if siswa['NRP'] == nrp_baru:
                            nrp_ada = True
                            break

                    if nrp_ada: #apabila NRP baru yang dimasukkan sama dengan NRP yang ada di database, maka akan diminta input ulang
                        print(f'NRP tersedia. Silakan masukkan NRP lain.') 
                    else:
                        print(f"NRP {nrp_baru} berhasil ditambahkan")
                        break
                else:
                    print('NRP harus 8 angka')

            # Masukkan Nama
            tambah_nama = input('\nMasukkan Nama Siswa Baru: ').upper()
            if tambah_nama.replace(' ', '').isalpha(): #semua nama berbentuk karakter/tanpa angka atau tambahan lain
                print(f'\nData siswa {tambah_nama} berhasil ditambahkan!\n')
            else:
                print('\nNama tidak valid! Hanya masukkan huruf saja')
                return create_data() #menghentikan looping

            # Tambah Kelas
            while True: #diminta input berulang apabila kelas tidak A atau B
                tambah_kelas = input('Masukkan kelas siswa (A/B): ').upper()
                if tambah_kelas in ['A', 'B']:
                    break
                else:
                    print('Kelas tersedia hanya A/B. Silahkan masukkan kelas yang sesuai.')

            # Tambah Nilai
            tambah_nilai = {}
            for mata_pelajaran in ['MATEMATIKA', 'KIMIA', 'STATISTIK', 'PEMROGRAMAN']:
                nilai_input = input(f'Masukkan nilai {mata_pelajaran} (0-100): ')
                if nilai_input.isdigit():
                    nilai = int(nilai_input)
                    if 0 <= nilai <= 100:   #nilai yang dimasukkan hanya berkisar 0-100
                        tambah_nilai[mata_pelajaran] = nilai
                    else:
                        print('Nilai harus 0-100')
                        return create_data()
                else:
                    print('Nilai harus angka')
                    return create_data()

            # Simpan Data
            simpan_data = input('Apakah Anda yakin menambahkan data? (Y/N): ').upper()
            if simpan_data == 'Y':
                daftar_nilai_siswa.append({  #ditambahkan di akhir
                    'NAMA': tambah_nama,
                    'NRP': nrp_baru,
                    'KELAS': tambah_kelas,
                    'MATEMATIKA': tambah_nilai['MATEMATIKA'],
                    'KIMIA': tambah_nilai['KIMIA'],
                    'STATISTIK': tambah_nilai['STATISTIK'],
                    'PEMROGRAMAN': tambah_nilai['PEMROGRAMAN']
                })
                print('\nData berhasil disimpan\n')
            else:
                print('\nData tidak disimpan\n')

        elif menu_option == 2:
            print("\nKembali ke Menu Utama.\n")
            break

        else:
            print("\nOpsi tidak valid. Silakan masukkan 1 atau 2.")

def read_data():
    from tabulate import tabulate #memudahkan user membaca dengan tampilan berupa tabel
    while True:
            menu_option = int(input('''
    MENAMPILKAN DAFTAR NILAI
    1. Tampilkan Seluruh Data
    2. Cari Data Berdasarkan NRP
    3. Kembali ke Menu Utama

    Input Opsi (1-3): '''))
            
            if menu_option == 1:
                if not daftar_nilai_siswa: #memeriksa apakah jika mengambil opsi 1 dan tidak ada dalam dictionary, maka akan terbaca tidak ada data
                    print('\nData tidak ditemukan.')
                    continue
                else:
                    print('\n-------- DAFTAR NILAI SISWA --------\n')
                    print(tabulate(daftar_nilai_siswa, headers = 'keys', tablefmt = 'rounded_outline'))

            elif menu_option == 2:
                if not daftar_nilai_siswa:
                    print("\nData kosong. Tidak ada yang bisa dicari.")
                    continue

                # Menampilkan NRP dan NAMA untuk memudahkan penulisan input NRP
                ringkasan_data = [{'NAMA': s['NAMA'], 'NRP': s['NRP']} for s in daftar_nilai_siswa]
                print('\nDAFTAR NAMA DAN NRP:')
                print(tabulate(ringkasan_data, headers='keys', tablefmt='rounded_outline'))

                while True: #memasukkan NRP yang dicari datanya atau opsi q untuk quit
                    temu_nrp = input('\nMasukkan NRP (8 angka) yang ingin dicari [atau ketik q untuk kembali]: ')
                    
                    if temu_nrp.lower() == 'q':
                        print("\nQuit.")
                        break
                    
                    if not (temu_nrp.isdigit() and len(temu_nrp) == 8):
                        print("Format NRP salah! Masukkan hanya 8 angka.")
                        continue #mengulang input saat kondisi yang dimasukkan salah
                    
                    siswa_ditemukan = None 
                    for siswa in daftar_nilai_siswa: # loop untuk mencari NRP siswa
                        if str(siswa['NRP']) == temu_nrp:
                            siswa_ditemukan = siswa
                            break

                    if siswa_ditemukan: #NRP ada
                        print('\nDATA DITEMUKAN:\n')
                        print(tabulate([siswa_ditemukan], headers='keys', tablefmt='rounded_outline'))
                        break  # Keluar dari loop setelah data ditemukan
                    else:
                        print("Data dengan NRP tersebut tidak ditemukan. Coba lagi.")

            elif menu_option == 3:
                print('\nKembali ke Menu Utama')
                break

            else:
                print('\nOpsi tidak valid\n')

def update_data():
    while True:
        menu_option = int(input('''
    MENGUPDATE NILAI
    1. Update Data Siswa
    2. Kembali ke Menu Utama
                
    Input Opsi (1-2): '''))

        if menu_option == 1:
            if not daftar_nilai_siswa:
                print('\nData tidak ditemukan.')
                continue

            print("\n--- Daftar Siswa ---")
            for i, siswa in enumerate(daftar_nilai_siswa, start=1): #mengiterasi semua data dalam daftar nilai siswa
                print(f"{i}. {siswa['NAMA']} (NRP: {siswa['NRP']})")

            while True:
                try:
                    idx = int(input("\nPilih nomor siswa yang ingin diupdate: ")) - 1 #untuk penomoran dimulai dari 1
                    if idx < 0 or idx >= len(daftar_nilai_siswa): #indeks berada dalam database yang telah dideklarasikan
                        print("Nomor tidak valid")
                        continue
                    siswa = daftar_nilai_siswa[idx]
                    break  # keluar dari loop pemilihan siswa
                except ValueError:
                    print("Masukkan angka yang valid.")
                    continue

            while True:
                print(f"\nData Siswa Belum Ter-Update:\n{siswa}")
                print('''
                Kolom yang bisa diupdate:
                1. NAMA
                2. NRP
                3. KELAS
                4. MATEMATIKA
                5. KIMIA
                6. STATISTIK
                7. PEMROGRAMAN
                ''')
                kolom = input("Masukkan nomor kolom yang ingin diubah: ")
                kolom_map = {
                    '1': 'NAMA',
                    '2': 'NRP',
                    '3': 'KELAS',
                    '4': 'MATEMATIKA',
                    '5': 'KIMIA',
                    '6': 'STATISTIK',
                    '7': 'PEMROGRAMAN'
                } #yang akan di-update, data ada dalam database

                if kolom not in kolom_map:
                    print("Pilihan kolom tidak valid. Masukkan angka 1-7.")
                    continue
                else:
                    kolom_baru = kolom_map[kolom]
                    break

            nilai_baru = input(f"Masukkan input baru untuk {kolom_baru}: ").upper()

            konfirmasi_update = input(f'Apakah yakin ingin update {kolom_baru} menjadi {nilai_baru}? (Y/N): ').upper()
            if konfirmasi_update != 'Y':
                print('Update dibatalkan')
                continue

            if kolom_baru == 'KELAS':
                if nilai_baru not in ['A', 'B']:
                    print('Kelas tersedia hanya A/B. Silahkan masukkan kelas yang sesuai.')
                    continue
                siswa[kolom_baru] = nilai_baru #update input baru

            elif kolom_baru in ['MATEMATIKA', 'KIMIA', 'STATISTIK', 'PEMROGRAMAN']:
                if not nilai_baru.isdigit() or not (0 <= int(nilai_baru) <= 100):
                    print("Nilai harus berupa angka 0-100.")
                    continue
                siswa[kolom_baru] = int(nilai_baru)

            elif kolom_baru == 'NRP':
                if not nilai_baru.isdigit() or len(nilai_baru) != 8:
                    print("NRP harus berupa angka 8 digit.")
                    continue
                siswa[kolom_baru] = int(nilai_baru)

            else:
                siswa[kolom_baru] = nilai_baru

            print("\n Data berhasil diupdate!\n")

        elif menu_option == 2:
            print('\nKembali ke Menu Utama')
            break
        else:
            print('\nMasukkan Opsi (1-2)')
                    
def delete_data(): 
    from tabulate import tabulate
    while True:
        menu_option = int(input('''
    MENGHAPUS DATA NILAI
    1. Delete Data Siswa
    2. Kembali ke Menu Utama
                
    Input Opsi (1-2): ''')) 
        
        if menu_option == 1:
            ringkasan_data = [{'NAMA': s['NAMA'], 'NRP': s['NRP']} for s in daftar_nilai_siswa] #s digunakan sebagai variabel untuk setiap item dalam databse daftar nilai siswa
            print('\nDAFTAR NAMA DAN NRP:')
            print(tabulate(ringkasan_data, headers='keys', tablefmt='rounded_outline'))
            while True:
                nrp_hapus = input("\nMasukkan NRP siswa (8 angka) yang ingin dihapus: ")
                if not nrp_hapus.isdigit() or len(nrp_hapus) != 8: #jika nrp tidak berisi angka dan tidak memiliki panjang karalter 8
                    print("NRP harus berupa angka 8 digit.")
                    continue

                nrp_hapus = int(nrp_hapus)
                ditemukan = False #belum ditemykan

                for i, siswa in enumerate(daftar_nilai_siswa):
                    if siswa['NRP'] == nrp_hapus:
                        option_konfirmasi = input(f"Apakah kamu yakin ingin menghapus data {siswa['NAMA']}? (Y/N): ").upper()
                        if option_konfirmasi == 'Y':
                            daftar_siswa_terhapus.append(siswa)
                            del daftar_nilai_siswa[i]
                            print(f"\nData dengan NRP {nrp_hapus} berhasil dihapus.")
                        else:
                            print("\nPenghapusan dibatalkan.")
                        ditemukan = True #ketika data telah ditemkan
                        return

                if ditemukan == False:
                    print(f"\nData dengan NRP {nrp_hapus} tidak ditemukan.")

        elif menu_option == 2:
            print('\nKembali ke Menu Utama')
            break

        else:
            print("\nOpsi tidak valid. Silakan masukkan 1 atau 2.")

def restore_data():
    from tabulate import tabulate
    if not daftar_siswa_terhapus:
        print('\nTidak ada data yang tersedia')
        return
    
    print('\nDATA YANG TERHAPUS: ')
    print(tabulate(daftar_siswa_terhapus, headers='keys', tablefmt='rounded_outline'))

    while True:
        nrp_pulih = input('Masukkan NRP yang ingin dipulihkan datanya: ')
        if not nrp_pulih.isdigit() or len(nrp_pulih) !=8:
            print('\nNRP harus berupa 8 angka')
            continue
        nrp_restore = int(nrp_pulih)
        ditemukan = False

        for i, siswa in enumerate(daftar_siswa_terhapus):
            if siswa['NRP'] == nrp_restore:
                option_konfirmasi = input(f"Apakah kamu yakin ingin memulihkan data {siswa['NAMA']}? (Y/N): ").upper()
                if option_konfirmasi == 'Y':
                    daftar_nilai_siswa.append(siswa) 
                    del daftar_siswa_terhapus[i]
                    print(f"\nData dengan NRP {nrp_restore} berhasil dipulihkan.")
                else:
                    print('\nPemulihan dibatalkan. Silahkan kembali')
                ditemukan = True #NRP telah ditemukan
                break #menghentikan looping mencari NRP 

        if ditemukan: #menghentikan proses looping dari while True
            break
        else:
            print(f"\nData dengan NRP {nrp_restore} tidak ditemukan di Recycle Bin.")

def main_menu():
    while True:
        menu_option = input('''
========== MENU UTAMA ============
1. Lihat Data Siswa
2. Tambah Data Siswa
3. Update Data Siswa
4. Hapus Data Siswa
5. Pulihkan Data Siswa
6. Keluar

Pilih (1-6): ''')

        if menu_option == '1':
            read_data()
        elif menu_option == '2':
            create_data()
        elif menu_option == '3':
            update_data()
        elif menu_option == '4':
            delete_data()
        elif menu_option == '5':
            restore_data()
        elif menu_option == '6':
            print("\nTerima kasih! Program selesai.\n")
            break
        else:
            print("\nPilihan tidak valid. Masukkan angka 1 - 5.")

main_menu()