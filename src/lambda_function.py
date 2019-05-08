import boto3
import logging
import json
import http.client
import os
import sys

logger = logging.getLogger()
logger.setLevel( logging.INFO )

def lambda_handler(event, context):

    logger.debug(os.environ['HOST'])
    logger.debug(os.environ['URL'])

    subject = "From GuardDuty"

    headers = {'Content-Type': 'application/json; charset=UTF-8'}
    body = {
        'text': "<users/all>\n" + subject + "\n\n" + json.dumps(event)
    }

    try:
        conn = http.client.HTTPSConnection(os.environ['HOST'], 443)
        conn.request('POST', os.environ['URL'],
                    json.dumps(body).encode("utf-8"), headers)
        response = conn.getresponse()

        if ( response.status == 200 ):
            data = response.read()
            logger.debug( data )
        else:
            logger.fatal('HTTP responsecode が' + response.status + 'でした')

    except http.client.InvalidURL :
        logger.fatal("URLが正しくありません:" + os.environ['URL'])
        raise Exception

    except Exception as e:
        # これは推奨されていないです
        logger.fatal("エラーが発生しました" + e.args)
        print( sys.exc_info() )
        raise Exception

