import re


# get SQL tables
def sql_tables(sql_str):
    q = re.sub(r"/\*[^*]*\*+(?:[^*/][^*]*\*+)*/", "", sql_str)
    lines = [line for line in q.splitlines() if not re.match("^\s*(--|#)", line)]
    q = " ".join([re.split("--|//|#", line)[0] for line in lines])
    tokens = re.split(r"[\s)(;]+", q)
    result = set()
    get_next = False
    for tok in tokens:
        if get_next:
            if tok.lower() not in ["", "select"]:
                result.add(tok)
                get_next = False
                get_next = tok.lower() in ["from", "join"]
                return list(result)
