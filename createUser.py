import configHeader
import argparse

parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter,
	description="This script creates an user in aws\n")

requiredNamed = parser.add_argument_group('Required arguments')

requiredNamed.add_argument('-n', metavar='userName', type=str, required=True, dest='userName',
		help='User name for the user which will be created\n')

parser.add_argument('--delete', dest='delete', action='store_const', const='delete',
		help='Deletes the created user\n')

args = parser.parse_args()

# Create user
def CreateUser(user_name):
    response = configHeader.iam.create_user(
        UserName=user_name
    )
    print(response)

def DeleteUser(user_name):
    response = configHeader.iam.delete_user(
        UserName=user_name
    )
    print(response)

if __name__ == '__main__':
    CreateUser(args.userName)
    if args.delete:
        DeleteUser(args.userName)
