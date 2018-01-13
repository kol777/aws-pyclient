output "password_for_PosD1" {
  value = "${aws_iam_user_login_profile.PosD1_lp.encrypted_password}"
}

output "password_for_PosD2" {
  value = "${aws_iam_user_login_profile.PosD2_lp.encrypted_password}"
}
