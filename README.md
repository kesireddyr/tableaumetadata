# tableau metadata
# values in main
    1. querytype - singlesite, allsites
    2. env - based on configuration json, prod, uat or qa or local

You will not see queries for 
1. excel-direct connections 
2. textscan connections 
3. hyper connections 
4. extracts where connection cannot be established 
5. when data is live 
need to update the csv file to reflect teh changes and lookups 
we use python string literals https://docs.python.org/3/library/re.html

Write output files as csv in your folders