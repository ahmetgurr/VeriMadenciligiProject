import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics

# Veri setini yükleme
data = pd.read_csv('musteri_veri_seti.csv')

# Bağımsız değişkenleri seçme
X = data[['Yaş', 'ÜrünMiktarı', 'ToplamTutar']]

# Hedef değişkeni seçme
y = data['ÜrünKategori']

# Eğitim ve test verilerini ayırma
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Karar ağacı modelini oluşturma
model = DecisionTreeClassifier()

# Modeli eğitme
model.fit(X_train, y_train)

# Test verileri ile tahmin yapma
y_pred = model.predict(X_test)

# Modelin performansını değerlendirme
accuracy = metrics.accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy}")

# Tahmin edilen sınıfları içeren bir tablo oluşturma
prediction_table = pd.DataFrame({'Gerçek Ürün': y_test, 'Tahmin Edilen Ürün': y_pred})

# Tabloyu ekrana yazdırma
print("\nTahmin Tablosu:")
print(prediction_table)

# En çok tercih edilen ürünü belirleme
en_cok_tercih_edilen_urun = prediction_table['Tahmin Edilen Ürün'].mode().iloc[0]
print(f"\nEn Çok Tercih Edilen Ürün: {en_cok_tercih_edilen_urun}")

# Alışveriş analizini belirleme
alisveris_analizi = data.groupby('ÜrünKategori').agg({'ToplamTutar': 'sum', 'ÜrünMiktarı': 'sum'})
print("\nAlışveriş Analizi:")
print(alisveris_analizi)

