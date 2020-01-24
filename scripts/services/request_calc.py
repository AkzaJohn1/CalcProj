from scripts.logging.glens_logging import logger
import json
from flask import Flask, request, Blueprint
import json
from scripts.core.handlers.calc_def import Calculator
import configparser
from scripts.constants.app_constants import Calculator_settings

calculator_service = Blueprint("calculator", __name__)


@calculator_service.route(Calculator_settings.api_end_point, methods=["POST"])
def post_method():
    try:
        # if request.method == 'POST':
        #     result_out = ''
        #     # action = request.data
        #     # print(request.json)
        #     # print(action)
        print("****************************")
        input_data = json.loads(request.data)
        print(input_data)
        calc_obj = Calculator()
        response = calc_obj.calculator(input_data)
        return response

    except Exception as e:
        logger.exception("Error in POST method" + str(e))
        return {}
