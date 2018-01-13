import boto3
import json

iam = boto3.client('iam')
iam_resource = boto3.resource('iam')

class CreateResource:
    def __init__(self):
        self.polArn = ''

    def CreateUser(self, user_name):
        print('**** Creating User %s ****' %user_name)
        response = iam.create_user(
            UserName=user_name
        )
        print(response)

    def CreateGroup(self, group_name):
        print('**** Creating Group %s ****' %group_name)
        response = iam.create_group(
            GroupName=group_name
        )
        print(response)

    def CreatePolicy(self, polName, polDoc):
        print('**** Creating Policy %s ****' %polName)
        jsonfile = json.load(open(polDoc))
        response = iam.create_policy(
            PolicyName=polName,
            PolicyDocument=json.dumps(jsonfile)
        )
        print(response)
        self.polArn = response['Policy']['Arn']
