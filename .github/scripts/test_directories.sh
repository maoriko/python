#!/bin/bash
set -e
set -x
_USERS=$(dscl . list /Users | grep -v "^_")
for user in $_USERS; do
    _dir=/Users/$user
    if [ -d "$_dir" ]; then
      cat << EOF > $_dir/.test-akeyless-sphere.rc
      identity_file=""
      cert_issuer_name="akeyless-zero-trust/staging/cert-issuer"
      profile="akeyless-zero-trust"
      BASTION_API_PROTO_=https
EOF
      chmod 444 $_dir/.test-akeyless-sphere.rc
    fi
done
cat $_dir/.test-akeyless-sphere.rc
#
#for user in $_USERS; do
#    _dir=/Users/$user
#    if [ -d "$_dir" ]; then
#		  cat << EOF > $_dir/.akeyless/profiles/test-akeyless-zero-trust.toml
#		  ["akeyless-zero-trust"]
#		  access_id = "p-6lpq3mwugkqv"
#  		access_type = "saml"
#EOF
#      chmod 444 $_dir/.akeyless/profiles/test-akeyless-zero-trust.toml
#    fi
#done
#cat $_dir/.akeyless/profiles/test-akeyless-zero-trust.toml