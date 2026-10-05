
class AirFare():
    def calc_fare(self,inp:[str])->[float]:

        enum={"United": {"Premium": "%d*(0.75 + 0.10)+10" ,
                         "Business": "%d*(0.80 + 0.25) + 50",
                         "Economy": "%d*1"},
              "Delta": {"Business": "%d*(0.50 + 0.25)+50",
                         "Economy": "%d*1"},
              "Southwest": {"Economy":"%d*1" },
              "LuigAir": {"Business": ["%d*(0.50 + 0.25)+50","2*(%d + 50 * 0.25)"],
                         }}   # here the first expression if miles > 100 and 2nd element is if miles <= 100
        res=[]
        for record in inp:
            airline_nm, miles, seating_class = record.split(" ")
            if airline_nm == 'LuigAir' and seating_class =='Business' and float(miles) <= 100:
                res.append(eval(enum[airline_nm][seating_class][1] % float(miles)))
            else:
                res.append(eval(enum[airline_nm][seating_class] % float(miles)))

        return res

test_input=[
    "United 150.0 Premium",
    "Delta 60.0 Business",
    "Southwest 1000.0 Economy",
    "LuigAir 50.0 Business"]

obj = AirFare()
print(obj.calc_fare(test_input))
