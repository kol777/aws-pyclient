# Provider configuration

provider "aws" {
  region                  = "us-east-1"
  shared_credentials_file = "C:\\Users\\fldinu\\.aws\\credentials"
  profile                 = "default"
}

# Creating Users

resource "aws_iam_user" "PosD1" {
  name = "PosD1"
}

resource "aws_iam_user" "PosD2" {
  name = "PosD2"
}

# Creating Login Profiles for Users
resource "aws_iam_user_login_profile" "PosD1_lp" {
  user    = "${aws_iam_user.PosD1.name}"
  pgp_key = "keybase:flaviuscdinu"
}

resource "aws_iam_user_login_profile" "PosD2_lp" {
  user    = "${aws_iam_user.PosD2.name}"
  pgp_key = "keybase:flaviuscdinu"
}

# Creating Groups
resource "aws_iam_group" "PosD_Group1" {
  name = "PosD_Group1"
}

resource "aws_iam_group" "PosD_Group2" {
  name = "PosD_Group2"
}


# Assigning users to groups
resource "aws_iam_group_membership" "Add-PosD1-to-PosD-Group1" {
  name  = "PosD1-to-PosD_Group1"

  users = ["${aws_iam_user.PosD1.name}"]
  group = "${aws_iam_group.PosD_Group1.name}"
}

resource "aws_iam_group_membership" "Add-PosD2-to-PosD-Group2" {
  name  = "PosD2-to-PosD_Group2"

  users = ["${aws_iam_user.PosD2.name}"]
  group = "${aws_iam_group.PosD_Group2.name}"
}


# Creating Policies
resource "aws_iam_policy" "iam_full" {
  name        = "PosD_iam_full"
  description = "IAM full policy"
  policy      = "${data.aws_iam_policy_document.iamfull.json}"
}

resource "aws_iam_policy" "iam_restricted" {
  name        = "PosD_iam_restricted"
  description = "IAM restricted policy"
  policy      = "${data.aws_iam_policy_document.iamrestricted.json}"
}

# Assigning policies to groups
resource "aws_iam_group_policy_attachment" "Attach_iam_full_to_PosD_Group_1" {
  group      = "${aws_iam_group.PosD_Group1.name}"
  policy_arn = "${aws_iam_policy.iam_full.arn}"
}

resource "aws_iam_group_policy_attachment" "Attach_iam_restricted_to_PosD_Group_2" {
  group      = "${aws_iam_group.PosD_Group2.name}"
  policy_arn = "${aws_iam_policy.iam_restricted.arn}"
}
