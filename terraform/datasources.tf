data "aws_iam_policy_document" "iamfull" {
  statement {
    actions = [ "iam:*" ]
    resources = [ "*" ]
  }
}

data "aws_iam_policy_document" "iamrestricted" {
  statement {
    actions = [ "iam:Get*", "iam:List*" ]
    resources = [ "*" ]
  }
}
