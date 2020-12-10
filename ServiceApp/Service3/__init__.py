import logging

import azure.functions as func

import random, string

import json

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function 3')

    rtnstr=""
    for i in range(5):
        rtnstr+=random.choice(string.ascii_letters)

    return func.HttpResponse(json.dumps({'letters':rtnstr}))
