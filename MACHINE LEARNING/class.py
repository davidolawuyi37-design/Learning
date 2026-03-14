# we want group students performance into 3 clusters:
# High performers
# Medium performance
# Low performance

import pandas as pd
from sklearn.cluster import KMeans

data = {
    "hours_studied": [1,2,3,4,5,6,7,8,2,6,4,7],
    "exam_score": [40,50,55,60,65,70,80,90,48,75,62,85]
}

df = pd.DataFrame(data)
print(df)

x  = df[["hours_studied", "exam_score"]]

model = KMeans(n_clusters=3)
model.fit(x)

df["cluster"] = model.labels_
print(df)