
    from flask import Flask, request,jsonify
    from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
    import requests
    import datetime

    app = Flask(__name__)
    api = Api(app)


    class SensorModel():
        sensors_details = {}
        sensors_freq_map = {}
        sensor_id=0


    @app.route("/")
    def hello_world():
        return "Hello world!"


    # @app.route("/create-sensor", methods=["POST"])
    # def create_sensor():
    #     """
    #     Create a new sensor object in the satellite, by calling the /sensors endpoint.
    #     """
    #     BASE = "http://127.0.0.1:5000/"
    #     frequency = request.form["frequency"]
    #     response= requests.post(BASE+"/sensors",{"frequency":frequency})
    #     return {frequency: "Creating Sensor with frequency " + frequency}, response.status_code

    def abort_if_invalid_int(user_input, attr_name):
        try:
            int(user_input)
        except ValueError:
            # abort(404, messsage='[ERROR] Invalid Integer value for '+attr_name)
            print('[ERROR] Invalid Integer value for ' + attr_name)


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
        freq = request.form["frequency"]
        abort_if_invalid_int(freq,'Frequency')
        sensor_id = SensorModel.sensor_id + 1
        SensorModel.sensor_id = sensor_id
        SensorModel.sensors_freq_map[sensor_id] = freq
        SensorModel.sensors_details[sensor_id] = []
        return {"sensor_id": "Successfully created sensor "+str(sensor_id) +" with frequency "+freq} , 200



    @app.route("/sensors/<int:sensor_id>", methods=["GET"])
    def get_sensor_id(sensor_id):
        """
        -> returns 200 JSON Sensor object
       -> returns 404 if sensor id does not exist
        """
        if sensor_id in SensorModel.sensors_freq_map:
            freq=SensorModel.sensors_freq_map[sensor_id]
            sensor_data = SensorModel.sensors_details[sensor_id]
            sta_cd = 200
        else:
            sensor_data = {sensor_id: "Sensor ID " + str(sensor_id) + " does not exist.."}
            freq = 0
            sta_cd = 400
        res= {'sensor_id': sensor_id, 'frequency': freq, 'data': sensor_data}
        return res, sta_cd

    @app.route("/sensors/<int:sensor_id>", methods=["PATCH"])
    def update_sensor_dtl(sensor_id):
        """
        -> returns 200 JSON Sensor object
       -> returns 404 if sensor id does not exist
        """
        measurement = request.form["measurement"]
        status = request.form["status"]
        time_stamp = datetime.datetime.now()
        if sensor_id in SensorModel.sensors_details:
            SensorModel.sensors_details[sensor_id].append({'measurement':measurement,'status':status,'time_stamp':time_stamp})
            msg = "Successfully updated sensor "+str(sensor_id)
            sta_cd = 200
        else:
            msg = {sensor_id: "Sensor ID " + str(sensor_id) + " does not exist.."}
            sta_cd = 404

        return {"message": msg}, sta_cd

    @app.route("/all-sensors", methods=["GET"])
    def all_sensors():
        """
        Return the latest cached data for all sensors, including timestamps.
        """
        res=[]
        for sensor_id in SensorModel.sensors_freq_map:
            freq = SensorModel.sensors_freq_map[sensor_id]
            sensor_data = SensorModel.sensors_details[sensor_id]
            res.append({'sensor_id': sensor_id, 'frequency': freq, 'data': sensor_data})
        return jsonify(res),200

    @app.route("/poll", methods=["GET"])
    def poll():
        """
        Update local cache with the latest sensor data from all sensors.
        """
        for sensor_id in SensorModel.sensors_freq_map:
            sensor_data = SensorModel.sensors_details[sensor_id][-1] if SensorModel.sensors_details[sensor_id] else []
            if sensor_data:
                SensorModel.sensors_details[sensor_id] = sensor_data

        return {"message": "Successfully polled for all sensors"}, 200

    if __name__ == '__main__':
        app.run(debug=True)


    """
    
    sensors_details 
    {
    0: [{"status": 'INIT','measurement': 12.45, time: 02/01-23:45},{"status": 'ACTIVE','measurement': 34.15, 'time': '02/02-13:38'}]
    1: [{"status": 'INIT','measurement': 45.67, time: 02/01-13:25}]
    2: [{"ststatusaus": 'INIT','measurement': 62.45, time: 02/01-21:41},{"status": 'ACTIVE','measurement': 24.15, 'time': '02/02-45:36'}]
    }
    
    
    sensors_freq_map = {
    0: 10
    1: 20
    3: 30
    }
    
    """