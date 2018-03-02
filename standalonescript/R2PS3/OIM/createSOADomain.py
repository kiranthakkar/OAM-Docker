import os

DOMAIN_DIR=os.environ.get("OIM_DOMAIN_DIR")
SOA_TEMPLATE=os.environ.get("MW_HOME") + "/soa/common/templates/applications/oracle.soa_template_11.1.1.jar"

DB_PASSWORD=os.environ.get("DB_PASSWORD")
DB_URL=os.environ.get("DB_URL")
DB_DRIVER=os.environ.get("DB_DRIVER")
MDS_SCHEMA=os.environ.get("OIM_SCHEMA_PREFIX") + "_MDS"
SOA_SCHEMA=os.environ.get("OIM_SCHEMA_PREFIX") + "_SOAINFRA"
UMS_SCHEMA=os.environ.get("OIM_SCHEMA_PREFIX") + "_ORASDPM"

print 'Extending Domain for SOA...'

execfile(os.getcwd()+r'/util.py')


readDomain(DOMAIN_DIR)
cd('/')
setOption('AppDir', DOMAIN_DIR+r'/applications')
addTemplate(SOA_TEMPLATE)


machine='AdminNode'
soaCluster='soa_cluster'
soaServer='soa_server1'


#Create Cluster
cd('/')
create(soaCluster, 'Cluster')
cd('/Clusters/'+soaCluster)
cmo.setClusterMessagingMode('unicast')

# Server
cd('/')
cd('Server/' + soaServer)
set('ListenPort',8001)
set('Machine',machine)
set('Cluster',soaCluster)

#Create JMS File Store Dir
createJMSFileStore(soaServer,DOMAIN_DIR)

#Set JMS to UDD
cd('/')
for mod in cmo.getJMSSystemResources():
    setDistDestType(mod.getName(), 'UDD')


# Data Sources

cd('/JDBCConnectionPool/mds-owsm')
set("Properties", "user="+MDS_SCHEMA)
cd('/JDBCSystemResource/mds-owsm/JdbcResource/mds-owsm/JDBCDriverParams/NO_NAME_0')
cmo.setUrl(DB_URL)
cmo.setDriverName('oracle.jdbc.OracleDriver')
cmo.setPasswordEncrypted(DB_PASSWORD)
print 'here1'

cd('/JDBCConnectionPool/OraSDPMDataSource')
set("Properties", "user="+UMS_SCHEMA)
cd('/JDBCSystemResource/OraSDPMDataSource/JdbcResource/OraSDPMDataSource/JDBCDriverParams/NO_NAME_0')
cmo.setUrl(DB_URL)
cmo.setDriverName('oracle.jdbc.OracleDriver')
cmo.setPasswordEncrypted(DB_PASSWORD)
print 'here2'

cd('/JDBCConnectionPool/SOADataSource')
set("Properties", "user="+SOA_SCHEMA)
cd('/JDBCSystemResource/SOADataSource/JdbcResource/SOADataSource/JDBCDriverParams/NO_NAME_0')
cmo.setDriverName('oracle.jdbc.xa.client.OracleXADataSource')
cmo.setPasswordEncrypted(DB_PASSWORD)
cmo.setUrl(DB_URL)
print 'here3'

cd('/JDBCConnectionPool/SOALocalTxDataSource')
set("Properties", "user="+SOA_SCHEMA)
cd('/JDBCSystemResource/SOALocalTxDataSource/JdbcResource/SOALocalTxDataSource/JDBCDriverParams/NO_NAME_0')
cmo.setDriverName('oracle.jdbc.OracleDriver')
cmo.setPasswordEncrypted(DB_PASSWORD)
cmo.setUrl(DB_URL)
print 'here4'

cd('/JDBCConnectionPool/EDNDataSource')
set("Properties", "user="+SOA_SCHEMA)
cd('/JDBCSystemResource/EDNDataSource/JdbcResource/EDNDataSource/JDBCDriverParams/NO_NAME_0')
cmo.setDriverName('oracle.jdbc.xa.client.OracleXADataSource')
cmo.setPasswordEncrypted(DB_PASSWORD)
cmo.setUrl(DB_URL)
print 'here5'

cd('/JDBCConnectionPool/EDNLocalTxDataSource')
set("Properties", "user="+SOA_SCHEMA)
cd('/JDBCSystemResource/EDNLocalTxDataSource/JdbcResource/EDNLocalTxDataSource/JDBCDriverParams/NO_NAME_0')
cmo.setDriverName('oracle.jdbc.OracleDriver')
cmo.setPasswordEncrypted(DB_PASSWORD)
cmo.setUrl(DB_URL)
print 'here6'

cd('/JDBCConnectionPool/mds-soa')
set("Properties", "user="+MDS_SCHEMA)
cd('/JDBCSystemResource/mds-soa/JdbcResource/mds-soa/JDBCDriverParams/NO_NAME_0')
cmo.setDriverName('oracle.jdbc.OracleDriver')
cmo.setPasswordEncrypted(DB_PASSWORD)
cmo.setUrl(DB_URL)
print 'here7'

#End Data Sources


updateDomain()
closeDomain()
exit()

