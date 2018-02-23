#!/usr/bin/python

import os, sys, re

#Borrowed from LCM


def convertPath(path):
    separator = os.path.sep;
    osname = os.name;
    path = path.replace('\\', separator);
    path = path.replace('/', separator);
    path = re.sub(r'\\+', r'\\\\', path);
    return path;


def setServerName(currentServerName, newServerName):
    cd('/Servers/' + currentServerName)
    cmo.setName(newServerName)
    cd('/Servers/' + newServerName + '/SSL/' + currentServerName)
    cmo.setName(newServerName)


def configureServer(serverName, host, port):
    cd('/Servers/' + serverName)
    cmo.setListenAddress(host)
    cmo.setListenPort(port)
    cd('/Servers/' + serverName + '/SSL/' + serverName)
    cmo.setEnabled(false)


def createCluster(serverHost, serverPort, serverName, domainHome, secondServerHost, secondServerPort, secondServerName,
                  clusterName):
    cd('/')
    create(clusterName, 'Cluster')
    cd('/Clusters/' + clusterName)
    cmo.setClusterMessagingMode('unicast')

    if secondServerHost == '':
        set('ClusterAddress', serverHost + ':' + str(serverPort))
        assign('Server', serverName, 'Cluster', clusterName)
    else:
        serversHostPort = serverHost + ':' + str(serverPort) + ',' + secondServerHost + ':' + str(secondServerPort)
        set('ClusterAddress', serversHostPort)
        cd('/')
        create(secondServerName, 'Server')
        cd('/Servers/' + secondServerName)
        cmo.setListenAddress(secondServerHost)
        cmo.setListenPort(secondServerPort)
        create(secondServerName, 'SSL')
        cd('SSL/' + secondServerName)
        cmo.setEnabled(false)
        cd('/Servers/' + secondServerName)
        create(secondServerName, 'DefaultFileStore')
        cd('DefaultFileStore/' + secondServerName)
        tlogspath = convertPath(domainHome + '/tlogs')
        cmo.setDirectory(tlogspath)
        serverNames = serverName + ',' + secondServerName
        assign('Server', serverNames, 'Cluster', clusterName)


def createJMSFileStore(serverName, domainHome):
    cd('/')
    defaultStoreDir = convertPath(domainHome + '/tlogs')

    for fileStore in cmo.getFileStores():
        fileStoreDir = convertPath(domainHome + '/jms/' + fileStore.getName())
        fileStore.setDirectory(fileStoreDir)
    cd('/Servers/' + serverName)
    create(serverName, 'DefaultFileStore')
    cd('DefaultFileStore/' + serverName)
    cmo.setDirectory(defaultStoreDir)

