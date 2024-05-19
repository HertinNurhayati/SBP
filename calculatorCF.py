# Dictionary untuk menyimpan nilai user (MB) dan nilai pakar (MD) untuk setiap gejala
gejala_data = {
    "G01": {"nilai_user": 1, "nilai_pakar": 0.8},
    "G02": {"nilai_user": 0.8, "nilai_pakar": 1},
    "G03": {"nilai_user": 0.6, "nilai_pakar": 0.8},
    "G04": {"nilai_user": 0.8, "nilai_pakar": 1},
    "G05": {"nilai_user": 1, "nilai_pakar": 0.8},
    "G06": {"nilai_user": 0.6, "nilai_pakar": 0.8},
    "G07": {"nilai_user": 0.8, "nilai_pakar": 1},
    "G08": {"nilai_user": 1, "nilai_pakar": 0.8},
    "G09": {"nilai_user": 0.8, "nilai_pakar": 0.6},
    "G10": {"nilai_user": 0.6, "nilai_pakar": 0.6},
    "G11": {"nilai_user": 0.6, "nilai_pakar": 0.8},
    "G12": {"nilai_user": 0.8, "nilai_pakar": 0.8},
    "G13": {"nilai_user": 1, "nilai_pakar": 0.8},
    "G14": {"nilai_user": 0.4, "nilai_pakar": 1},
    "G15": {"nilai_user": 0.8, "nilai_pakar": 0.8},
    "G16": {"nilai_user": 0.6, "nilai_pakar": 0.8},
    "G17": {"nilai_user": 0.8, "nilai_pakar": 0.8},
    "G18": {"nilai_user": 0.8, "nilai_pakar": 0.6},
    "G19": {"nilai_user": 0.4, "nilai_pakar": 0.8},
    "G20": {"nilai_user": 0.8, "nilai_pakar": 0.8},
    "G21": {"nilai_user": 0.6, "nilai_pakar": 0.8},
    "G22": {"nilai_user": 0.6, "nilai_pakar": 0.6},
    "G23": {"nilai_user": 0.8, "nilai_pakar": 0.6},
    "G24": {"nilai_user": 0.6, "nilai_pakar": 0.8},
    "G25": {"nilai_user": 0.8, "nilai_pakar": 0.8},
    "G26": {"nilai_user": 0.6, "nilai_pakar": 0.8},
    "G27": {"nilai_user": 0.6, "nilai_pakar": 0.6},
    "G28": {"nilai_user": 0.4, "nilai_pakar": 0.8},
    "G29": {"nilai_user": 0.6, "nilai_pakar": 0.6},
    "G30": {"nilai_user": 0.8, "nilai_pakar": 0.8}
}

# Dictionary untuk menyimpan kode kerusakan dan gejala yang terkait
kode_gejala = {
    "K1": ["G01", "G08", "G15", "G23"],
    "K2": ["G02", "G09", "G16", "G24", "G29"],
    "K3": ["G03", "G10", "G17", "G22", "G25", "G30"],
    "K4": ["G04", "G11", "G18", "G26"],
    "K5": ["G05", "G12", "G19", "G27"],
    "K6": ["G06", "G13", "G20", "G28"],
    "K7": ["G07", "G14", "G21"]
}

# Fungsi untuk menghitung nilai CF kombinasi
def hitung_CF(kode_kerusakan):
    cf_kombinasi = 1
    for gejala in kode_gejala[kode_kerusakan]:
        cf_kombinasi *= gejala_data[gejala]["nilai_user"]
    return cf_kombinasi

# Fungsi untuk menampilkan hasil perhitungan CF kombinasi
def tampilkan_hasil_CF():
    print("Kode Kerusakan\tNilai CF Kombinasi\tPersentase")
    for kode_kerusakan in kode_gejala:
        cf_kombinasi = hitung_CF(kode_kerusakan)
        persentase = cf_kombinasi * 100
        print(f"{kode_kerusakan}\t\t{cf_kombinasi:.10f}\t\t{persentase:.1f}%")

# Tampilkan hasil perhitungan CF kombinasi
tampilkan_hasil_CF()
