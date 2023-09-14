import json


def get_config_by_environment(configuration=None, env=None):
    if configuration is None or env is None:
        raise Exception("Invalid configuration : {} or Invalid Environment : {}".format(configuration, env))
    with open(configuration, 'r') as configfile:
        config_details = json.load(configfile)
        # print(config_details)
        response = {"graphql_queries": config_details["graphql_queries"],
                    "graphql_WB": config_details["graphql_WB"], "graphql_DS": config_details["graphql_DS"],
                    "graphql_test": config_details["graphql_test"]}
        config_details[env].update(response)
        # print(config_details[env])
        if env not in config_details:
            raise Exception("Invalid configuration : {} or Invalid Environment : {}".format(config_details, env))
        return config_details[env]
