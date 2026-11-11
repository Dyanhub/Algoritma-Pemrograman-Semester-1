import logging
import time

# ==========================
# BAGIAN 1: MEMBUAT DAN MENGAKSES DICTIONARY
# ==========================

def bagian_1():
    print("=" * 70)
    print("BAGIAN 1: MEMBUAT DAN MENGAKSES DICTIONARY")
    print("=" * 70)

    database_user = {
        "admin": {"password": "Admin123", "role": "administrator", "ip": "192.168.1.100"},
        "user1": {"password": "User123", "role": "user", "ip": "192.168.1.101"},
        "security": {"Password": "Secure@2024", "role": "security_officer", "ip": "192.168.1.102"}
    }

    print(f"\nDatabase User Lengkap: {database_user}")
    print(f"\nDatabase User admin: {database_user['admin']}")
    print(f"\nRole admin: {database_user['admin']['role']}")
    print(f"\nIP user1: {database_user['user1']['ip']}")
    print(f"\nakses aman get(): {database_user.get('guest', 'User tidak ditemukan')}")

# ==========================
# BAGIAN 2: operasi dasar dan method dictionary
# ==========================

def bagian_2():
    print("=" * 70)
    print("BAGIAN 2: OPERASI DASAR DAN METHOD DICTIONARY")
    print("=" * 70)

    ip_blacklist = {"192.168.1.100": "malicious",}
    print(f"\nData Awal: {ip_blacklist}")

    ip_blacklist["10.0.0.1"] = "suspicious"  # This line has a syntax error and will raise an exception
    ip_blacklist["192.168.1.100"] = "blocked"  # This line has a syntax error and will raise an exception
    print(f"\nSetelah Update: {ip_blacklist}") 

    print(f"\nKeys : {list(ip_blacklist.keys())}")
    print(f"\nValues : {list(ip_blacklist.values())}")
    print(f"\nItems : {list(ip_blacklist.items())}")    

    status = ip_blacklist.pop('10.0.0.1')
    print(f"\nElemen yang di-pop : {status}")
    print(f"\nSetelah pop : {ip_blacklist}")

    del ip_blacklist["192.168.1.100"]  # This line has a syntax error and will raise an exception
    print(f"\nSetelah delete : {ip_blacklist}")

# ==========================
# BAGIAN 3: ITERASI DAN DICTIONARY COMPREHENSION
# ==========================

def bagian_3():
    print("=" * 70)
    print("BAGIAN 3: ITERASI DAN DICTIONARY COMPREHENSION")
    print("=" * 70)

    log_skor = {"192.168.1.100": 9, "8.8.8.8": 2, "10.0.0.1": 8, "1.1.1.1": 3}
    print(f"\nData Log Skor: {log_skor}")

    print("\n--- Iterasi Melalui Keys value:")
    for ip, skor in log_skor.items():
        print(f"IP: {ip:18}, Skor: {skor}")

    ip_kritis = {ip: skor for ip, skor in log_skor.items() if skor >= 7}
    print(f"\nIP dengan skor kritis (>=7): {ip_kritis}")

    skor_kuadrat = {ip: skor**2 for ip, skor in log_skor.items()}
    print(f"\nSkor kuadrat: {skor_kuadrat}")

# ==========================
# BAGIAN 4: MEMBUAT DAN MENGAKSES SET
# ==========================

def bagian_4():
    print("=" * 70)
    print("BAGIAN 4: MEMBUAT DAN MENGAKSES SET")
    print("=" * 70)

    port_berbahaya = {21, 23, 25, 135, 445, 3389}
    print(f"\nPort Berbahaya: {port_berbahaya}")

    port_berbahaya.add(5900)
    print(f"\nSetelah menambahkan port 5900: {port_berbahaya}")

    port_berbahaya.discard(21)
    print(f"\nSetelah menghapus port 21: {port_berbahaya}")

    print(f"\nApakah 445 ada dalam set? {445 in port_berbahaya}")
    print(f"\nApakah 80 ada dalam set? {80 in port_berbahaya}")

    print("\n--- Iterasi Set ---")
    for port in port_berbahaya:
        print(f"Port Berbahaya: {port}")

