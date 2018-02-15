WLST_SCRIPT=$ORACLE_HOME/common/bin/wlst.sh

$WLST_SCRIPT createOAMDomain.py
$WLST_SCRIPT $ORACLE_HOME/common/tools/configureSecurityStore.py -d $OAM_DOMAIN_DIR -c IAM -p $DB_PASSWORD -m create
