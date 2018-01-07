import configHeader
import argparse

parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter,
	description="This script attaches a policy to a group in aws\n")

requiredNamed = parser.add_argument_group('Required arguments')

requiredNamed.add_argument('-pn', metavar='policyName', type=str, required=True, dest='policyName',
		help='Policy name\n')

requiredNamed.add_argument('-gn', metavar='groupName', type=str, required=True, dest='groupName',
		help='Group name\n')

args = parser.parse_args()

# Attaches a user to a group
def AttachPolicyToGroup(policy_name, group_name):
    groupName = configHeader.iam_resource.Group(group_name)
    response = groupName.attach_policy(
        PolicyArn=policy_name
    )
    print(response)

if __name__ == '__main__':
    AttachPolicyToGroup(args.policyName, args.groupName)
