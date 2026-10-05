"""
0 :  [(Status: ACTIVE, measurement: 23.56, time: 02/01-23:45), (Status ACTIVE measurement 78.56)]
1 : [(Status:INITIALIZE, measurement:56.3), ]
3 : [Status measurement]


0: freq 10
1: freq 20
3: Freq.30
"""

from flask import Flask, request,jsonify
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with, request
import datetime
from flask_sqlalchemy import SQLAlchemy
import enum

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sensor_data.db'
db = SQLAlchemy(app)

class StatusType(enum.Enum):
    INITIALIZING = "INIT"
    ACTIVE = "ACT"
    FAILED = "FLD"
    RESTARTING = "RST"
    TERMINATING = "TRM"


class SensorModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    frequency = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String, nullable=False)
    # status = db.Column(db.Enum(StatusType), nullable=True)
    measurement = db.Column(db.Float, nullable=True)
    time_stamp = db.Column(db.DateTime, nullable=True)

    def __repr__(self):
        return f"Sensor(id={self.id}, frequency = {self.frequency}, status = {self.status}, " \
               f"measurement = {self.measurement})"

db.create_all()

# class Sensor(Resource):
@app.route("/")
def hello_world():
    return "Hello world!"


# @app.route("/create-sensor", methods=["POST"])
# def create_sensor():
#     """
#     Create a new sensor object in the satellite, by calling the /sensors endpoint.
#     """
#     frequency = request.json["frequency"]
#     return "Implement me"
#
#
# @app.route("/poll", methods=["GET"])
# def poll():
#     """
#     Update local cache with the latest sensor data from all sensors.
#     """
#     return "Implement me"
#
#
# @app.route("/all-sensors", methods=["GET"])
# def all_sensors():
#     """
#     Return the latest cached data for all sensors, including timestamps.
#     """
#     return "Implement me"
#
#
# @app.route("/sensor-ids", methods=["GET"])
# def sensor_ids():
#     """
#     returns JSON list of sensor IDs
#     """
#     return "Implement me"

@app.route("/sensors", methods=["PUT"])
def sensors():


    """
   -> CREATE a new sensor
   -> accepts a JSON body with the following properties
   -> "frequency": an integer
   -> returns 200 JSON Sensor object if successful
   -> returns 400 if frequency is invalid or absent
   -> returns 500 if not enough resources
    """

    sensor_put_args = reqparse.RequestParser()
    sensor_put_args.add_argument("frequency", type=float, help="Fequency of a sensor", required=True)
    sensor_put_args.add_argument("status", type=str, help="Status of a sensor", required=True)
    sensor_put_args.add_argument("measurement", type=float, help="Measurement of a sensor", required=True)
    args = sensor_put_args.parse_args()
    sensor = SensorModel(frequency=args['frequency'],  status=args['status'],time_stamp=datetime.datetime.now(), measurement=args['measurement'])
    db.session.add(sensor)
    db.session.commit()

    return jsonify({"id":sensor.id}),200

@app.route("/sensors/<int:sensor_id>", methods=["GET"])
def get_sensor_id(sensor_id):
    """
    -> returns 200 JSON Sensor object
   -> returns 404 if sensor id does not exist
    """
    sensor = SensorModel.query.get_or_404(sensor_id)
    # res=sensors[sensor_id]
    # print("res",sensors[sensor_id])
    #return jsonify(res),200

    return {'id':sensor.id, 'frequency':sensor.frequency, 'status':sensor.status, 'measurement':sensor.measurement},200


if __name__ == '__main__':
    app.run(debug=True)
