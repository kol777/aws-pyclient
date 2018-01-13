import boto3

iam = boto3.client('iam')
iam_resource = boto3.resource('iam')

class AttachResource:
    def AttachUserToGroup(self, user_name, group_name):
        print('**** Attaching user %s to group %s' % (user_name, group_name))
        groupName = iam_resource.Group(group_name)
        response = groupName.add_user(
            UserName=user_name
        )
        print(response)

    def AttachPolicyToGroup(self, policy_name, group_name):
        print('**** Attaching policy %s to group %s' % (policy_name, group_name))
        groupName = iam_resource.Group(group_name)
        response = groupName.attach_policy(
            PolicyArn=policy_name
        )
        print(response)
