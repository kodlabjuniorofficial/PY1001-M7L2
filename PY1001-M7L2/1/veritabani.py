import sqlite3

def barinak_veritabani_hazirla():
    conn = sqlite3.connect("barinak.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS hayvanlar (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ad TEXT,
            tur TEXT,
            renk TEXT,
            yas INTEGER,
            gorsel_yolu TEXT,
            aclik INTEGER,
            uyku INTEGER,
            mutluluk INTEGER
        )
    """)
    conn.commit()
    conn.close()

class EvcilHayvan:
    def __init__(self, id_no, ad, tur, renk, yas, gorsel_yolu, aclik, uyku, mutluluk):
        self.id_no = id_no
        self.ad = ad
        self.tur = tur
        self.renk = renk
        self.yas = yas
        self.gorsel_yolu = gorsel_yolu
        self.aclik = aclik       
        self.uyku = uyku         
        self.mutluluk = mutluluk 

    def veritabani_guncelle(self):
        conn = sqlite3.connect("barinak.db")
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE hayvanlar SET aclik = ?, uyku = ?, mutluluk = ? WHERE id = ?
        """, (self.aclik, self.uyku, self.mutluluk, self.id_no))
        conn.commit()
        conn.close()

    # --- 2. AŞAMA GÖREVLERİ ---
    def besle(self):
        # GÖREV 1: Açlığı 20 azaltın (en az 0), mutluluğu 5 artırın (en fazla 100).
        # Güncelleme metodunu tetikleyin.
        # BURAYA KOD GELECEK
        pass

    def uyut(self):
        # GÖREV 2: Uykuyu 30 azaltın, açlığı 10 artırın. Veritabanını güncelleyin.
        # BURAYA KOD GELECEK
        pass

    def oyun_oyna(self):
        # GÖREV 3: Mutluluğu 25 artırın, açlık ve uykuyu 15 artırın. Veritabanını güncelleyin.
        # BURAYA KOD GELECEK
        pass

    def ses_ver(self):
        return "Genel hayvan sesi! 🐾"

# GÖREV 4: EvcilHayvan'dan miras alan Kedi, Kopek ve Ejderha sınıflarını kurun.
# ses_ver() metotlarını Overriding tekniği ile ezin.
# BURAYA KOD GELECEK

barinak_veritabani_hazirla()