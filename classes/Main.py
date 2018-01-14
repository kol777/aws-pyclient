import CreateResource
import AttachResource

if __name__ == '__main__':
    Creator = CreateResource.CreateResource()
    Attacher = AttachResource.AttachResource()

    # Create Users
    Creator.CreateUser('PosD1')
    Creator.CreateUser('PosD2')

    # Create Groups
    Creator.CreateGroup('PosD_Group1')
    Creator.CreateGroup('PosD_Group2')

    # Attach Users to groups
    AttachUserToGroup('PosD1', 'PosD_Group1')
    AttachUserToGroup('PosD2', 'PosD_Group2')

    # Create and Attach Policies to groups
    Creator.CreatePolicy('PosD_iam_full', '.\\policydocuments\\iamfull.json')
    Attacher.AttachPolicyToGroup(Creator.polArn, 'PosD_Group1')
    Creator.CreatePolicy('PosD_iam_restricted', '.\\policydocuments\\iamrestricted.json')
    Attacher.AttachPolicyToGroup(Creator.polArn, 'PosD_Group2')
