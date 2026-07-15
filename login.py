import logging
from flask import Flask, jsonify, request
from flask_cors import CORS

# Setup logging agar bisa memantau request di terminal
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)
CORS(app)  # Mengizinkan akses dari aplikasi frontend lain

# Database user tiruan
DATABASE_USERS = {"admin": "12345", "member": "password123"}


@app.route("/login", methods=["POST"])
def auth_login():
    logger.info("Menerima request login...")

    # Mengambil data JSON yang dikirim oleh client
    data = request.get_json() or {}
    username = data.get("username")
    password = data.get("password")

    # Proses Pengecekan
    if (
        username in DATABASE_USERS
        and DATABASE_USERS[username] == password
    ):
        logger.info(f"User '{username}' berhasil login.")
        return (
            jsonify(
                {
                    "status": "success",
                    "message": "Login berhasil!",
                    "user": username,
                }
            ),
            200,
        )

    logger.warning(f"Gagal login untuk username: '{username}'")
    return (
        jsonify(
            {"status": "error", "message": "Username atau password salah!"}
        ),
        401,
    )


if __name__ == "__main__":
    # Berjalan di http://127.0.0.1:5000
    app.run(debug=True)

# Database tiruan berupa dictionary (username: password)
database_users = {"admin": "12345", "user_baru": "pass123"}


def login():
    print("=== SISTEM LOGIN PYTHON ===")

    # Mengambil input dari user
    username = input("Masukkan Username: ")
    password = input("Masukkan Password: ")

    # Validasi cek apakah username ada di database dan password-nya cocok
    if username in database_users and database_users[username] == password:
        print("\n[SUKSES] Login berhasil! Selamat datang,", username)
    else:
        print("\n[GAGAL] Username atau password salah.")


# Menjalankan fungsi login
if __name__ == "__main__":
    login()

