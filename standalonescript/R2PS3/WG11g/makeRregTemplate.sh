#!/bin/bash
source setEnv.sh
CURRENT_PATH=`pwd`
cp ./input/$RREG_TEMPLATE ./input/$RREG_AGENT11G
echo OAMHOST | sed -i 's/OAMHOST/'$OAMHOST'/g' ./input/$RREG_AGENT11G
echo OHSHOST | sed -i 's/OHSHOST/'$OHSHOST'/g' ./input/$RREG_AGENT11G
(echo $DOMAIN_USERNAME; echo $DOMAIN_PASSWORD; echo $DOMAIN_PASSWORD) | ./bin/oamreg.sh inband ${CURRENT_PATH}/input/${RREG_AGENT11G} -noprompt
echo "Copying Webgate artifacts..."
cp ./output/RREG_DEV1/{cwallet.sso*,ObAccessClient.xml,password.xml} $OHS_INSTANCE/webgate/config/
cp -r ./output/RREG_DEV1/wallet $OHS_INSTANCE/webgate/config/
cp ./output/RREG_DEV1/aaa_* $OHS_INSTANCE/webgate/config/simple
echo "Finished copying Webgate artifacts..."
echo "Starting OHS..."
$INSTALL_BASE/oracle/scripts/startOHS.sh
