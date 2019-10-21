## Project Outline

The goal of this analysis is to inform a business owner on where to start a new restaurant in LA. Geographic restaurant data from Foursquare is used to uncover the culinary make-up of different neighborhoods and to determine which areas are most active and popular based on their likes. Neighborhood boundaries are defined with data from the LA Times. The major culinary groups in LA are revealed with the k-means algorithm --- a basic machine learning clustering method --- and compared to rent data from Zillow. 

## Data

Before accessing restaurant data, it is important to understand the geography of LA. Specifically, an effective method of subdividing LA that is somewhat associated with the culinary make-up of various neighborhoods is needed. One approach is to use official subdivisions, like zipcodes or county lines. This dataset could work well, but the boundaries may not be related to the actual cultural regions of LA. They also don't take into account the dynamics of neighborhoods. For example, when one neighborhood expands and others converge, zipcodes will not follow. 

I came across a possibly more representative dataset from the [LA Times](http://maps.latimes.com/neighborhoods/) that was developed with input from hundreds of residents of the city. Since the boundaries were drawn by residents, they are likely much more representitive of the cultural regions of LA than any official designations. I downloaded the neighborhood polygons in JSON format from their website, parsed them with GeoPandas, and plotted them with Folium.

![LA_times](https://github.com/iafinn/LA-culinary-clusters/blob/master/reports/figures/LA_neighborhoods.png)

The neighborhood polygons cover all of LA county, so I decided to restrict analysis to the main metroplitan area. The center of each polygon was determined with the centroid method in GeoPandas and neighborhoods further than 30 km from the Downtown centroid were removed from the polygon dataset. All distances were calculated using the Haversine formula, which gives the great circle distance between two points on a sphere. The resulting centroids are shown below.

![centroids](https://github.com/iafinn/LA-culinary-clusters/blob/master/reports/figures/centroids.png)

All restaurant data was accessed from the [Foursquare API](https://developer.foursquare.com/). Each neighborhood was queried with the explore endpoint in the Places API to get a list of representative restaurants. Results are limited to food venues with the category ID and only 50 venues are returned for each search (there is a 50 venue cap from Foursquare). As an example, the search results for the neighborhood of Alhambra are shown below. In this map, the blue circle represents the search area and the green region is the Alhambra polygon. The center of the search area is given by the Alhambra centroid, and the radius of the search was calculated by finding the maximum distance from the centroid to the furthest point in the polygon. Search results outside (blue dots) and inside (green dots) the Alhambra polygon are differentiated using the 'within' method of GeoPandas.

![API](https://github.com/iafinn/LA-culinary-clusters/blob/master/reports/figures/API_search.png)

For the previous sections, LA is subdivided using the LA Times neighborhood polygons. Unfortunately, I couldn't find rental data for these specific neighborhood divisions. Instead, I divide LA according to the zipcode-defined regions from the [County of Los Angeles Open Data website](https://data.lacounty.gov/) (GeoJSON format). The median rental price per square foot for each zipcode for the past year were accessed from Zillow via the [Quandl API](https://docs.quandl.com/).

## Exploratory Data Analysis

Now I'll go over some highlights from the EDA. The 10 most numerous venues in our dataset are shown next. At the top of list are Mexican, pizza, and fast food restaurants. Any business owner opening a restaurant within these categories should be ready to face a lot of competition. 

![common](https://github.com/iafinn/LA-culinary-clusters/blob/master/reports/figures/most_common_rest.png)

Next, the 10 most liked venues by mean likes are given. Theme restaurants top this list, followed by German and Cuban restaurants. These seem like good restaurant categories for a new business.

![mean_likes](https://github.com/iafinn/LA-culinary-clusters/blob/master/reports/figures/mean_likes.png)

Finally, let's look at the geographic distribution of likes per restaurant. Santa Monica and downtown are both pretty high.

### Median Likes Per Restaurant

![likes](https://github.com/iafinn/LA-culinary-clusters/blob/master/reports/figures/like_map.png)

Comparing the likes map to the median rent price per square foot in the next figure, shows a clear correlation between the two. Higher rent areas also have a higher number of likes.

### Median Rent Prices Per Square Foot

![rent](https://github.com/iafinn/LA-culinary-clusters/blob/master/reports/figures/rent_prices.png)

## Modeling with Principal Component Analysis and K-Means Clustering

The next questions to consider are: 1) what is the geographic distribution of restaurants in LA? and 2) are there natural culinary regions within LA or is it fairly homogeneous? To answer these questions, the restaurant data is rearranged to yield the fraction of each restaurant type in each neighborhood (see notebook in models directory).

Let's consider the possible machine learning methods that could be used to answer these questions. Fundamentally, an unsupervised learning algorithm is required, since there isn't a ground truth --- in other words, the accuracy of the model output cannot be directly calculated. Within unsupervised learning, clustering algorthms are suited to grouping a dataset by similarity. The k-means argorithm is a good simple starting point for clustering, as it doesn't require too many input parameters and it is conceptually easy to understand the outputs. However, k-means suffers from an inability to detect outliers and identify elongated clusters. It also requires the user to input the number of clusters k. The cost function that is minimized during k-means is the inertia, or sum of squares distances between each point in a cluster and the cluster centroid. 


![PCA](https://github.com/iafinn/LA-culinary-clusters/blob/master/reports/figures/inertia_ss_plot.png)

### LA Restaurant Clusters Mean Composition
![PCA](https://github.com/iafinn/LA-culinary-clusters/blob/master/reports/figures/cluster_barplot.png)

### Geographic Distribution of Clusters
![PCA](https://github.com/iafinn/LA-culinary-clusters/blob/master/reports/figures/clustering_results.png)

### Clusters Projected on the Principal Component Axes
![PCA](https://github.com/iafinn/LA-culinary-clusters/blob/master/reports/figures/pca_clusters.png)

