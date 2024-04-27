import requests
import json
import logging

TRADING_NEWS_API_URL="https://trading-view.p.rapidapi.com/news/list"
TRADING_NEWS_API_KEY="3fb2350dd0msh962751bd232e22ep141805jsnd4607e8a45ef"


def lambda_handler():
    logging.info(f"Handler Starts")
    ResponseBody, ResponseCode, httpStatusCode = tradingNews()

    logging.info(f"Handler Finishes")
    return setLambdaFunctionResponse(ResponseBody, ResponseCode, httpStatusCode)
    



def tradingNews():
    response = requests.get(url=TRADING_NEWS_API_URL, headers=setRequestHeaders())
    newsIn=json.loads(response.text)
    newsOut=[]

    for articleIn in newsIn:
        articleOut = {}
        articleOut["title"] =  articleIn["title"]
        articleOut["source"] =  articleIn["source"]
        if "link" in articleIn:
            articleOut["sourceLink"] =  articleIn["link"]
        newsOut.append(articleOut)

    return newsOut.text,"OK", response.status_code


def setRequestHeaders():
    return {
        "Accept": "application/json",
        "X-RapidAPI-Key" : TRADING_NEWS_API_KEY
    }

def setLambdaFunctionResponse(ResponseBody, ResponseCode, httpStatusCode):
    return {
        "isBase64Encoded": False,
        "statusCode": httpStatusCode,
        "body": setResponseBody(ResponseBody, ResponseCode, httpStatusCode)
    }

def setResponseBody(ResponseBody, ResponseCode, httpStatusCode):
    if httpStatusCode!=200:
        return {
            "code": ResponseCode,
            "userMessage": ResponseBody
        }
    return ResponseBody
