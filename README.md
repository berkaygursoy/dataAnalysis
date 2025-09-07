# Titanic Veri Analizi

Bu proje, Titanic kazasında yolcuların hayatta kalma oranlarını analiz eden bir Python uygulamasıdır. Cinsiyet, sınıf ve yaş gibi faktörlere göre hayatta kalma oranlarını görselleştirir.

## Proje Açıklaması

Titanic veri seti, 1912 yılında Titanic gemi kazasında yolcuların hayatta kalma durumlarını içeren ünlü bir veri setidir. Bu proje, aşağıdaki faktörlere göre hayatta kalma oranlarını analiz eder:

- Cinsiyete göre hayatta kalma oranları
- Sınıfa göre hayatta kalma oranları
- Yolcuların yaş dağılımı

## Kullanılan Teknolojiler

- Python 3.x
- Pandas (Veri manipülasyonu için)
- NumPy (Sayısal hesaplamalar için)
- Matplotlib (Grafik çizimi için)
- Seaborn (İstatistiksel grafikler için)

## Kurulum

Gerekli kütüphaneleri yüklemek için:

```bash
pip install pandas numpy matplotlib seaborn
```

## Kullanım

Projeyi çalıştırmak için:

```bash
python analysis.py
```

## Veri Seti

Proje, `train.csv` adlı dosyada bulunan Titanic yolcu verilerini kullanır. Bu veri seti aşağıdaki bilgileri içerir:

- Yolcu kimlik numarası (PassengerId)
- Hayatta kalma durumu (Survived)
- Yolcu sınıfı (Pclass)
- İsim (Name)
- Cinsiyet (Sex)
- Yaş (Age)
- Kardeş/eş sayısı (SibSp)
- Ebeveyn/çocuk sayısı (Parch)
- Bilet numarası (Ticket)
- Ücret (Fare)
- Kabin numarası (Cabin)
- Biniş limanı (Embarked)

## Görselleştirmeler

Proje üç farklı görselleştirme sunar:

1. **Cinsiyete Göre Hayatta Kalma Oranı**: Kadın ve erkek yolcuların hayatta kalma oranlarını karşılaştırır.
2. **Sınıfa Göre Hayatta Kalma Oranı**: 1., 2. ve 3. sınıf yolcuların hayatta kalma oranlarını gösterir.
3. **Yaş Dağılımı**: Yolcuların yaş dağılımını histogram ve yoğunluk eğrisi ile gösterir.

## Katkıda Bulunma

Bu proje açık kaynaklıdır. Katkıda bulunmak isterseniz:
1. Projeyi fork'layın
2. Yeni bir branch oluşturun (`git checkout -b feature/YeniOzellik`)
3. Değişikliklerinizi commit'leyin (`git commit -am 'Yeni özellik ekle'`)
4. Branch'inizi push'layın (`git push origin feature/YeniOzellik`)
5. Bir Pull Request oluşturun
