import configHeader
import argparse

parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter,
	description="This script attaches a user to a group in aws\n")

requiredNamed = parser.add_argument_group('Required arguments')

requiredNamed.add_argument('-un', metavar='userName', type=str, required=True, dest='userName',
		help='User name\n')

requiredNamed.add_argument('-gn', metavar='groupName', type=str, required=True, dest='groupName',
		help='Group name\n')

args = parser.parse_args()

# Attaches a user to a group
def AttachUserToGroup(user_name, group_name):
    groupName = configHeader.iam_resource.Group(group_name)
    response = groupName.add_user(
        UserName=user_name
    )
    print(response)

if __name__ == '__main__':
    AttachUserToGroup(args.userName, args.groupName)
