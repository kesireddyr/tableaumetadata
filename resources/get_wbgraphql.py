import os
import csv
import datetime


def get_wbgraphl(endCursor=None, graphql_WB=None):
    if endCursor is not None:
        graphql_WB = '{ workbooksConnection( first: 100, after:' + '"' + endCursor + '")' + graphql_WB + '}'
    else:
        graphql_WB = '{ workbooksConnection( first: 100, after: null)' + graphql_WB + '}'
    return graphql_WB


def wbcsvfile(filename=None, data=None):
    header = ['date', 'site', 'workBookproject', 'workbookname', 'workbookid',
              'workbookownername', 'workbookownereid', 'workbookowneremail',
              'upstreamdatabasename', 'upstreamdatabaseconnectionType',
              'embeddeddatasourcename', 'embeddeddatasourceid']
    with open(filename, 'a', encoding='UTF8') as wbdatafile:
        file_is_empty = os.stat(filename).st_size == 0
        writer = csv.writer(wbdatafile)
        # write the header
        if file_is_empty: writer.writerow(header)
        writer.writerow(data)
        wbdatafile.close()

    # get the Query details of workbook


def csv_data_wb(query, site, csv_file):
    for index, queries in enumerate(query):
        date = datetime.date.today()
        site = site
        workBookproject = queries['projectName']
        workbookname = queries['name']
        workbookid = queries['id']
        workbookownername = queries['owner']['name']
        workbookownereid = queries['owner']['username']
        workbookowneremail = queries['owner']['email']
        if (queries['upstreamDatabases'] == []) and (queries['embeddedDatasources'] != []):
            upstreamdatabasename = "empty"
            upstreamdatabaseconnectionType = "empty"
            embeddeddatasourcename = queries['embeddedDatasources'][0]['name']
            embeddeddatasourceid = queries['embeddedDatasources'][0]['id']
            data = [date, site, workBookproject, workbookname, workbookid, workbookownername, workbookownereid,
                    workbookowneremail, upstreamdatabasename, upstreamdatabaseconnectionType, embeddeddatasourcename,
                    embeddeddatasourceid]
            wbcsvfile(csv_file, data)
        elif (queries['upstreamDatabases'] != []) and (queries['embeddedDatasources'] == []):
            upstreamdatabasename = queries['upstreamDatabases'][0]['name']
            upstreamdatabaseconnectionType = queries['upstreamDatabases'][0]['connectionType']
            embeddeddatasourcename = "empty"
            embeddeddatasourceid = "empty"
            data = [date, site, workBookproject, workbookname, workbookid, workbookownername, workbookownereid,
                    workbookowneremail, upstreamdatabasename, upstreamdatabaseconnectionType, embeddeddatasourcename,
                    embeddeddatasourceid]
            wbcsvfile(csv_file, data)
        elif (queries['embeddedDatasources'] != []) and (queries['upstreamDatabases'] != []):
            upstreamdatabasename = queries['upstreamDatabases'][0]['name']
            upstreamdatabaseconnectionType = queries['upstreamDatabases'][0]['connectionType']
            embeddeddatasourcename = queries['embeddedDatasources'][0]['name']
            embeddeddatasourceid = queries['embeddedDatasources'][0]['id']
            data = [date, site, workBookproject, workbookname, workbookid, workbookownername, workbookownereid,
                    workbookowneremail,
                    upstreamdatabasename, upstreamdatabaseconnectionType, embeddeddatasourcename, embeddeddatasourceid]
            wbcsvfile(csv_file, data)
        elif (queries['embeddedDatasources'] == []) and (queries['upstreamDatabases'] == []):
            upstreamdatabasename = "empty"
            upstreamdatabaseconnectionType = "empty"
            embeddeddatasourcename = "empty"
            embeddeddatasourceid = "empty"
            data = [date, site, workBookproject, workbookname, workbookid, workbookownername, workbookownereid,
                    workbookowneremail,
                    upstreamdatabasename, upstreamdatabaseconnectionType, embeddeddatasourcename, embeddeddatasourceid]
            wbcsvfile(csv_file, data)