# ==========================
# BAGIAN 5: OPERASI HIMPUNAN pada (SET)
# ==========================

def bagian_5():
    print("=" * 70)
    print("BAGIAN 5: OPERASI HIMPUNAN PADA (SET)")
    print("=" * 70)

    set_a = {21, 22, 80, 443}
    set_b = {22, 80, 3306, 3389}

    print(f"\nSet A(port Terbuka): {set_a}")
    print(f"\nSet B(Port aman): {set_b}")

    print(f"\nUnion (A | B): {set_a | set_b}")
    print(f"\nIntersection (A & B): {set_a & set_b}")
    print(f"\nDifference (A - B): {set_a - set_b}")
    print(f"\nSymmetric Difference (A ^ B): {set_a ^ set_b}")

# ==========================
# BAGIAN 6: PERBANDINGAN PERFOROMA (LIST VS SET)
# ==========================

def bagian_6():
    print("=" * 70)
    print("BAGIAN 6: PERBANDINGAN PERFOROMA (LIST VS SET)")
    print("=" * 70)

    data_list = list(range(1000000))  # List dengan 1 juta elemen
    data_set = set(range(1000000))     # Set dengan 1 juta elemen

    start = time.time()
    _ = 999999 in data_list
    list_time = time.time() - start
    start = time.time()
    _ = 999999 in data_set
    set_time = time.time() - start

    print(f"\nWaktu pencarian di List: {list_time:.6f} detik")
    print(f"\nWaktu pencarian di Set: {set_time:.6f} detik")
    print(f"\nPerbandingan: Set lebih cepat {list_time / set_time:.2f} kali dibanding List")

# ==========================
# BAGIAN 7: EXCEPTION HANDLING PADA DICTIONARY DAN SET
# ==========================

def bagian_7():
    print("=" * 70)
    print("BAGIAN 7: EXCEPTION HANDLING PADA DICTIONARY DAN SET")
    print("=" * 70)

    try:
        angka = int(input("\nMasukkan angka untuk dibagi (contoh: 5 atau 0): "))
        hasil = 10 / angka
        print(f"Hasil pembagian 10 / {angka} = {hasil}")
    except ZeroDivisionError:
        print("Error: Tidak bisa membagi dengan nol.")
    finally:
        print("Eksekusi selesai.")

# ==========================
# BAGIAN 8: RAISE AND CUSTOM EXCEPTION
# ==========================

def bagian_8():
    print("=" * 70)
    print("BAGIAN 8: RAISE AND CUSTOM EXCEPTION")
    print("=" * 70)

    class PortTidakValidError(Exception):
        pass

    def validasi_port(port):
        if port < 1 or port > 65535:
            raise ValueError(f"Port {port} tidak valid. Harus antara 0-65535.")
        if port in [21, 23, 25, 135]:
            raise PortTidakValidError(f"Port {port} termasuk port berbahaya.")
        return True
    try:
        validasi_port(70000)
    except ValueError as e:
        print(f"ValueError: {e}")
    try:
        validasi_port(23)
    except PortTidakValidError as e:
        print(f"PortTidakValidError: {e}")

# ==========================
# BAGIAN 9: Debugging dengan assert and print
# ==========================

def bagian_9():
    print("=" * 70)
    print("BAGIAN 9: DEBUGGING DENGAN ASSERT DAN PRINT")
    print("=" * 70)

    def validasi_ip(ip):
        print(f"[DEBUG] memeriksa Validasi IP: {ip}")
        assert len(ip.split('.')) == 4, f"IP {ip} tidak valid. Harus memiliki 4 oktet."
        for oktet in ip.split('.'):
            assert oktet.isdigit() and 0 <= int(oktet) <= 255, f"IP {ip} tidak valid. Oktet {oktet} tidak valid."
            return True

    try:
        validasi_ip("192.168.1.100")
        print("IP valid.")

        validasi_ip("192.168.1.")
    except AssertionError as e:
        print(f"AssertionError: {e}")

# ==========================
# BAGIAN 10: LOGGING DENGAN MODUL LOGGING
# ==========================

