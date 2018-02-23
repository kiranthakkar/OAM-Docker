import os

DOMAIN_DIR=os.environ.get("OIM_DOMAIN_DIR")
OIM_TEMPLATE=os.environ.get("ORACLE_HOME") + "/common/templates/applications/oracle.oim_11.1.2.0.0_template.jar"
JRF_TEMPLATE=os.environ.get("ORACLE_HOME") + "/oracle_common/common/templates/applications/oracle.jrf.ws.async_template_11.1.1.jar"
OES_TEMPLATE=os.environ.get("ORACLE_HOME") + "/common/templates/applications/oracle.oes_11.1.1.3.0_template.jar"
DB_PASSWORD=os.environ.get("DB_PASSWORD")
DB_URL=os.environ.get("DB_URL")
DB_DRIVER=os.environ.get("DB_DRIVER")
OIM_SCHEMA=os.environ.get("OIM_SCHEMA_PREFIX") + "_OIM"
MDS_SCHEMA=os.environ.get("OIM_SCHEMA_PREFIX") + "_MDS"
OPSS_SCHEMA=os.environ.get("OIM_SCHEMA_PREFIX") + "_OPSS"
SOA_SCHEMA=os.environ.get("OIM_SCHEMA_PREFIX") + "_SOAINFRA"
BI_SCHEMA=os.environ.get("OIM_SCHEMA_PREFIX") + "_BIPLATFORM"
UMS_SCHEMA=os.environ.get("OIM_SCHEMA_PREFIX") + "_ORASDPM"


execfile(r'product_config_util.py')

readDomain(DOMAIN_DIR)
addTemplate(JRF_TEMPLATE)
addTemplate(OIM_TEMPLATE)
addTemplate(OES_TEMPLATE)

machine='AdminNode'
oimCluster='oim_cluster'
oimServer='oim_server1'
oimPort=14000


## Create Machine
cd('/')
create(machine, 'Machine')
cd('Machine/' + machine)
create(machine, 'NodeManager')
cd('NodeManager/' + machine)
set('NMType','SSL')
set('ListenAddress','localhost')
set('ListenPort',5658)
cd('/Servers/AdminServer')
set('Machine',machine)

#Create Cluster
cd('/')
create(oimCluster, 'Cluster')
cd('/Clusters/'+clusterName)
cmo.setClusterMessagingMode('unicast')


#Set Server
cd('/')
cd('Server/' + oimServer)
set('ListenPort',oimPort)
set('Machine',machine)
set('Cluster',oimCluster)

#Create JMS File Store Dir
createJMSFileStore(oimServer,DOMAIN_DIR)

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

    # cd('/JDBCConnectionPool/opss-DBDS')
    # cmo.setDriverName('oracle.jdbc.OracleDriver')
    # cmo.setPasswordEncrypted('<ENCRYPTED VALUE>')
    # set("Properties","user=OIG_OPSS;portNumber=1521;serverName=snake.democo.com")
    # cmo.setURL('jdbc:oracle:thin:@snake.democo.com:1521:%PROVISIONING.IDMPROV.OIM.DB.SID%')

    cd('/JDBCConnectionPool/ApplicationDB')
    set("Properties", "user="+OIM_SCHEMA)
    cd('/JDBCSystemResource/ApplicationDB/JdbcResource/ApplicationDB/JDBCDriverParams/NO_NAME_0')
    cmo.setDriverName('oracle.jdbc.OracleDriver')
    cmo.setPasswordEncrypted(DB_PASSWORD)
    cmo.setUrl(DB_URL)

#End DataSources


"""
cd('/')
cd('JDBCSystemResource/mds-oim/JdbcResource/mds-oim')
dataSourceParams=create('dataSourceParams','JDBCDataSourceParams')
cd('JDBCDataSourceParams/NO_NAME_0')
print "Setting JNDI Names: "
set('JNDIName','jdbc/mds/oim')
cd('/JDBCSystemResource/mds-oam/JdbcResource/mds-oam')
create('myJdbcDriverParams','JDBCDriverParams')
cd('JDBCDriverParams/NO_NAME_0')
set('DriverName',DB_DRIVER)
set('URL',DB_URL)
set('PasswordEncrypted',DB_PASSWORD)
create('myProps','Properties')
cd('Properties/NO_NAME_0')
#create('user', 'Property')
cd('Property/user')
cmo.setValue(MDS_SCHEMA)

cd('/JDBCSystemResources/mds-oam/JdbcResource/mds-oam/JDBCDriverParams/NO_NAME_0')
create('myProps','Properties')
cd('Properties/NO_NAME_0')
#create('SendStreamAsBlob', 'Property')
cd('Property/SendStreamAsBlob')
cmo.setValue('true')

cd('/JDBCSystemResources/mds-oam/JdbcResource/mds-oam/JDBCDriverParams/NO_NAME_0')
create('myProps','Properties')
cd('Properties/NO_NAME_0')
#create('oracle.net.CONNECT_TIMEOUT', 'Property')
cd('Property/oracle.net.CONNECT_TIMEOUT')
cmo.setValue('10000')

cd('/')
#create('mds-owsm', 'JDBCSystemResource')
cd('JDBCSystemResource/mds-owsm/JdbcResource/mds-owsm')
dataSourceParams=create('dataSourceParams','JDBCDataSourceParams')
cd('JDBCDataSourceParams/NO_NAME_0')
print "Setting JNDI Names: "
set('JNDIName','jdbc/mds/owsm')
cd('/JDBCSystemResource/mds-owsm/JdbcResource/mds-owsm')
create('myJdbcDriverParams','JDBCDriverParams')
cd('JDBCDriverParams/NO_NAME_0')
set('DriverName',DB_DRIVER)
set('URL',DB_URL)
set('PasswordEncrypted',DB_PASSWORD)
create('myProps','Properties')
cd('Properties/NO_NAME_0')
#create('user', 'Property')
cd('Property/user')
cmo.setValue(MDS_SCHEMA)

cd('/JDBCSystemResources/mds-owsm/JdbcResource/mds-owsm/JDBCDriverParams/NO_NAME_0')
create('myProps','Properties')
cd('Properties/NO_NAME_0')
#create('SendStreamAsBlob', 'Property')
cd('Property/SendStreamAsBlob')
cmo.setValue('true')

cd('/JDBCSystemResources/mds-owsm/JdbcResource/mds-owsm/JDBCDriverParams/NO_NAME_0')
create('myProps','Properties')
cd('Properties/NO_NAME_0')
#create('oracle.net.CONNECT_TIMEOUT', 'Property')
cd('Property/oracle.net.CONNECT_TIMEOUT')
cmo.setValue('10000')



cd('/')
assign('JDBCSystemResource', 'mds-oam', 'Target', policyServer)

assign('JDBCSystemResource', 'mds-owsm', 'Target', omsmServer)

assign('JDBCSystemResource', 'oamDS', 'Target', 'AdminServer')
assign('JDBCSystemResource', 'oamDS', 'Target', oamCluster)
assign('JDBCSystemResource', 'oamDS', 'Target', policyServer)

assign('JDBCSystemResource', 'omsm-ds', 'Target', omsmServer)
assign('JDBCSystemResource', 'omsm-ds', 'Target', policyServer)

assign('JDBCSystemResource', 'opss-DBDS', 'Target', 'AdminServer')
assign('JDBCSystemResource', 'opss-DBDS', 'Target', oimCluster)
assign('JDBCSystemResource', 'opss-DBDS', 'Target', policyServer)
assign('JDBCSystemResource', 'opss-DBDS', 'Target', soaServer)

updateDomain()
"""

exit()

