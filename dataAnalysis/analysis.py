import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Veriyi okuma
veri = pd.read_csv("train.csv")

veri["Age"].fillna(veri["Age"].mean(), inplace=True)

veri["Embarked"].fillna(veri["Embarked"].mode()[0], inplace=True)

veri["Sex"] = veri["Sex"].map({"male": 0, "female": 1})

veri["Cinsiyet"] = veri["Sex"].map({0: "Erkek", 1: "Kadın"})

# Hayatta kalma oranını cinsiyete göre görselleştirme
sns.barplot(x="Cinsiyet", y="Survived", data=veri) 
plt.xlabel("Cinsiyet")
plt.ylabel("Hayatta Kalma Oranı") 
plt.title("Cinsiyete Göre Hayatta Kalma Oranı") 
plt.show()

# Hayatta kalma oranını sınıfa göre görselleştirme
sns.barplot(x="Pclass", y="Survived", data=veri)
plt.xlabel("Sınıf")  
plt.ylabel("Hayatta Kalma Oranı") 
plt.title("Sınıfa Göre Hayatta Kalma Oranı") 
plt.show()

# Yaş dağılımını görselleştirme
sns.histplot(veri["Age"], kde=True)
plt.xlabel("Yaş") 
plt.ylabel("Yoğunluk") 
plt.title("Yaş Dağılımı")  
plt.show()

