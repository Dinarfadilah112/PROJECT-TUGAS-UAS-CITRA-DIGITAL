# PROJECT-TUGAS-UAS-CITRA-DIGITAL
🛠️ Persiapan Awal (Prasyarat)
Sebelum menjalankan kode, pastikan pengguna telah menyiapkan hal berikut:

File Proyek: Pastikan folder di Google Drive berisi file-file berikut:

SISTEM_TULISAN_TANGAN_CNN.ipynb (Notebook utama) (ini tidak usah di import ke folder google drive, langsung saja open di google colab)

train.py (Skrip pelatihan model)

gradio_app.py (Skrip antarmuka web)

model_utils.py (Fungsi pembantu pengolahan citra)

Struktur Folder: Simpan semua file di dalam folder Google Drive dengan path: /MyDrive/citra digital/.


<img width="1349" height="753" alt="Screenshot 2026-01-06 at 15 50 22" src="https://github.com/user-attachments/assets/c47fbd82-4470-4c2e-95fb-7cf787587702" />


Hardware Accelerator: Di Google Colab, masuk ke menu Runtime > Change runtime type > pilih T4 GPU.

<img width="1558" height="316" alt="Screenshot 2026-01-05 at 20 47 13" src="https://github.com/user-attachments/assets/e7584970-c983-4eb9-8bdb-ceb8847891e7" />

🚀 Langkah-Langkah Menjalankan
1. Menghubungkan Google Drive
Jalankan cell pertama untuk memberikan akses ke Google Drive agar Colab bisa membaca skrip Python dan menyimpan model hasil pelatihan.

2. Instalasi Library & Persiapan Data
Instalasi: Jalankan cell !pip install emnist untuk memasang pustaka dataset.
Pembersihan Cache: Jika sebelumnya pernah gagal mengunduh data, jalankan cell pembersihan cache agar folder dataset kembali bersih.
Unduh Dataset: Jalankan cell !wget untuk mengunduh dataset EMNIST secara manual ke sistem Colab guna memastikan data tersedia.

3. Melatih Model (Training)
Jalankan cell yang berisi perintah:
!python train.py

Proses: Model akan dilatih selama 10 epoch.
Target: Akurasi akhir diharapkan mencapai kisaran 90% pada data pelatihan.
Output: Setelah selesai, file model_emnist.h5 akan muncul di folder Drive Anda.

4. Menjalankan Aplikasi Web
Jalankan cell terakhir untuk membuka antarmuka prediksi:
!python gradio_app.py

Akses: Setelah muncul pesan sukses, klik Public URL (contoh: https://xxxx.gradio.live).
Uji Coba: Gambar karakter apa saja pada kanvas yang disediakan, lalu sistem akan menampilkan hasil prediksinya secara otomatis.

⚠️ Catatan Penting
Interupsi: Jika ingin menghentikan aplikasi Gradio, Anda bisa menekan tombol stop pada cell atau memberikan perintah interupsi keyboard di Colab.
GPU: Tanpa mengaktifkan GPU, proses pelatihan (train.py) akan memakan waktu jauh lebih lama.
