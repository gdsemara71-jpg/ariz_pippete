# 🌿 A Riz Pippete — Eco Premium Website

Website brand ramah lingkungan **A Riz Pippete** — dibangun dengan Flask, HTML/CSS/JS modern.

---

## 🚀 Cara Menjalankan

### 1. Pastikan Python sudah terinstall
```bash
python --version
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Jalankan aplikasi
```bash
python app.py
```

### 4. Buka di browser
```
http://localhost:5000
```

---

## 📁 Struktur Folder

```
ariz_pippete/
├── app.py                  # Flask backend
├── requirements.txt        # Python dependencies
├── README.md
├── templates/
│   └── index.html          # Halaman utama
└── static/
    ├── css/
    │   └── style.css       # Stylesheet utama
    ├── js/
    │   └── main.js         # JavaScript utama
    ├── images/             # (tambahkan gambar produk di sini)
    └── video/              # (tambahkan video eco di sini)
```

---

## 🎨 Fitur Website

- ✅ **Navbar transparan** dengan glassmorphism saat scroll
- ✅ **Hero section** dengan background video + overlay
- ✅ **Custom cursor** dengan glow effect
- ✅ **Loading screen** animasi modern
- ✅ **Eco particles** canvas floating
- ✅ **Parallax** ringan di hero
- ✅ **Scroll reveal** animasi per section
- ✅ **Counter animasi** (statistik about)
- ✅ **Product cards** dengan hover zoom premium
- ✅ **Masonry gallery** dengan lightbox preview
- ✅ **Contact form** dengan AJAX (Flask backend)
- ✅ **Mobile menu** fullscreen animasi
- ✅ **Fully responsive** (desktop, tablet, mobile)
- ✅ **Footer** lengkap dengan social media

---

## 🌿 Produk

| Produk | Deskripsi |
|---|---|
| Pipet Beras | Batang padi alami, biodegradable 100% |
| Pipet Bambu | Bambu pilihan, reusable |
| Pipet Besi | Stainless steel food-grade |
| Totebag Kertas | Kraft paper premium |
| Gelas Kertas | Biodegradable food-grade |
| Jaket Bambu | Serat bambu organik |

---

## 🖼️ Menambahkan Gambar & Video

**Gambar produk** → simpan di `static/images/`  
**Video hero** → simpan di `static/video/hero.mp4`

Lalu update src di `templates/index.html`:
```html
<!-- Video -->
<source src="{{ url_for('static', filename='video/hero.mp4') }}" type="video/mp4" />

<!-- Gambar produk (ganti SVG placeholder) -->
<img src="{{ url_for('static', filename='images/pipet-beras.jpg') }}" alt="Pipet Beras" />
```

---

## ✏️ Kustomisasi

Edit variabel CSS di `static/css/style.css`:
```css
:root {
  --forest: #1a2e1a;   /* Hijau tua utama */
  --clay:   #c4956a;   /* Aksen earth tone */
  --cream:  #f5f0e8;   /* Background cream */
  /* ... dst */
}
```

---

*Made with 🌿 for a better earth — A Riz Pippete*
