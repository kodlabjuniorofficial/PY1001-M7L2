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
        self.id_no = id_no; self.ad = ad; self.tur = tur; self.renk = renk; self.yas = yas
        self.gorsel_yolu = gorsel_yolu; self.aclik = aclik; self.uyku = uyku; self.mutluluk = mutluluk 
    def veritabani_guncelle(self):
        conn = sqlite3.connect("barinak.db"); cursor = conn.cursor()
        cursor.execute("UPDATE hayvanlar SET aclik=?, uyku=?, mutluluk=? WHERE id=?", (self.aclik, self.uyku, self.mutluluk, self.id_no))
        conn.commit(); conn.close()
    def besle(self): self.aclik = max(0, self.aclik - 20); self.mutluluk = min(100, self.mutluluk + 5); self.veritabani_guncelle()
    def uyut(self): self.uyku = max(0, self.uyku - 30); self.aclik = min(100, self.aclik + 10); self.veritabani_guncelle()
    def oyun_oyna(self): self.mutluluk = min(100, self.mutluluk + 25); self.aclik = min(100, self.aclik + 15); self.uyku = min(100, self.uyku + 15); self.veritabani_guncelle()
    def ses_ver(self): return "Genel hayvan sesi! 🐾"

class Kedi(EvcilHayvan):
    def ses_ver(self): return f"🐈 {self.ad}: Miyav! Beni çok iyi besliyorsun! Purr..."
class Kopek(EvcilHayvan):
    def ses_ver(self): return f"🦮 {self.ad}: Hav hav! Kuyruğumu sallıyorum, hadi oyun oynayalım!"
class Ejderha(EvcilHayvan):
    def ses_ver(self): return f"🐉 {self.ad}: Kükredi! Ekrana doğru küçük bir alev üfledi! 🔥"

def yeni_hayvan_ekle(ad, tur, renk, yas, gorsel_yolu):
    conn = sqlite3.connect("barinak.db")
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO hayvanlar (ad, tur, renk, yas, gorsel_yolu, aclik, uyku, mutluluk) 
        VALUES (?, ?, ?, ?, ?, 50, 50, 50)
    """, (ad, tur, renk, yas, gorsel_yolu))
    conn.commit()
    conn.close()

# --- 4. AŞAMA: BÜYÜK DÖNÜŞÜM VE FETCHALL ---
def tum_hayvanlari_nesne_olarak_getir():
    # GÖREV 1: Veritabanına bağlanıp tüm hayvanları SELECT * FROM sorgusuyla çekin.
    # satirlar = cursor.fetchall() komutunu kullanın. Bağlantıyı kapatın.
    # BURAYA KOD GELECEK
    
    nesneler = []
    
    # GÖREV 2: BÜYÜK AYRIŞTIRMA (Unpacking)
    # satirlar listesinin içinde for döngüsüyle dönün. 
    # Her satırdan gelen 9 sütun değerini değişkenlere bölün!
    # for satir in satirlar:
    #     h_id, ad, tur, renk, yas, gorsel, aclik, uyku, mutluluk = satir
        
    # GÖREV 3: KARAR MEKANİZMASI (OOP Tür Ataması)
    # Eğer hayvanın türü "Kedi" ise nesneler listesine bir Kedi() nesnesi ekleyin.
    # Eğer "Köpek" ise Kopek() nesnesi, değilse Ejderha() nesnesi ekleyin!
    # BURAYA KOD GELECEK
        
    return nesneler

barinak_veritabani_hazirla()