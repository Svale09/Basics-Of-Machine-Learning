import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as Image
from sklearn.cluster import KMeans

# ucitaj sliku
img = Image.imread("/Users/ivansvalina/Documents/Faks/LV7/imgs/test_5.jpg")



# prikazi originalnu sliku
plt.figure()
plt.imshow(img)
plt.axis('off')
plt.title("Originalna slika")
plt.show()

# pretvori vrijednosti elemenata slike u raspon 0 do 1
img = img.astype(np.float64) / 255

# transfromiraj sliku u 2D numpy polje (jedan red su RGB komponente elementa slike)
w,h,d = img.shape
img_array = np.reshape(img, (w*h, d))

# rezultatna slika
img_array_aprox = img_array.copy()

print("No. of colors = {}".format(len(img_array_aprox)))

km = KMeans(n_clusters=3, init='k-means++', n_init=5, random_state=0)
km.fit(img_array_aprox)
labels = km.predict(img_array_aprox)

q_img = km.cluster_centers_[labels].reshape(w,h,-1)

plt.figure()
plt.imshow(q_img)
plt.axis('off')
plt.title("Kvantizirana slika")
plt.show()

Sum_of_squared_distances = []
K = range(1,15)
for k in K:
    km = KMeans(n_clusters=k, init='k-means++', n_init=5, random_state=0)
    km = km.fit(img_array_aprox)
    Sum_of_squared_distances.append(km.inertia_)

plt.plot(K, Sum_of_squared_distances, 'bx-')
plt.xlabel('k')
plt.ylabel('Sum_of_squared_distances')
plt.title('Elbow Method For Optimal k')
plt.show()

#7
for i in range(clusters): 
    bit_values = labels==[i]
    binary_img = np.reshape(bit_values, (img.shape[0:2]))
    binary_img = binary_img*1
    x=int(i/2)
    y=i%2

plt.figure("Binary image")
plt.imshow(binary_img)
plt.show()