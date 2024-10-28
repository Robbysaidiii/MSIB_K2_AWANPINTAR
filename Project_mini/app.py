import streamlit as st
import cv2
import numpy as np
from HOG import compute_hog_features  # Mengimpor fungsi HOG dari HOG.py
from FaceBase import verify_user, register_new_user  # Mengimpor fungsi dari FaceBase.py
from home import show_home  # Mengimpor fungsi dari home.py

# CSS untuk mengatur gambar kiri dan kanan dengan Flexbox
st.markdown(
    """
    <style>
    .container {
        display: flex;
        justify-content: space-between;
        align-items: center;
        width: 100%;
    }
    .left-img {
        width: 100px;
    }
    .right-img {
        width: 100px;
        margin-right: 50px;  /* Tambahkan margin untuk menggeser lebih ke kanan */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Menampilkan gambar Orbit di kiri dan km di kanan dengan tata letak Flexbox
st.markdown("<div class='container'>", unsafe_allow_html=True)

# Gunakan st.image() untuk menampilkan gambar dengan lebar 100px
col1, col2, col3 = st.columns([1, 2, 1])  # Mengatur tiga kolom untuk memberikan jarak lebih besar ke kanan
with col1:
    st.image('images/Orbit.png', width=100)  # Ganti jalur jika diperlukan
with col3:  # Menggunakan kolom ke-3 agar lebih ke kanan
    st.image('images/km.png', width=100)  # Ganti jalur jika diperlukan

st.markdown("</div>", unsafe_allow_html=True)

# Cek apakah `page` ada di session_state; jika tidak, set default ke "Home"
if "page" not in st.session_state:
    st.session_state.page = "Home"

# Menambahkan sidebar untuk navigasi antar halaman
st.sidebar.title("Kelompok4")
page = st.sidebar.selectbox("Pilih Halaman", ["Home", "Login", "Register", "Logout"], key="page_selectbox")

if page != st.session_state.page:
    st.session_state.page = page

# Halaman Home
if st.session_state.page == "Home":
    show_home()  # Panggil fungsi untuk menampilkan halaman home

# Halaman Login
elif st.session_state.page == "Login":
    st.title("Halaman Login")
    st.write("Silakan gunakan webcam Anda untuk login.")

    # Menggunakan Streamlit camera input
    enable_camera = st.checkbox("Enable camera", key="login_camera_checkbox")
    picture = st.camera_input("Take a picture", disabled=not enable_camera, key="login_camera_input")

    if picture:
        # Menampilkan gambar tangkapan
        st.image(picture, caption="Gambar Tangkapan", use_column_width=True)

        # Mengkonversi gambar dari Streamlit ke format OpenCV
        image_bytes = picture.getvalue()
        nparr = np.frombuffer(image_bytes, np.uint8)
        frame = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

        # Komputasi HOG untuk frame yang diambil
        hog_features = compute_hog_features(frame)

        # Verifikasi pengguna
        user_info = verify_user(hog_features)
        if user_info != 'unknown_person':
            user_id, name, age, address, college = user_info
            st.success(f"Wajah dikenali ")
            st.write("Informasi User:")
            st.write(f"**Nama:** {name}")
            st.write(f"**Umur:** {user_id}")
            st.write(f"**Alamat:** {age}")
            st.write(f"**Kuliah:** {address}")
            st.write(f"**Kuliah:** {college}")
        else:
            st.error("Wajah tidak dikenali!")

# Halaman Register
elif st.session_state.page == "Register":
    st.title("Halaman Register")
    st.write("Silakan isi form untuk mendaftar.")

    user_id = st.text_input("ID", key="register_user_id")
    name = st.text_input("Nama", key="register_name")
    age = st.number_input("Umur", min_value=0, key="register_age")
    address = st.text_input("Alamat", key="register_address")
    college = st.text_input("Kuliah", key="register_college")

    # Menggunakan Streamlit camera input untuk registrasi
    enable_camera = st.checkbox("Enable camera", key="register_camera_checkbox")
    picture = st.camera_input("Take a picture", disabled=not enable_camera, key="register_camera_input")

    if picture:
        # Menampilkan gambar tangkapan
        st.image(picture, caption="Gambar Tangkapan", use_column_width=True)

        # Mengkonversi gambar dari Streamlit ke format OpenCV
        image_bytes = picture.getvalue()
        nparr = np.frombuffer(image_bytes, np.uint8)
        frame = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

        # Komputasi HOG untuk gambar yang diambil
        hog_features = compute_hog_features(frame)

        # Simpan fitur HOG ke database
        result = register_new_user(user_id, name, age, address, college, hog_features)
        st.success(result)

# Halaman Logout
elif st.session_state.page == "Logout":
    st.title("Anda telah logout")
    st.write("Anda telah keluar dari akun Anda.")
    st.session_state.page = "Home"  # Mengatur kembali ke halaman Home setelah logout
