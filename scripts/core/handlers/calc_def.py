from scripts.logging.glens_logging import logger
import json


class Calculator:
    def __init__(self):
        logger.info("This is Calculator")

    def calculator(self, input_data):
        logger.info("Starting Calculator")
        try:
            value1 = input_data["value1"]
            value2 = input_data["value2"]
            action = input_data["action"]
            if action == 'Add':
                result = value1 + value2
                print(result)
                result_out = "The Addition output is " + str(result)
            elif action == 'Sub':
                result = value1 - value2
                result_out = "The Subtraction output is " + str(result)
            elif action == 'Mul':
                result = value1 * value2
                result_out = "The Multiplication output is", str(result)
            elif action == 'Div':
                try:
                    result = value1 / value2
                    result_out = "The Division output is", str(result)
                except Exception as e:
                    logger.exception("Invalid input" + str(e))

            out_put = {"Message:": result_out}
            print(json.dumps(out_put))
            return out_put
        except Exception as e:
            logger.exception("Error in calculator method" + str(e))
            return {"Message": "Invalid data"}
