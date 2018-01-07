import configHeader
import argparse

parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter,
	description="This script creates a group in aws\n")

requiredNamed = parser.add_argument_group('Required arguments')

requiredNamed.add_argument('-n', metavar='groupName', type=str, required=True, dest='groupName',
		help='Group name for the group which will be created\n')

parser.add_argument('--delete', dest='delete', action='store_const', const='delete',
		help='Deletes the created group\n')

args = parser.parse_args()

# Creates group
def CreateGroup(group_name):
    response = configHeader.iam.create_group(
        GroupName=group_name
    )
    print(response)

def DeleteGroup(group_name):
    response = configHeader.iam.delete_group(
        GroupName=group_name
    )
    print(response)

if __name__ == '__main__':
    CreateGroup(args.groupName)
    if args.delete:
        DeleteGroup(args.groupName)
