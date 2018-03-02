import os

DOMAIN_DIR=os.environ.get("OIM_DOMAIN_DIR")
OIM_TEMPLATE=os.environ.get("ORACLE_HOME") + "/common/templates/applications/oracle.oim_11.1.2.0.0_template.jar"
JRF_TEMPLATE=os.environ.get("MW_HOME") + "/oracle_common/common/templates/applications/oracle.jrf.ws.async_template_11.1.1.jar"
OES_TEMPLATE=os.environ.get("ORACLE_HOME") + "/common/templates/applications/oracle.oes_11.1.1.3.0_template.jar"
DB_PASSWORD=os.environ.get("DB_PASSWORD")
DB_URL=os.environ.get("DB_URL")
DB_DRIVER=os.environ.get("DB_DRIVER")
OIM_SCHEMA=os.environ.get("OIM_SCHEMA_PREFIX") + "_OIM"
MDS_SCHEMA=os.environ.get("OIM_SCHEMA_PREFIX") + "_MDS"
BIP_SCHEMA=os.environ.get("OIM_SCHEMA_PREFIX") + "_BIPLATFORM"

machine='AdminNode'
oimCluster='oim_cluster'
oimServer='oim_server1'
oimPort=14000
biCluster='bi_cluster'
biServer='bi_server1'

execfile(os.getcwd()+r'/util.py')

print 'Extending Domain for OIM...'

readDomain(DOMAIN_DIR)
cd('/')
setOption('AppDir', DOMAIN_DIR+r'/applications')
addTemplate(JRF_TEMPLATE)
addTemplate(OIM_TEMPLATE)
addTemplate(OES_TEMPLATE)



#Create OIM Cluster
cd('/')
create(oimCluster, 'Cluster')
cd('/Clusters/'+oimCluster)
cmo.setClusterMessagingMode('unicast')

#Create BIP Cluster
cd('/')
create(biCluster, 'Cluster')
cd('/Clusters/'+biCluster)
cmo.setClusterMessagingMode('unicast')


#OIM Server
cd('/')
cd('Server/' + oimServer)
set('ListenPort',oimPort)
set('Machine',machine)
set('Cluster',oimCluster)

# BIP Server
cd('/')
cd('Server/' + biServer)
set('ListenPort',9704)
set('Machine',machine)
set('Cluster',biCluster)

#Create OIM JMS File Store Dir
createJMSFileStore(oimServer,DOMAIN_DIR)

#Create BIP JMS File Store Dir
createJMSFileStore(biServer,DOMAIN_DIR)

#Set JMS to UDD
cd('/')
for mod in cmo.getJMSSystemResources():
    setDistDestType(mod.getName(), 'UDD')

#Datasources


cd('/JDBCConnectionPool/oimOperationsDB')
set("Properties", "user="+OIM_SCHEMA)
cd('/JDBCSystemResource/oimOperationsDB/JdbcResource/oimOperationsDB/JDBCDriverParams/NO_NAME_0')
cmo.setDriverName('oracle.jdbc.xa.client.OracleXADataSource')
cmo.setPasswordEncrypted(DB_PASSWORD)
cmo.setUrl(DB_URL)

cd('/JDBCConnectionPool/mds-oim')
set("Properties", "user="+MDS_SCHEMA)
cd('/JDBCSystemResource/mds-oim/JdbcResource/mds-oim/JDBCDriverParams/NO_NAME_0')
cmo.setDriverName('oracle.jdbc.OracleDriver')
cmo.setPasswordEncrypted(DB_PASSWORD)
cmo.setUrl(DB_URL)

cd('/JDBCConnectionPool/oimJMSStoreDS')
set("Properties", "user="+OIM_SCHEMA)
cd('/JDBCSystemResource/oimJMSStoreDS/JdbcResource/oimJMSStoreDS/JDBCDriverParams/NO_NAME_0')
cmo.setDriverName('oracle.jdbc.OracleDriver')
cmo.setPasswordEncrypted(DB_PASSWORD)
cmo.setUrl(DB_URL)

cd('/JDBCConnectionPool/soaOIMLookupDB')
set("Properties", "user="+OIM_SCHEMA)
cd('/JDBCSystemResource/soaOIMLookupDB/JdbcResource/soaOIMLookupDB/JDBCDriverParams/NO_NAME_0')
cmo.setDriverName('oracle.jdbc.xa.client.OracleXADataSource')
cmo.setPasswordEncrypted(DB_PASSWORD)
cmo.setUrl(DB_URL)

cd('/JDBCConnectionPool/ApplicationDB')
set("Properties", "user="+OIM_SCHEMA)
cd('/JDBCSystemResource/ApplicationDB/JdbcResource/ApplicationDB/JDBCDriverParams/NO_NAME_0')
cmo.setDriverName('oracle.jdbc.OracleDriver')
cmo.setPasswordEncrypted(DB_PASSWORD)
cmo.setUrl(DB_URL)

cd('/JDBCConnectionPool/bip_datasource')
set("Properties","user="+BIP_SCHEMA)
cd('/JDBCSystemResource/bip_datasource/JdbcResource/bip_datasource/JDBCDriverParams/NO_NAME_0')
cmo.setDriverName('oracle.jdbc.OracleDriver')
cmo.setPasswordEncrypted(DB_PASSWORD)
cmo.setUrl(DB_URL)

#End DataSources




updateDomain()
closeDomain()

exit()

