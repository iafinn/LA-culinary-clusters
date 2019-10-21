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

### Most Common Restaurants in LA

https://github.com/iafinn/LA-culinary-clusters/blob/master/reports/figures/most_common_rest.png

### Median Likes Per Restaurant

![likes](https://github.com/iafinn/LA-culinary-clusters/blob/master/reports/figures/like_map.png)

### Median Rent Prices Per Square Foot

![rent](https://github.com/iafinn/LA-culinary-clusters/blob/master/reports/figures/rent_prices.png)


