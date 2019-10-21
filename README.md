## LA Culinary Clusters

Los Angeles (LA) is a massive city with cuisines from around the world. The most popular food regions are constantly shifting in response 
to customer demand and rising rent prices, resulting in an fairly dynamic restaurant scene. Diverse culinary influences in LA have also 
fostered an innovative atmosphere and led to the development of many fusion cuisines. Starting a successful restaurant in LA is no easy task.
With so many existing restaurants, the competition for a newcomer is fierce. 

The goal of this analysis is to inform a business owner on where to start a new restaurant in LA. Geographic restaurant data from 
Foursquare is used to uncover the culinary make-up of different neighborhoods and to determine which areas are most active and popular 
based on their likes. Neighborhood boundaries are defined with data from the LA Times. The major culinary groups in LA are revealed with 
principal component analysis and k-means clustering and compared to rent data from Zillow.

## Directory Overview

```
├───data            
│   ├───processed       <- Processed data
│   └───raw             <- raw JSON files used in analysis
├───data-processing     <- scripts used for processing and API calls
├───EDA                 <- Exploratory Data Analysis
├───models              <- Script used for PCA and k-means clustering 
└───reports             <- Results of the study
    └───figures
```

## Sample Results

### LA Restaurant Clusters Mean Composition
![PCA](https://github.com/iafinn/LA-culinary-clusters/blob/master/reports/figures/cluster_barplot.png)

### Geographic Distribution of Clusters
![PCA](https://github.com/iafinn/LA-culinary-clusters/blob/master/reports/figures/clustering_results.png)

### Clusters Projected on the Principal Component Axes
![PCA](https://github.com/iafinn/LA-culinary-clusters/blob/master/reports/figures/pca_clusters.png)
