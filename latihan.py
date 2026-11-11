import logging
import time

# =================================
# BAGIAN 1: MANAJEMEN USER (DICTIONARY)
# =================================

def bagian1():
    print("=" * 70)
    print("BAGIAN 1: MANAJEMEN USER (DICTIONARY)")
    print("=" * 70)

    database_user = {
        "admin": {"password": "admin123", "role": "admin", "status": "active", "ip": "192.168.101"},
        "user1": {"password": "user123", "role": "user", "status": "active", "ip": "192.1.168.101"},
        "security": {"password": "security123", "role": "security", "status": "active", "ip": "192.168.102"},
    }

    print(f"\n[info] Database User Awal: {database_user}")

    print("\n--- Menampilkan Detail user ---")
    for username, info in database_user.items():
        print(f"Username: {username}")
        print(f"Password : {info['password']}")
        print(f"Role     : {info['role']}")
        print(f"Status   : {info['status']}")
        print(f"IP       : {info['ip']}")

    user_dihapus = "user1"
    data_dihapus = database_user.pop(user_dihapus, None)
    print(f"\n[info] User '{user_dihapus}' telah dihapus dari database.")
    print(f"[info] Data yang dihapus: {data_dihapus}")

    database_user.update({
        "auditor": {
            "password": "auditor123",
            "role": "auditor",
            "status": "active",
            "ip": "192.168.103"
        }
    })
    print(f"\n[info] User 'auditor' telah ditambahkan ke database.")

    print(f"\n[info] Database User Terbaru (Total User: {len(database_user)}):")
    for username, info in database_user.items():
        print(f"Username: {username}")
        print(f"Password : {info['password']}")
        print(f"Role     : {info['role']}")
        print(f"Status   : {info['status']}")
        print(f"IP       : {info['ip']}")
        print("=" * 70)
