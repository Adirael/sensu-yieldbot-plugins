#!/usr/bin/env python

from optparse import OptionParser
import socket
import sys
import httplib
import json

PASS = 0
FAIL = 1

adservers = {}
adservers["east"] = []
adservers["west"] = []

def get_bongo_host(server, app):
    try:
        con = httplib.HTTPConnection(server, timeout=45)
        con.request("GET","/v2/apps/" + app)
        data = con.getresponse()
        if data.status >= 300:
            print "Recieved non-2xx response= %s in get_bongo_host" % (data.status)
            sys.exit(FAIL)
        json_data = json.loads(data.read())
        host = json_data['app']['tasks'][0]['host']
        port = json_data['app']['tasks'][0]['ports'][0]
        con.close()
        return host, port
    except Exception, e:
        print "%s Exception caught in get_bongo_host" % (e)
        sys.exit(FAIL)

def get_status(host, region):
    sys.exit(PASS)
    '''
    output = "\n"
    con = httplib.HTTPConnection(host,timeout=45)
    for i in range(len(adservers[region])):
        try:
            con.request("GET","/v1/adserver/health/" + adservers[region][i])
            data = con.getresponse()
            if data.status >= 300:
                output = output + "%s status: Recieved non-2xx response= %s \n" % (adservers[region][i], data.status)
            else:
                json_data = json.loads(data.read())
                if json_data['status'] == 1:
                    output = output + "%s status= %s \n" % (adservers[region][i], json_data['msg'])
        except Exception, e:
            output = output + "%s Exception caught for adserver %s in get_status" % (e,adservers[region][i])
    con.close()
    if output == "\n":
        print "mirror-maker on `adservers` are fine"
        sys.exit(PASS)
    else:
        print output
        sys.exit(FAIL)
    '''

if __name__=="__main__":
    parser = OptionParser()
    parser.add_option("-s", dest="server", action="store", default="localhost:8080", help="Marathon Cluster address with port no")
    parser.add_option("-a", dest="app", action="store", default="bongo.useast.prod", help="App Id to retrieve the slave address")
    parser.add_option("-r", dest="region", action="store", default="east", help="Region for which adservers health has to be checked")
    (options, args) = parser.parse_args()
    host, port = get_bongo_host(options.server, options.app)
    if "useast" in host:
        host = host.rsplit("prd",1)
        consul_host = "%snode.us-east-1.consul:%s" % (host[0], port)
    else:
        consul_host = "%s:%s" % (host, port)
    get_status(consul_host, options.region)
