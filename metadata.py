import tableauserverclient as tsc
from resources import get_config, get_queries, get_dsgraphql, get_wbgraphql, truncate_csv


def query_details(server=None, graphql_queries=None, graphql_WB=None, graphql_DS=None, config_details=None,
                  site=None):
    if site == '':
        site = "Default"
        # meta data queries loaded
        metadata_queries = get_queries.get_queriesgraphql(graphql_queries=graphql_queries)
        resp_queries = server.metadata.query(metadata_queries)
        print("total count of queries of {0} is {1}.".format(site, resp_queries['data']['customSQLTablesConnection'][
            'totalCount']))
        metadata_results = resp_queries['data']['customSQLTablesConnection']['nodes']
        while resp_queries['data']['customSQLTablesConnection']['pageInfo']['hasNextPage']:
            metadata_queries = get_queries.get_queriesgraphql(graphql_queries=graphql_queries, endCursor=
            resp_queries['data']['customSQLTablesConnection']['pageInfo']['endCursor'])
            resp_queries = server.metadata.query(metadata_queries)
            metadata_results = metadata_results + resp_queries['data']['customSQLTablesConnection']['nodes']
            get_queries.csv_data_queries(metadata_results, site, config_details["json_queries"])
            # wb queries loaded
        wb_queries = get_wbgraphql.get_wbgraphl(graphql_WB=graphql_WB)
        resp_queries = server.metadata.query(wb_queries)
        print("total count of Workbooks of {0} is {1}.".format(site, resp_queries['data']['workbooksConnection'][
            'totalCount']))
        wb_results = resp_queries['data']['workbooksConnection']['nodes']
        while resp_queries['data']['workbooksConnection']['pageInfo']['hasNextPage']:
            wb_queries = get_wbgraphql.get_wbgraphl(graphql_WB=graphql_WB,
                                                    endCursor=resp_queries['data']['workbooksConnection']['pageInfo'][
                                                        'endCursor'])
            resp_queries = server.metadata.query(wb_queries)
            wb_results = wb_results + resp_queries['data']['workbooksConnection']['nodes']
            get_wbgraphql.csv_data_wb(wb_results, site, config_details["json_wb"])
            # ds queries loaded
        ds_queries = get_dsgraphql.get_dsgraphl(graphql_DS=graphql_DS)
        resp_queries = server.metadata.query(ds_queries)
        print("total count of Datasources of {0} is {1}.".format(site,
                                                                 resp_queries['data']['publishedDatasourcesConnection'][
                                                                     'totalCount']))
        ds_results = resp_queries['data']['publishedDatasourcesConnection']['nodes']
        while resp_queries['data']['publishedDatasourcesConnection']['pageInfo']['hasNextPage']:
            ds_queries = get_dsgraphql.get_dsgraphl(graphql_DS=graphql_DS,
                                                    endCursor=
                                                    resp_queries['data']['publishedDatasourcesConnection']['pageInfo'][
                                                        'endCursor'])
            resp_queries = server.metadata.query(ds_queries)
            ds_results = ds_results + resp_queries['data']['publishedDatasourcesConnection']['nodes']
            get_dsgraphql.csv_data_ds(ds_results, site, config_details["json_ds"])

        # single site


def single_site(config_details=None, server=None, tableau_auth=None, graphql_queries=None, graphql_WB=None,
                graphql_DS=None):
    with server.auth.sign_in(tableau_auth):
        query_details(server=server, config_details=config_details, graphql_queries=graphql_queries,
                      graphql_WB=graphql_WB, graphql_DS=graphql_DS, site=config_details["tableau_site_id"])
        server.auth.sign_out()

    # allsites


def all_sites(config_details=None, server=None, tableau_auth=None, graphql_queries=None, graphql_WB=None,
              graphql_DS=None):
    with server.auth.sign_in(tableau_auth):
        sites = tsc.Pager(server.sites)
        for site in sites:
            server.auth.switch_site(site)
            # print(site.content_url)
            query_details(server=server, config_details=config_details, graphql_queries=graphql_queries,
                          graphql_WB=graphql_WB, graphql_DS=graphql_DS, site=site.content_url)
            server.auth.sign_out()


# main
def main(querytype=None, configurationfile=None, env=None):
    # get configuration file details
    config_details = get_config.get_config_by_environment(configuration=configurationfile, env=env)
    truncate_csv.truncatecsv(config_details)
    graphql_queries = config_details["graphql_queries"]
    graphql_WB = config_details["graphql_WB"]
    graphql_DS = config_details["graphql_DS"]
    tableau_auth = tsc.TableauAuth(username=config_details["tableau_user"], password=config_details["tableau_password"],
                                   site=config_details["tableau_site_id"])
    server = tsc.Server(server_address=config_details["tableau_server"], use_server_version=True)
    if querytype == 'singlesite':
        single_site(config_details=config_details, server=server, tableau_auth=tableau_auth,
                    graphql_queries=graphql_queries, graphql_WB=graphql_WB, graphql_DS=graphql_DS)
    elif querytype == 'allsites':
        all_sites(config_details=config_details, server=server, tableau_auth=tableau_auth,
                  graphql_queries=graphql_queries, graphql_WB=graphql_WB, graphql_DS=graphql_DS)


if __name__ == '__main__':
    main(querytype='singlesite',
         configurationfile='configuration.json',
         env='prod')
    print("Done")
