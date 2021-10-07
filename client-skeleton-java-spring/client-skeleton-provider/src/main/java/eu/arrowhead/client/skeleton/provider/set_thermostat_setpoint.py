import requests
import json
import sys
import os
import glob


wished_temp = sys.argv[1]
parenthesis = ")"

url = "http://localhost:8083/JS/Run/zway.devices[3].instances[0].ThermostatSetPoint.Set(1,"+str(wished_temp)+str(parenthesis)

thermostat_setpoint = requests.get(url,auth=('admin','eislab'),stream=True)


