import unittest
import boto3

class TestLambda(unittest.TestCase):

    def testPerformControl(self):
        client = boto3.client('lambda', region_name='us-west-2',
            aws_access_key_id='*',
            aws_secret_access_key='*'
        )

        response = client.invoke(
            FunctionName='arn:aws:lambda:us-west-2:078580774324:function:performControl',
            InvocationType='RequestResponse',
            LogType='None',
            Payload='{}'
        )
        self.assertEqual(response['ResponseMetadata']['HTTPStatusCode'], 200)



if __name__ == '__main__':
    unittest.main()