#!/bin/bash
source setEnv.sh
$INSTALL_BASE/oracle/scripts/stopOHS.sh
echo "Removing RREG template..."
rm ./input/RREG_OAM11G_Request.xml
echo "Removing Webgate artifacts..."
rm $OHS_INSTANCE/webgate/config/{cwallet.sso*,ObAccessClient.xml,password.xml}
rm $OHS_INSTANCE/webgate/config/simple/*
rm -rf $OHS_INSTANCE/webgate/config/wallet
rm -rf ./output/RREG_DEV1
