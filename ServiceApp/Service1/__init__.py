import logging

import azure.functions as func

import json

import requests

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function 1')
    integers= requests.get('https://zgazureapp.azurewebsites.net/api/service2?code=XotsvLtp3Lv/bNyBulCTDiSLCV115EaU9aAEB6VdVIrDCmvnsBOH8Q==').json()["integers"]
    letters = requests.get('https://zgazureapp.azurewebsites.net/api/service3?code=rmTREQL/6Q7ZQitj41t3WmQ3H0HOagybgnQuheegd9LtKZrvAvucvg==').json()["letters"]

#    rtnstr=""
#    for i in range(5):
#        rtnstr+=integers[i]
#	rtnstr+=letters[i]
    rtnstr=integers+letters
    return func.HttpResponse(json.dumps({ "user":rtnstr }))
