import os
import csv
import datetime


def get_dsgraphl(endCursor=None, graphql_DS=None):
    if endCursor is not None:
        graphql_DS = '{ publishedDatasourcesConnection( first: 100, after:' + '"' + endCursor + '")' + graphql_DS + '}'
    else:
        graphql_DS = '{ publishedDatasourcesConnection( first: 100, after: null)' + graphql_DS + '}'
    return graphql_DS


def dscsvfile(filename=None, data=None):
    header = ['date', 'site', 'datasourceproject', 'datasourcename',
              'datasourceid', 'datasourceownername', 'datasourceownereid',
              'datasourceowneremail']
    with open(filename, 'a', encoding='UTF8') as dsdatafile:
        file_is_empty = os.stat(filename).st_size == 0
        writer = csv.writer(dsdatafile)
        # write the header
        if file_is_empty:
            writer.writerow(header)
            writer.writerow(data)
            dsdatafile.close()

        # get the Query details of datasources


def csv_data_ds(query, site, csv_file):
    for index, queries in enumerate(query):
        date = datetime.date.today()
        site = site
        datasourceproject = queries['projectName']
        datasourcename = queries['name']
        datasourceid = queries['id']
        datasourceownername = queries['owner']['name']
        datasourceownereid = queries['owner']['username']
        datasourceowneremail = queries['owner']['email']
        data = [date, site, datasourceproject, datasourcename, datasourceid, datasourceownername, datasourceownereid,
                datasourceowneremail]
        dscsvfile(csv_file, data)
