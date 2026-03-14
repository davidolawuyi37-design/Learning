# we want group different houses and their prices  into 2 clusters:
# expensive houses
# cheap houses

import pandas as pd
from sklearn.cluster import KMeans
data = {
    "home_type": ["Apartment", "Apartment", "Apartment", "Apartment", "Apartment", "Apartment",
                  "Bungalow", "Bungalow", "Bungalow", "Bungalow", "Bungalow", "Bungalow",
                  "Duplex", "Duplex", "Duplex", "Duplex", "Duplex", "Duplex",
                  "Detached_House", "Detached_House", "Detached_House", "Detached_House", "Detached_House", "Detached_House",
                  "Villa", "Villa", "Villa", "Villa", "Villa", "Villa"],

    "size_sqft": [400, 500, 550, 600, 650, 700, 900, 1000, 1100, 1200, 1300, 1400,
                  1600, 1700, 1800, 1900, 2000, 2100, 2300, 2500, 2700, 2900, 3100, 3300,
                  3600, 4000, 4300, 4600, 5000, 5400],

    "bedrooms": [1, 1, 2, 2, 2, 3, 2, 2, 3, 3, 3, 4,
                 3, 3, 4, 4, 4, 5, 4, 4, 5, 5, 5, 6,
                 5, 6, 6, 7, 7, 8],

    "price": [35000, 40000, 45000, 50000, 55000, 60000, 70000, 80000, 90000, 100000, 110000, 120000,
              150000, 170000, 190000, 210000, 230000, 250000, 300000, 330000, 360000, 390000, 420000, 450000,
              520000, 580000, 640000, 700000, 780000, 850000]
}

df = pd.DataFrame(data)
print(df)

x = df[["size_sqft", "bedrooms", "price"]]

modelling = KMeans(n_clusters=4)
modelling.fit(x)

df["cluster"] = modelling.labels_
print(df)