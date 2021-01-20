# Time-series-forecasting
Quantitative Analysis of time series forecasting
Task 1 - Coding
A. Put this in a file named places.csv:
Name,Latitude,Longitude
Alta,69.96887,23.27165
Anchorage,61.21806,-149.90028
Jakarta,-6.21462,106.84513
London,51.50853,-0.12574
Longyearbyen,78.22334,15.64689
North pole,90,0
Oslo,59.91273,10.74609
South pole,-90,0
Troll research station,-72.00194,2.53389
Vardø,70.37048,31.11066
B. Write a command line program that takes one optional integer argument n. Use C# or
Python.
C. If no argument is given, use places.csv as input.
D. If n is given, use n randomly generated places as input.
E. Find the air distance (great circle distance) between all pairs of places. Discard pairs
having the same pair of places as another pair.
F. Write out all place pairs and distances by ascending distance, lines column aligned
and formatted like this:
Someplace Otherplace 152.6 km
G. On the last line, write out the average distance and the place pair and corresponding
distance having the distance closest to the average value, like this:
Average distance: 321.8 km. Closest pair: Thisplace – Thatplace 312.5 km.
Try to keep the code both concise, idiomatic and readable. Code must contain a readme,
with instructions on setup and use, and must be runnable. Feel free to deliver as repo on
github.
Task 2 - Forecasting Air Quality
You are to sketch (describe) how you would approach building a model for forecasting air
quality globally. To limit scope we are only considering particle matter, PM.
Output from the model could either be:
1. A time series (future observations) for a given location,
2. A set of maps, each visualizing the air quality for a specific time period (aka a
timelapse)
Questions:
A. What would be the key challenges for building a forecasting model for air quality?
B. How would be the difference between output 1 or 2 impact the complexity when
building the model
Expected output from task 2:
● Sketch/description for model approach
● Answer to questions A and B
● Optionally: links to github repos, or other works demonstrating past experiences in
the field
Task 3 - Forecasting Pollen
We are also looking to build models for forecasting pollen levels globally.
Question:
A. 1.How would building a model for pollen forecasting differ from building a model for
forecasting air quality?
Expected output from task 3:
● Answer to question A
● Optionally: links to github repos, or other works demonstrating past experiences in
the field
