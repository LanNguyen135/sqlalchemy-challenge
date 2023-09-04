# SQLAlchemy Challenge

### Contributor: Lan "Alice" Nguyen

### Part 1: Analyze and explore data
In this section, I use Python along with SQLAlchemy ORM queries, Pandas, and Matplotlib to conduct basic climate analysis and explore the climate database.

Connecting to the Database
- Utilize the SQLAlchemy create_engine() function to establish a connection with the SQLite database.
- Employ the SQLAlchemy automap_base() function to reflect the database tables into Python classes and subsequently save references to these classes.
- Establish a connection between Python and the database by creating a SQLAlchemy session.

Data Analysis

I perform two types of data analysis:

Precipitation Analysis
- Query the data for the last 12 months of precipitation records.
- Transform the retrieved data into a Pandas DataFrame.
- Create a plot representing the precipitation data.

Station Analysis
- Develop a query to identify the most active station.
- Create a query that calculates the lowest, highest, and average temperatures, filtering the data for the most active station.
- Generate a plot displaying the results of this analysis.

### Part 2: Design climate app
In this section, I design a Flask API based on the queries and analyses conducted in Part 1.
- Homepage:
  - Provide a list of all available routes for easy navigation.
- Route: /api/v1.0/precipitation
  - Convert the results from the precipitation analysis into a dictionary format, using date as the key and precipitation (prcp) as the value.
  - Return the JSON representation of this dictionary.
- Route: /api/v1.0/stations
  - Return a JSON list of weather stations from the dataset.
- Route: /api/v1.0/tobs
  - Return a JSON list of temperature observations for the previous year recorded at the most active station.
- Route: /api/v1.0/<start> and /api/v1.0/<start>/<end>
  - Provide JSON lists containing minimum temperature, average temperature, and maximum temperature for a specified start date or start-end date range.

