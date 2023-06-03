# RFM-model
### **Customer satisfaction project built on data with information on RFM (stands for recency,frequenct,monetary).Dataset is from [kaggle](https://www.kaggle.com/datasets/mcarujo/customer-segmentation-rfm)**

## **Project Details**
 ### In this project, I applied the **K-means** clustering algorithm to analyze the dataset. To determine the optimal number of clusters, I used the **elbow method**. The elbow method is a technique that helps identify the appropriate number of clusters by evaluating the within-cluster sum of squares (WCSS) for different values of k.

### I iterated over a range of k values and calculated the WCSS for each k. Then, I plotted a line graph with the number of clusters (k) on the x-axis and the corresponding WCSS on the y-axis. The graph resembled an elbow shape, and the **'elbow point'** indicated the optimal number of clusters.

<img src="https://i.ibb.co/2qTtVR1/Ekran-g-r-nt-s-2023-06-03-225220.png" alt="Ekran-g-r-nt-s-2023-06-03-225220" border="0">

### By visually inspecting the graph, I determined the value of k at the elbow point, which represents the point of diminishing returns in terms of decreasing WCSS. This value was selected as the optimal number of clusters for the K-means algorithm in this project.

## **Evaluation**
### For getting meaningful results, I used **plotly** for visualizations and named my customer segments as:
* ### Loyal Spenders 
* ### Occasional Engagers 
* ### Rapid Repeaters
* ### Potential Lost
* ### High value Regulars
###  each one segment explanations can be seen on dashboard I created with this project which also presents the visual outputs.
