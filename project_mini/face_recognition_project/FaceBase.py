import mysql.connector
import pickle
import face_recognition

def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",  # Sesuaikan dengan username MySQL Anda
        password="",  # Sesuaikan dengan password MySQL Anda
        database="facebase"  # Pastikan nama database sesuai
    )

def register_new_user(user_id, name, age, address, college, face_encoding):
    conn = connect_db()
    cursor = conn.cursor()

    face_encoding_serialized = pickle.dumps(face_encoding)

    try:
        cursor.execute(
            "INSERT INTO user (id, nama, umur, alamat, kuliah, face_encoding) VALUES (%s, %s, %s, %s, %s, %s)",
            (user_id, name, age, address, college, face_encoding_serialized)
        )
        conn.commit()
        return f"User {name} registered successfully!"
    except mysql.connector.IntegrityError:
        return "ID already exists!"
    except Exception as e:
        return f"Error registering user: {e}"
    finally:
        cursor.close()
        conn.close()

def verify_user(face_encoding):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT id, nama, umur, alamat, kuliah, face_encoding FROM user")
    users = cursor.fetchall()

    for user in users:
        user_id, name, age, address, college, db_face_encoding = user
        db_face_encoding = pickle.loads(db_face_encoding)

        results = face_recognition.compare_faces([db_face_encoding], face_encoding)
        if results[0]:
            return user_id, name, age, address, college

    return 'unknown_person'
