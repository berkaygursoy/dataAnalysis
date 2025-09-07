import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Veriyi okuma
veri = pd.read_csv("train.csv")

# Eksik değerleri işleme (örneğin, "Age" için ortalama değerle doldurma)
veri["Age"].fillna(veri["Age"].mean(), inplace=True)

# "Embarked" için en sık görünen değerle doldurma
veri["Embarked"].fillna(veri["Embarked"].mode()[0], inplace=True)

# Kategorik verileri sayısal verilere dönüştürme (örneğin, "Sex" için)
veri["Sex"] = veri["Sex"].map({"male": 0, "female": 1})

# Cinsiyet sütununu dönüştürme
veri["Cinsiyet"] = veri["Sex"].map({0: "Erkek", 1: "Kadın"})

# Hayatta kalma oranını cinsiyete göre görselleştirme
sns.barplot(x="Cinsiyet", y="Survived", data=veri)  # x ekseninde 'Cinsiyet' kullan
plt.xlabel("Cinsiyet")  # Etiketi Türkçeleştirme
plt.ylabel("Hayatta Kalma Oranı")  # Etiketi Türkçeleştirme
plt.title("Cinsiyete Göre Hayatta Kalma Oranı")  # Başlığı Türkçeleştirme
plt.show()

# Hayatta kalma oranını sınıfa göre görselleştirme
sns.barplot(x="Pclass", y="Survived", data=veri)
plt.xlabel("Sınıf")  # Etiketi Türkçeleştirme
plt.ylabel("Hayatta Kalma Oranı")  # Etiketi Türkçeleştirme
plt.title("Sınıfa Göre Hayatta Kalma Oranı")  # Başlığı Türkçeleştirme
plt.show()

# Yaş dağılımını görselleştirme
sns.histplot(veri["Age"], kde=True)
plt.xlabel("Yaş")  # Etiketi Türkçeleştirme
plt.ylabel("Yoğunluk")  # Etiketi Türkçeleştirme
plt.title("Yaş Dağılımı")  # Başlığı Türkçeleştirme
plt.show()
