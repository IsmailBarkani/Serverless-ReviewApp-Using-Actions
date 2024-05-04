import requests
import json
import logging
import os

TRADING_NEWS_API_URL=os.environ["TRADING_NEWS_API_URL"]
TRADING_NEWS_API_KEY=os.environ["TRADING_NEWS_API_KEY"]
logging.getLogger().setLevel(logging.INFO)

def lambda_handler(event, context):
    try:
        '''
        Lambda handler independant from the busines logic
        '''
        logging.info(f"Handler Starts")
        ResponseBody, ResponseCode, httpStatusCode = tradingNews()
        logging.info(f"Handler Finishes")
        return setLambdaFunctionResponse(ResponseBody, ResponseCode, httpStatusCode)
    except Exception as err:
        #Catch all internal error
        logging.error(f"Internal error with: {err}")
        logging.info(f"Handler Finishes")
        return setLambdaFunctionResponse("Internal failure, please contact the administration", "INTERNAL_FAILURE", 500)

def tradingNews():
    '''
    Method with zero argument returns a multivalue response 
    that contains a list of trading news and tha code status of 
    the http call to the Trading API
    '''
    try:
        logging.info(f"TradingNews Starts")
        response = requests.get(url=TRADING_NEWS_API_URL, headers=setRequestHeaders())
        if response.status_code!=200:
            #Handles error from the API call
            logging.error(f"Bad gateway, the API provider responded with the code status {response.status_code} and the response message {response.text}")
            return "Bad gateway, please try later","BAD_GATEWAY", 502
        newsIn=json.loads(response.text)
        newsOut=[]
        for articleIn in newsIn:
            articleOut = {}
            articleOut["title"] =  articleIn["title"]
            articleOut["source"] =  articleIn["source"]
            if "link" in articleIn:
                articleOut["sourceLink"] =  articleIn["link"]
            newsOut.append(articleOut)
        logging.info(f"tradingNews Finishes")
        return newsOut,"OK", response.status_code
    except requests.exceptions.RequestException as e:
        #Handles error from the API call
        logging.error("Error fetching data:", e)
        return "Bad gateway, please try later","BAD_GATEWAY", 502
    except json.JSONDecodeError as e:
        #Handles Decoding errors
        raise Exception(f"Error decoding JSON: {e}")
    except KeyError as e:
        #Handles Key errors
        raise Exception(f"Key error: {e}")
    except Exception as e:
        #Handles unexpected errors
        raise Exception(f"Unexpected error: {e}")


def setRequestHeaders():
    '''
    HTTP header factory
    '''
    return {
        "Accept": "application/json",
        "X-RapidAPI-Key" : TRADING_NEWS_API_KEY
    }

def setLambdaFunctionResponse(ResponseBody, ResponseCode, httpStatusCode):
    '''
    Initialize the lambda response to meet the proxy integration type response with the API gateway (the exposure)
    '''
    return {
        "isBase64Encoded": False,
        "statusCode": httpStatusCode,
        "body": setResponseBody(ResponseBody, ResponseCode, httpStatusCode)
    }

def setResponseBody(ResponseBody, ResponseCode, httpStatusCode):
    '''
    Set the body response, and handle the success and the failure response
    '''
    if httpStatusCode!=200:
        return {
            "code": ResponseCode,
            "userMessage": ResponseBody
        }
    return ResponseBody
