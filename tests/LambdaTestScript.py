import unittest
import boto3

#class TestLambda(unittest.TestCase):
#
#    def testPerformControl(self):
#        client = boto3.client('lambda', region_name='us-west-2',
#            aws_access_key_id='AKIAJNEFR4MZ7Q2TERIQ',
#            aws_secret_access_key='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'
#        )
#
#        response = client.invoke(
#            FunctionName='arn:aws:lambda:us-west-2:078580774324:function:performControl',
#            InvocationType='RequestResponse',
#            LogType='None',
#            Payload='{}'
#        )
#        self.assertEqual(response['ResponseMetadata']['HTTPStatusCode'], 200)
#


class Testing(unittest.TestCase):
    def test_string(self):
        a = 'some'
        b = 'some'
        self.assertEqual(a, b)

    def test_boolean(self):
        a = True
        b = True
        self.assertEqual(a, b)

if __name__ == '__main__':
    unittest.main()