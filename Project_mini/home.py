import streamlit as st

def show_home():
    st.title("Face Recognition Histogram of Oriented Gradient")

    st.markdown(
        """
        Aplikasi ini menggunakan metode Histogram of Oriented Gradients (HOG) untuk mengenali wajah. HOG adalah teknik pengolahan citra yang sangat efektif untuk mendeteksi objek, terutama wajah, dengan memanfaatkan fitur-fitur orientasi dari gradient intensitas pada gambar.

       ### Pendahuluan

        Kegiatan perkuliahan tidak terlepas dari proses absensi yang merupakan bagian penting dalam mencatat kehadiran mahasiswa. Absensi yang akurat sangat diperlukan untuk memastikan mahasiswa hadir dalam setiap sesi kuliah, serta untuk mendukung pengelolaan akademik yang lebih baik. Namun, metode absensi konvensional seperti daftar hadir manual sering kali menimbulkan berbagai kendala, seperti kecurangan, keterlambatan, dan kesulitan dalam pengolahan data kehadiran.

        Untuk mengatasi masalah tersebut, aplikasi "Face Recognition Histogram of Oriented Gradient" hadir sebagai solusi inovatif. Dengan memanfaatkan teknologi pengenalan wajah, aplikasi ini memungkinkan proses absensi dilakukan secara otomatis dan efisien. Melalui pengenalan wajah yang akurat, aplikasi ini tidak hanya meningkatkan keandalan data kehadiran tetapi juga memberikan kemudahan bagi mahasiswa dan pengajar dalam melakukan pencatatan kehadiran.

        
       ### AI Project Cycle

        1. **Problem Scoping**: Mengembangkan sistem pengenalan wajah untuk absensi otomatis guna meningkatkan efisiensi dan akurasi kehadiran mahasiswa.
   
        2. **Data Acquisition**:gambar wajah setiap mahasiswa di ambil secara manual menggunakan webcam dan mengisi informasi profil melalui formulir Register.

        3. **Data Exploration**: menggunakan webscam untuk mengambil gambar pada area wajah untuk membantu mengidentifikasi objek.

        4. **Modeling**: Menggunakan Histogram of Oriented Gradient untuk ekstraksi fitur dan menerapkan algoritma klasifikasi KNN untuk pengenalan wajah.

        5. **Evaluasi**:Di uji pada pada 5 wajah yang berbeda dan model dengan tepat mencocokan wajah,model Mengukur akurasi dengan metrik seperti precision

        6. **Deployment**: Membangun aplikasi web menggunakan Streamlit, OpenCV, NumPy, scikit-image dan MySQL Connector.
    
        ### Cara Kerja Aplikasi:
        1. **Registrasi**: Pengguna dapat mendaftar dengan mengambil foto wajah. Aplikasi ini akan menangkap wajah  untuk meningkatkan akurasi pengenalan.
        2. **Login**: Setelah registrasi, pengguna dapat melakukan login dengan mengambil foto wajah mereka. Sistem akan membandingkan wajah yang diambil dengan data yang tersimpan dalam database.
        3. **Pengenalan Wajah**: Jika wajah yang diambil sesuai dengan data yang ada, aplikasi akan menampilkan informasi pengguna seperti nama, umur, alamat, dan institusi pendidikan, serta mencatat kehadiran pengguna.
    
        """,
        unsafe_allow_html=True
    )
