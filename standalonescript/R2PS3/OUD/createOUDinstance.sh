#!/bin/bash

# Variables
source setEnv.sh

# Create required root user password file
echo -n "${OUD_ROOTPASSWORD}" > ${OUD_HOME}/rootUserPwd.txt

# Create OUD instance and start after completed
${OUD_HOME}/oud-setup \
--cli --no-prompt \
--baseDN "${OUD_BASEDN}" \
--ldapPort 1389 \
--adminConnectorPort 4444 \
--rootUserDN "cn=Directory Manager" \
--rootUserPasswordFile ${OUD_HOME}/rootUserPwd.txt \
--enableStartTLS \
--ldapsPort 1636 \
--generateSelfSignedCertificate \
--hostname ${OUD_HOSTNAME} \
--sampleData 10 \
--offlineToolsTuning autotune

# Get OUD LDAP Status
$OUD_INSTANCE/OUD/bin/status \
--bindDN "cn=Directory Manager" \
--bindPasswordFile ${OUD_HOME}/rootUserPwd.txt \
--no-prompt

# Clean up root user password file
rm -f ${OUD_HOME}/rootUserPwd.txt
