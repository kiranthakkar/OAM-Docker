import os

DOMAIN_DIR=os.environ.get("OIM_DOMAIN_DIR")
OAM_TEMPLATE=os.environ.get("ORACLE_HOME") + "/common/templates/applications/oracle.oim_11.1.2.0.0_template.jar"
DB_PASSWORD=os.environ.get("DB_PASSWORD")
DB_URL=os.environ.get("DB_URL")
DB_DRIVER=os.environ.get("DB_DRIVER")
OIM_SCHEMA=os.environ.get("OIM_SCHEMA_PREFIX") + "_OIM"
MDS_SCHEMA=os.environ.get("OIM_SCHEMA_PREFIX") + "_MDS"
OPSS_SCHEMA=os.environ.get("OIM_SCHEMA_PREFIX") + "_OPSS"
SOA_SCHEMA=os.environ.get("OIM_SCHEMA_PREFIX") + "_SOAINFRA"
BI_SCHEMA=os.environ.get("OIM_SCHEMA_PREFIX") + "_BIPLATFORM"
UMS_SCHEMA=os.environ.get("OIM_SCHEMA_PREFIX") + "_ORASDPM"

readDomain(DOMAIN_DIR)
addTemplate(OIM_TEMPLATE)

machine='AdminNode'
oamCluster='oim_cluster'
oamServer='oim_server1'
soaServer='soa_server1'
biServer='bi_server1'

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

cd('/')
create(oimCluster, 'Cluster')

cd('/')
#create(oimServer, 'Server')
cd('Server/' + oimServer)
set('ListenPort',14000)
set('Machine',machine)
set('Cluster',oimCluster)

cd('/')
#create(soaServer, 'Server')
cd('Server/' + soaServer)
set('ListenPort',8001)
set('Machine',machine)

cd('/')
#create(policyServer, 'Server')
cd('Server/' + biServer)
set('ListenPort',9704)
set('Machine',machine)

cd('/')
#create('mds-oim', 'JDBCSystemResource')
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
#create('oamDS', 'JDBCSystemResource')
cd('JDBCSystemResource/oamDS/JdbcResource/oamDS')
dataSourceParams=create('dataSourceParams','JDBCDataSourceParams')
cd('JDBCDataSourceParams/NO_NAME_0')
print "Setting JNDI Names: "
set('JNDIName','jdbc/oamds')
cd('/JDBCSystemResource/oamDS/JdbcResource/oamDS')
create('myJdbcDriverParams','JDBCDriverParams')
cd('JDBCDriverParams/NO_NAME_0')
set('DriverName',DB_DRIVER)
set('URL',DB_URL)
set('PasswordEncrypted',DB_PASSWORD)
create('myProps','Properties')
cd('Properties/NO_NAME_0')
#create('user', 'Property')
cd('Property/user')
cmo.setValue(OAM_SCHEMA)

cd('/JDBCSystemResources/oamDS/JdbcResource/oamDS/JDBCDriverParams/NO_NAME_0')
create('myProps','Properties')
cd('Properties/NO_NAME_0')
create('SendStreamAsBlob', 'Property')
cd('Property/SendStreamAsBlob')
cmo.setValue('true')

cd('/JDBCSystemResources/oamDS/JdbcResource/oamDS/JDBCDriverParams/NO_NAME_0')
create('myProps','Properties')
cd('Properties/NO_NAME_0')
#create('oracle.net.CONNECT_TIMEOUT', 'Property')
cd('Property/oracle.net.CONNECT_TIMEOUT')
cmo.setValue('10000')

cd('/')
#create('omsm-ds', 'JDBCSystemResource')
cd('JDBCSystemResource/omsm-ds/JdbcResource/omsm-ds')
dataSourceParams=create('dataSourceParams','JDBCDataSourceParams')
cd('JDBCDataSourceParams/NO_NAME_0')
print "Setting JNDI Names: "
set('JNDIName','jdbc/omsm-ds')
cd('/JDBCSystemResource/omsm-ds/JdbcResource/omsm-ds')
create('myJdbcDriverParams','JDBCDriverParams')
cd('JDBCDriverParams/NO_NAME_0')
set('DriverName',DB_DRIVER)
set('URL',DB_URL)
set('PasswordEncrypted',DB_PASSWORD)
create('myProps','Properties')
cd('Properties/NO_NAME_0')
#create('user', 'Property')
cd('Property/user')
cmo.setValue(OMSM_SCHEMA)

cd('/JDBCSystemResources/omsm-ds/JdbcResource/omsm-ds/JDBCDriverParams/NO_NAME_0')
create('myProps','Properties')
cd('Properties/NO_NAME_0')
#create('oracle.net.CONNECT_TIMEOUT', 'Property')
cd('Property/oracle.net.CONNECT_TIMEOUT')
cmo.setValue('10000')

cd('/')
#create('opss-DBDS', 'JDBCSystemResource')
cd('JDBCSystemResource/opss-DBDS/JdbcResource/opss-DBDS')
dataSourceParams=create('dataSourceParams','JDBCDataSourceParams')
cd('JDBCDataSourceParams/NO_NAME_0')
print "Setting JNDI Names: "
set('JNDIName','jdbc/OPSSDBDS')
cd('/JDBCSystemResource/opss-DBDS/JdbcResource/opss-DBDS')
create('myJdbcDriverParams','JDBCDriverParams')
cd('JDBCDriverParams/NO_NAME_0')
set('DriverName',DB_DRIVER)
set('URL',DB_URL)
set('PasswordEncrypted',DB_PASSWORD)
create('myProps','Properties')
cd('Properties/NO_NAME_0')
#create('user', 'Property')
cd('Property/user')
cmo.setValue(OPSS_SCHEMA)

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

exit()

