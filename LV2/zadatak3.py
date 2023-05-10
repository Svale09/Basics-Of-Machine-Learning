import numpy as np
import matplotlib.pyplot as plt

# Skripta zadatak_3.py ucˇitava sliku ’road.jpg’. Manipulacijom odgovarajuc ́e numpy matrice pokušajte:
# a) posvijetliti sliku,
# b) prikazati samo drugu cˇetvrtinu slike po širini,
# c) zarotirati sliku za 90 stupnjeva u smjeru kazaljke na satu, 
# d) zrcaliti sliku.

# SAMO PRIMJER UCITAVANJA SLIKE I PLOTANJE
img = plt.imread("/Users/ivansvalina/Documents/Faks/LV2/road.jpg")
img = img[:,:,0].copy() #uzima se samo jedan od tri kanala za boje jer su svi isti = 255 jer je gray slika

fig,axes = plt.subplots(nrows=1,ncols=5)

axes[0].imshow(img, cmap="gray") #kada bi bilo 3, 4 i vise slika onda bi bilo axes[0,0] za prvu sliku, axes [0,1] za prvi row, drugi column....

# a)
brightness = 50
brightImg = np.clip(img+brightness,0,255)

axes[1].imshow(brightImg, cmap="gray")

# b)
quarter = (len(img[0])/4)
quarter = int(quarter)
print(quarter)
quarterImg = img[:,quarter:2*quarter]
axes[2] = plt.imshow(quarterImg, cmap="gray")

# c)
rotatedImg = np.rot90(img)
rotatedImg = np.rot90(rotatedImg)
rotatedImg = np.rot90(rotatedImg)

axes[3] = plt.imshow(rotatedImg, cmap="gray")

# d)

mirroredImg = np.flip(img, axis= 1)

axes[4] = plt.imshow(mirroredImg, cmap="gray")
plt.show() # u sub plotovima iz nekog razloga 3 i 4 nisu prikazani TO DO