## Project Outline

The goal of this analysis is to inform a business owner on where to start a new restaurant in LA. Geographic restaurant data from Foursquare is used to uncover the culinary make-up of different neighborhoods and to determine which areas are most active and popular based on their likes. Neighborhood boundaries are defined with data from the LA Times. The major culinary groups in LA are revealed with the k-means algorithm --- a basic machine learning clustering method --- and compared to rent data from Zillow. 

## Data

Before accessing restaurant data, it is important to understand the geography of LA. Specifically, an effective method of subdividing LA that is somewhat associated with the culinary make-up of various neighborhoods is needed. One approach is to use official subdivisions, like zipcodes or county lines. This dataset could work well, but the boundaries may not be related to the actual cultural regions of LA. They also don't take into account the dynamics of neighborhoods. For example, when one neighborhood expands and others converge, zipcodes will not follow. 

I came across a possibly more representative dataset from the LA Times that was developed with input from hundreds of residents of the city. Since the boundaries were drawn by residents, they are likely much more representitive of the cultural regions of LA than any official designations. I downloaded the neighborhood polygons in JSON format from their website, parsed them with GeoPandas, and plotted them with Folium. Check out  for an outline of the LA Times project that came up with these boundaries. 

![LA_times](https://github.com/iafinn/LA-culinary-clusters/blob/master/reports/figures/LA_neighborhoods.png)

The neighborhood polygons cover all of LA county, so I decided to restrict analysis to the main metroplitan area. The center of each polygon was determined with the centroid method in GeoPandas and neighborhoods further than 30 km from the Downtown centroid were removed from the polygon dataset. All distances were calculated using the Haversine formula, which gives the great circle distance between two points on a sphere. The resulting centroids are shown below.