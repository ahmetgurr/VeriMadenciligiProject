# VERİ MADENCİLİĞİ
## Çalışma ekibi
 - Ahmet GÜR      - 02200201053
 - Dilara KARATAŞ - 02200201044
 - Burak KUTLUK   - 02200201040
 - Ayşe DEVEDEN   - 02200201081
 - Ahmet TAKCI    - 02200201055


## Proje Konusu 
Veri Madenciliği İle Müşteri Davranışlarının Analizi: Perakende Sektöründe Bir İnceleme
## Proje Özeti
Bu proje, perakende sektöründe veri madenciliği tekniklerinin kullanılmasıyla müşteri davranışlarının derinlemesine analizini amaçlamaktadır. İlgili veri setleri üzerinde yapılacak analizler, müşteri tercihlerini anlamak, alışveriş alışkanlıklarını belirlemek ve öngörüsel analizlerle gelecekteki trendleri tahmin etmek için kullanılacaktır. Veri madenciliği algoritmaları aracılığıyla elde edilen bilgiler, perakende işletmelerine stratejik kararlar alabilmeleri için değerli bir temel sağlayacaktır. Bu çalışma, müşteri memnuniyetini artırmak, stok yönetimini optimize etmek ve satışları artırmak gibi perakende sektöründeki önemli konulara odaklanarak veri madenciliği uygulamalarının iş dünyasına katkısını ele almaktadır.


## Output
Accuracy: 0.875

Tahmin Tablosu:
   Gerçek Ürün Tahmin Edilen Ürün
30  Elektronik         Elektronik
0   Elektronik         Elektronik
22       Giyim              Giyim
31       Giyim              Giyim
18  Elektronik         Elektronik
28       Giyim               Gıda
10        Gıda               Gıda
70       Giyim         Elektronik
4   Elektronik         Elektronik
12       Giyim              Giyim
49        Gıda               Gıda
33        Gıda               Gıda
67  Elektronik         Elektronik
35  Elektronik         Elektronik
68  Elektronik         Elektronik
45  Elektronik         Elektronik

En Çok Tercih Edilen Ürün: Elektronik

Alışveriş Analizi:
              ToplamTutar  ÜrünMiktarı
ÜrünKategori
Elektronik        34000.0           55
Giyim             13850.0           64
Gıda               6360.0           89

Bir Sonraki Ay İçin Tahmin Edilen Ürün: Elektronik


## K-means (Kümeleme Algoritması)
Bu algoritma denetimsiz öğrenme için kullanılan bir makine öğrenimi algoritmasıdır. Veri noktalarının benzerliğine dayalı olarak verileri önceden tanımlanmış sayıda küme (k) içinde gruplama yöntemidir. 
K-means algoritması için aşağıdaki adımları gerçekleştirilir; 
1.	Başlangıçta, k küme merkezi rastgele seçilir.
2.	Her veri noktası, ona en yakın küme merkezine atanır.
3.	Her küme için yeni bir merkez hesaplanır (küme elemanlarının ortalaması alınır).
4.	Küme merkezleri artık değişmiyorsa veya belirli bir iterasyon sayısına ulaşıldıysa algoritma sona erer; aksi halde, adımlar 2-3 tekrarlanır.
5.	Sonuç olarak, veri noktaları k kümesine atanmış olur.
