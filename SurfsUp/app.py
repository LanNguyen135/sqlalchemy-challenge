# Import the dependencies.
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources\\hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(autoload_with=engine)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(bind=engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)



#################################################
# Flask Routes
#################################################
@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/2016-08-23<br/>"
        f"/api/v1.0/2016-08-23/2017-08-23"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    # Query the last 12 months of precipitation
    data = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= '2016-08-23').all()
    session.close()
    precipitation_list = []

    # Convert data into dictionary using date as the key and prcp as the value and append into a list of precipitation_list
    for date, prcp in data:
        precipitation_dict = {}
        precipitation_dict[date] = prcp
        precipitation_list.append(precipitation_dict)
     
    return jsonify(precipitation_list)

@app.route("/api/v1.0/stations")
def stations():
    # Query all the station names 
    session = Session(engine)
    results = session.query(Station.station).all()
    session.close()

    # Convert list of tuples into normal list
    stations_list = list(np.ravel(results))
    return jsonify(stations_list)

@app.route("/api/v1.0/tobs")
def tobs():
    # Query last 12 months temperature from the most active station
    session = Session(engine)
    station_data = session.query(Measurement.tobs).filter(Measurement.station=='USC00519281').filter(Measurement.date >= '2016-08-23').all()
    session.close()

    # Convert list of tuples into normal list
    station_data_list = list(np.ravel(station_data))
    return jsonify(station_data_list)

@app.route("/api/v1.0/<start>")
def start_temp(start):
    # Query the min, average and max temperature for a specific start date
    session = Session(engine)
    temp_data = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).filter(Measurement.date >= start).all()
    session.close()

    # Convert temp_data into list data
    data=[]
    for tmin, tavg, tmax in temp_data:
        data.append(tmin)
        data.append(tavg)
        data.append(tmax)
    return jsonify(data)

@app.route("/api/v1.0/<start>/<end>")
def start_end_temp(start, end):
    # Query the min, average and max temperature for a specific start date and end date
    session = Session(engine)
    temp_data = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).filter(Measurement.date >= start, Measurement.date <= end).all()
    session.close()

    # Convert temp_data into list data
    data=[]
    for tmin, tavg, tmax in temp_data:
        data.append(tmin)
        data.append(tavg)
        data.append(tmax)
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)