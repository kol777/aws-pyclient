import configHeader
import argparse
import json

parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter,
	description="This script creates a policy in aws\n")

requiredNamed = parser.add_argument_group('Required arguments')

requiredNamed.add_argument('-n', metavar='policyName', type=str, required=True, dest='policyName',
		help='Policy name for the policy which will be created\n')

requiredNamed.add_argument('-d', metavar='policyDocument', type=str, required=True, dest='policyDocument',
		help='Path_to_Policy Document for the policy which will be created\n')

args = parser.parse_args()

# Create user
def CreatePolicy(polName, polDoc):
    jsonfile = json.load(open(polDoc))
    response = configHeader.iam.create_policy(
        PolicyName=polName,
        PolicyDocument=json.dumps(jsonfile)
    )
    print(response)

if __name__ == '__main__':
    print(json.dumps(args.policyDocument))
    CreatePolicy(args.policyName, args.policyDocument)
