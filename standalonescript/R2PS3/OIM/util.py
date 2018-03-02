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

