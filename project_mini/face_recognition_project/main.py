import tkinter as tk
from tkinter import messagebox
import util  # Import fungsi util.py untuk interaksi database
import cv2
from PIL import Image, ImageTk
import face_recognition

class App:
    def __init__(self):
        self.main_window = tk.Tk()
        self.main_window.geometry("1200x520+350+100")

        # Tombol login
        self.login_button_main_window = util.get_button(self.main_window, 'Login', 'green', self.login)
        self.login_button_main_window.place(x=750, y=200)

        # Tombol logout
        self.logout_button_main_window = util.get_button(self.main_window, 'Logout', 'red', self.logout)
        self.logout_button_main_window.place(x=750, y=300)

        # Tombol register user baru
        self.register_new_user_button_main_window = util.get_button(self.main_window, 'Register New User', 'gray', self.register_new_user, fg='black')
        self.register_new_user_button_main_window.place(x=750, y=400)

        # Label untuk menampilkan video webcam
        self.webcam_label = util.get_img_label(self.main_window)
        self.webcam_label.place(x=10, y=0, width=700, height=500)

        # Inisialisasi webcam
        self.add_webcam(self.webcam_label)

    def add_webcam(self, label):
        if 'cap' not in self.__dict__:
            self.cap = cv2.VideoCapture(0)  # Menggunakan webcam
        self._label = label
        self.process_webcam()

    def process_webcam(self):
        ret, frame = self.cap.read()
        if ret:
            self.most_recent_capture_arr = frame
            img_ = cv2.cvtColor(self.most_recent_capture_arr, cv2.COLOR_BGR2RGB)
            self.most_recent_capture_pil = Image.fromarray(img_)
            imgtk = ImageTk.PhotoImage(image=self.most_recent_capture_pil)
            self._label.imgtk = imgtk
            self._label.configure(image=imgtk)

        self._label.after(20, self.process_webcam)

    def login(self):
        face_encodings = face_recognition.face_encodings(self.most_recent_capture_arr)

        if len(face_encodings) == 0:
            util.msg_box("Error", "Tidak ada wajah terdeteksi! Coba lagi.")
            return

        face_encoding = face_encodings[0]
        user_data = util.verify_user(face_encoding)

        if user_data == 'unknown_person':
            util.msg_box("Login Error", "Wajah tidak dikenali! Silakan register terlebih dahulu.")
        else:
            user_id, name, age, address, college = user_data
            util.msg_box("Login Success", f"Selamat datang, {name}!\nID: {user_id}\nUmur: {age}\nAlamat: {address}\nKuliah: {college}")

    def logout(self):
        util.msg_box("Logout", "You have successfully logged out!")
        self.main_window.destroy()  # Menutup GUI setelah logout

    def register_new_user(self):
        register_window = tk.Toplevel(self.main_window)
        register_window.title("Register New User")
        register_window.geometry("400x400")

        # Input fields
        tk.Label(register_window, text="ID").pack()
        id_entry = tk.Entry(register_window)
        id_entry.pack()

        tk.Label(register_window, text="Name").pack()
        name_entry = tk.Entry(register_window)
        name_entry.pack()

        tk.Label(register_window, text="Umur").pack()
        age_entry = tk.Entry(register_window)
        age_entry.pack()

        tk.Label(register_window, text="Alamat").pack()
        address_entry = tk.Entry(register_window)
        address_entry.pack()

        tk.Label(register_window, text="Kuliah").pack()
        college_entry = tk.Entry(register_window)
        college_entry.pack()

        def capture_and_register():
            face_encodings = face_recognition.face_encodings(self.most_recent_capture_arr)
            if len(face_encodings) == 0:
                util.msg_box("Error", "Tidak ada wajah terdeteksi! Coba lagi.")
                return

            face_encoding = face_encodings[0]
            name = name_entry.get()
            id_value = id_entry.get()
            age = age_entry.get()
            address = address_entry.get()
            college = college_entry.get()

            if id_value and name and age and address and college:
                result = util.register_new_user(id_value, name, age, address, college, face_encoding)
                util.msg_box("Registration Result", result)
                if "successfully" in result:
                    register_window.destroy()
            else:
                util.msg_box("Error", "SEMUA KOLOM WAJIB DIISI!")

        register_button = tk.Button(register_window, text="Register", command=capture_and_register)
        register_button.pack()

    def start(self):
        self.main_window.mainloop()


if __name__ == '__main__':
    app = App()
    app.start()
