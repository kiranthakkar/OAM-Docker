#!/usr/bin/python

import os, sys


dataSources= 'mds-owsm,OraSDPMDataSource,SOADataSource,SOALocalTxDataSource,EDNDataSource,EDNLocalTxDataSource,mds-soa,opss-DBDS,oimOperationsDB,mds-oim,bip_datasource,oimJMSStoreDS,soaOIMLookupDB,ApplicationDB'
DB_URL=os.environ.get("DB_URL")

# Updated datasource jdbc url in NON-RAC DB

connect(os.environ.get("DOMAIN_USERNAME"), os.environ.get("DOMAIN_PASSWORD"), 't3://localhost:7001')
edit()
startEdit()

for dsName in dataSources.split(','):

    cd('/JDBCSystemResources/' + dsName + '/JDBCResource/' + dsName + '/JDBCDriverParams/' + dsName)
    cmo.setUrl(DB_URL)

save()
activate()
disconnect()
exit()