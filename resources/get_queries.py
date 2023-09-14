import os
import csv

def get_queriesgraphql(endCursor=None, graphql_queries=None):
    if endCursor is not None:
        graphql_queries = '{ customSQLTablesConnection( first: 100, after:' + '"' + endCursor + '")' + graphql_queries + '}'
    else:
        graphql_queries = '{ customSQLTablesConnection( first: 100, after: null)' + graphql_queries + '}'
    return graphql_queries


def queriescsvfile(filename=None, data=None):
    header = ['date', 'site', 'workBookproject', 'workbookname', 'workbookid', 'datasourceproject', 'datasourcename',
              'datasourceid', 'ownername', 'ownerusername', 'owneremail', 'sqlqueryid', 'sqlqueryname', 'sqlquery',
              'tables']
    with open(filename, 'a', encoding='UTF8') as queriesdatafile:
        file_is_empty = os.stat(filename).st_size == 0
        writer = csv.writer(queriesdatafile)
        # write the header
        if file_is_empty:
            writer.writerow(header)
            writer.writerow(data)
            queriesdatafile.close()

        # get the Query details


def csv_data_queries(query, site, csv_file):
    for index, queries in enumerate(query):
        date = datetime.date.today()
        sql_queries = sql_tables.sql_tables(queries['query'])
        site = site
        sqlqueryid = queries['id']
        sqlqueryname = queries['name']
        sqlquery = queries['query']
        sqlquerydatabase = queries['database']['name']
        sqlquerydatabaseconnectiontype = queries['database']['connectionType']
        tables = sql_queries
        if (queries['downstreamDatasources'] == []) and (queries['downstreamWorkbooks'] != []):
            workBookproject = queries['downstreamWorkbooks'][0]['projectName']
            workbookname = queries['downstreamWorkbooks'][0]['name']
            workbookid = queries['downstreamWorkbooks'][0]['id']
            ownername = queries['downstreamWorkbooks'][0]['owner']['name']
            ownerusername = queries['downstreamWorkbooks'][0]['owner']['username']
            owneremail = queries['downstreamWorkbooks'][0]['owner']['email']
            datasourceproject = "Empty"
            datasourcename = "Empty"
            datasourceid = "Empty"
            data = [date, site, workBookproject, workbookname, workbookid, datasourceproject, datasourcename,
                    datasourceid, ownername, ownerusername, owneremail, sqlqueryid, sqlqueryname, sqlquery, tables]
            queriescsvfile(csv_file, data)
        elif (queries['downstreamWorkbooks'] == []) and (queries['downstreamDatasources'] != []):
            workBookproject = "Empty"
            workbookname = "Empty"
            workbookid = "Empty"
            datasourceproject = queries['downstreamDatasources'][0]['projectName']
            datasourcename = queries['downstreamDatasources'][0]['name']
            datasourceid = queries['downstreamDatasources'][0]['id']
            ownername = queries['downstreamDatasources'][0]['owner']['name']
            ownerusername = queries['downstreamDatasources'][0]['owner']['username']
            owneremail = queries['downstreamDatasources'][0]['owner']['email']
            data = [date, site, workBookproject, workbookname, workbookid, datasourceproject, datasourcename,
                    datasourceid, ownername, ownerusername, owneremail, sqlqueryid, sqlqueryname, sqlquery, tables]
            queriescsvfile(csv_file, data)
        elif (queries['downstreamWorkbooks']) == [] and (queries['downstreamDatasources'] == []):
            workBookproject = "Empty"
            workbookname = "Empty"
            workbookid = "Empty"
            datasourceproject = "Empty"
            datasourcename = "Empty"
            datasourceid = "Empty"
            ownername = "Empty"
            ownerusername = "Empty"
            owneremail = "Empty"
            data = [date, site, workBookproject, workbookname, workbookid, datasourceproject, datasourcename,
                    datasourceid,
                    ownername, ownerusername, owneremail, sqlqueryid, sqlqueryname, sqlquery, tables]
            queriescsvfile(csv_file, data)
        elif (queries['downstreamWorkbooks']) != [] and (queries['downstreamDatasources'] != []):
            workBookproject = queries['downstreamWorkbooks'][0]['projectName']
            workbookname = queries['downstreamWorkbooks'][0]['name']
            workbookid = queries['downstreamWorkbooks'][0]['id']
            datasourceproject = queries['downstreamDatasources'][0]['projectName']
            datasourcename = queries['downstreamDatasources'][0]['name']
            datasourceid = queries['downstreamDatasources'][0]['id']
            ownername = queries['downstreamWorkbooks'][0]['owner']['name']
            ownerusername = queries['downstreamWorkbooks'][0]['owner']['username']
            owneremail = queries['downstreamWorkbooks'][0]['owner']['email']
            data = [date, site, workBookproject, workbookname, workbookid, datasourceproject, datasourcename,
                    datasourceid,
                    ownername, ownerusername, owneremail, sqlqueryid, sqlqueryname, sqlquery, tables]
            queriescsvfile(csv_file, data)
