import logging

import azure.functions as func

import random

import json

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function 2')

    rtnstr=""
    for i in range(5):
        rtnstr+=str(random.randint(0,9))

    return func.HttpResponse(json.dumps({'integers':rtnstr}))