def bagian_10():
    print("=" * 70)
    print("BAGIAN 10: LOGGING DENGAN MODUL LOGGING")
    print("=" * 70)

    logging.basicConfig(filename='contoh.log', level=logging.DEBUG,
                        format='%(asctime)s - %(levelname)s - %(message)s')

    logging.debug("Ini adalah pesan debug.")
    logging.info("Ini adalah pesan info.")
    logging.warning("Ini adalah pesan warning.")
    logging.error("Ini adalah pesan error.")
    logging.critical("Ini adalah pesan critical.")

    print("\nLog telah ditulis ke 'contoh.log'.")

# ==========================
# BAGIAN 11: STUDI KASUS (SISTEM LOGIN DAN LOG)
# ==========================

def bagian_11():
    print("=" * 70)
    print("BAGIAN 11: STUDI KASUS (SISTEM LOGIN DAN LOG)")
    print("=" * 70)

    logging.basicConfig(
        filename = 'securelog_audit_log.',
        level = logging.INFO,
        format = '%(asctime)s - %(levelname)s - %(message)s',
        force = True
    )

    users_db = {
        "admin": {"password": "Admin123", "role": "administrator"},
        "user1": {"password": "User123", "role": "user"}
    }

    class LoginGagalError(Exception):
        pass

    def login(username, password, ip):
        if username not in users_db:
            logging.warning(f"Login gagal: User '{username}' tidak ditemukan dari IP {ip}.")
            raise LoginGagalError(f"User '{username}' tidak ditemukan.")
        if users_db[username]["password"] != password:
            logging.warning(f"Login gagal: Password salah untuk user '{username}' dari IP {ip}.")
            raise LoginGagalError("Password salah.")
        logging.info(f"Login berhasil: User '{username}' berhasil login dari IP {ip}.")
        return True

    print("\n--- Simulasi Login ---")
    try:
        login("admin", "Admin123", "192.168.1.100")
    except LoginGagalError as e:
        print(f"LoginGagalError: {e}")

    try:
        login("user1", "WrongPassword", "192.168.1.100")
    except LoginGagalError as e:
        print(f"LoginGagalError: {e}")

    print("\nLog telah ditulis ke 'securelog_audit_log.'.")

# =========================
# MENU UTAMA UNTUK MEMILIH BAGIAN
# =========================

def menu_utama():
    while True:
        print("\n" + "=" * 70)
        print("MENU UTAMA - PILIH BAGIAN UNTUK DITAMPILKAN")
        print("=" * 70)
        print("1. Bagian 1: Membuat dan Mengakses Dictionary")
        print("2. Bagian 2: Operasi Dasar dan Method Dictionary")
        print("3. Bagian 3: Iterasi dan Dictionary Comprehension")
        print("4. Bagian 4: Membuat dan Mengakses Set")
        print("5. Bagian 5: Operasi Himpunan pada Set")
        print("6. Bagian 6: Perbandingan Performa (List vs Set)")
        print("7. Bagian 7: Exception Handling pada Dictionary dan Set")
        print("8. Bagian 8: Raise and Custom Exception")
        print("9. Bagian 9: Debugging dengan Assert dan Print")
        print("10. Bagian 10: Logging dengan Modul Logging")
        print("11. Bagian 11: Studi Kasus (Sistem Login dan Log)")
        print("0. Keluar")

        pilihan = input("\nMasukkan pilihan Anda (0-11): ")

        if pilihan == "1":
            bagian_1()
        elif pilihan == "2":
            bagian_2()
        elif pilihan == "3":
            bagian_3()
        elif pilihan == "4":
            bagian_4()
        elif pilihan == "5":
            bagian_5()
        elif pilihan == "6":
            bagian_6()
        elif pilihan == "7":
            bagian_7()
        elif pilihan == "8":
            bagian_8()
        elif pilihan == "9":
            bagian_9()
        elif pilihan == "10":
            bagian_10()
        elif pilihan == "11":
            bagian_11()
        elif pilihan == "0":
            print("\nTerima kasih telah menggunakan program ini.")
            break
        else:
            print("\nPilihan tidak valid. Silakan coba lagi.")

# Menjalankan Menu Utama
if __name__ == "__main__":
    menu_utama()