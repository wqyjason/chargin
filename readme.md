# Safer Home

We built the website in the hope of creating a safer environment for people living in Urbana-Champaign.



## Procedure

We obtained data from the [Urbana Police Incidents dataset](https://github.com/cudsug/urbana-police-incidents), and focused on six main areas in our analysis: theft, burglary, offenses to children, noise and vibration violation and sexual offenses. These are important factors in evaluating housing quality and safety. We created rectangular and geographical heatmaps and area charts from 454,172 entries of police incidents ranging from 1988 to 2019.

We then calculated the safety index for each major apartment on campus (Latitude, Tower at 3rd, HERE, Skyline and Campus Circle) using clustering and eventually came up with our ranking. Note that our algorithm does not limit us to only the 5 apartments listed above: we are capable of ranking more apartments, as long as you provide us with the location!



##Potential Usage

* People in search of the safest location for their future apartments.
* Police looking to explore the trend in various categories of crimes, the time of the day, the month of the year or even the most popular location.

All in all, our data speak for itself!



## Built With

* Flask

* Tableau
* Google Map API



## Contributors

* Qingyu Wang - Web Development
* Zecheng Wu - Web Development
* Zixiong Feng - Data Visualization and Geocoding
* Chutong Xiao - Data Visualization
* Yutong Liu - Data Visualization
