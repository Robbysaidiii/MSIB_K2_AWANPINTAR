import mysql.connector
import numpy as np

def connect_to_database():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="facebase"
    )

def register_new_user(user_id, name, age, address, college, hog_features):
    conn = connect_to_database()
    cursor = conn.cursor()
    
    # Pastikan hanya menyimpan hog_features
    cursor.execute("INSERT INTO user (id, nama, umur, alamat, kuliah, hog_features) VALUES (%s, %s, %s, %s, %s, %s)",
                   (user_id, name, age, address, college, hog_features.tobytes()))  # Simpan sebagai bytes
    conn.commit()
    cursor.close()
    conn.close()
    return "Registrasi berhasil!"

def verify_user(hog_features):
    conn = connect_to_database()
    cursor = conn.cursor()
    
    cursor.execute("SELECT id, nama, umur, alamat, kuliah, hog_features FROM user")
    results = cursor.fetchall()
    
    for row in results:
        user_id, name, age, address, college, stored_hog_features = row
        stored_hog_features = np.frombuffer(stored_hog_features, dtype=np.float64)  # Memastikan dtype sesuai
        
        # Hitung jarak antara fitur HOG login dan fitur yang disimpan
        distance = np.linalg.norm(hog_features - stored_hog_features)
        
        if distance < 10:  # Misalnya threshold 10
            return user_id, name, age, address, college  # Kembalikan informasi pengguna

    return 'unknown_person'
