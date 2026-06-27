# 📚 Dataset: TinyStories

Folder ini diperuntukkan sebagai tempat penyimpanan dataset lokal yang digunakan sebagai referensi konteks pada proses pembuat cerita (*inference*) oleh model bahasa **TinyLlama-1.1B-Chat-v1.0** di dalam aplikasi **AI Creative Studio**.

## 📌 Sumber Dataset
*   **Nama Dataset:** `roneneldan/TinyStories`
*   **Sumber Asli:** [HuggingFace - TinyStories](https://huggingface.co/datasets/roneneldan/TinyStories)
*   **Jenis Data:** *Text Corpus* (Kumpulan teks cerita pendek untuk anak)
*   **Jumlah Data Total:** ~2,11 Juta baris cerita.

Dataset ini berisi cerita pendek yang digenerasi oleh AI (sebagian besar oleh GPT-3.5/GPT-4) yang menggunakan kosakata sederhana. Dalam tugas besar ini, kami tidak melakukan *training* ulang, melainkan menggunakan sampel teks dari dataset ini untuk memberikan contoh kepada TinyLlama (metode *Retrieval-Augmented Generation/Context Injection*).

## 🗂️ Struktur File
Karena ukuran dataset sangat besar, kami **tidak** mengunggah file data mentah (`stories.csv`) ke dalam repositori ini agar tidak membebani kapasitas GitHub. 

Format tabel akhir yang diharapkan di dalam file `stories.csv` ketika sudah terunduh adalah sebagai berikut:
| text |
| :--- |
| "Once upon a time, there was a little girl named Lily. She loved to play outside..." |
| "A big brown bear lived in the forest. He was very hungry..." |

## 🚀 Cara Mengunduh & Menyiapkan Dataset
Untuk menjalankan aplikasi ini di komputer lokal, kamu **wajib** mengunduh dataset dan menyimpannya di folder ini terlebih dahulu. Ikuti langkah berikut:

1. Pastikan kamu berada di *root* folder/direktori proyek (di luar folder `dataset`).
2. Instal library yang dibutuhkan untuk mengunduh:
   ```bash
   pip install datasets pandas
