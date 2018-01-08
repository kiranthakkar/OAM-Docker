readTemplate("/u01/oracle/middleware/wlserver_10.3/common/templates/domains/wls.jar")

cd('Servers/AdminServer')
set('ListenAddress','')
set('ListenPort', 7001)

create('AdminServer','SSL')
cd('SSL/AdminServer')
set('Enabled', 'True')
set('ListenPort', 7002)


cd('/')
cd('Security/base_domain/User/weblogic')
cmo.setPassword('*****')
# Please set password here before using this script, e.g. cmo.setPassword('value')


setOption('OverwriteDomain', 'true')
writeDomain('/u01/oracle/middleware/user_projects/domains/OAMDomain')
closeTemplate()
exit()

