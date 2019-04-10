import psycopg2
DBNAME = "news"

def get_result(query):
    connection = psycopg2.connect(dbname=DBNAME)
    cursor = connection.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    connection.close()
    return result

def show_result(result,query_num):
    if(query_num == 1 or query_num == 2):
        for i in range (len(result)):
            print('{0} - {1} views\n'.format(result[i][0],result[i][1]))
    else:
        for i in range (len(result)):
            print('{0} - {1}% errors'.format(result[i][0],result[i][1]))

request_1 = "What are the most popular three articles of all time?\n"

query_1 = "Select title,count(*) as views from articles \
           join log on articles.slug = substring(log.path,10) \
           group by articles.title order by views desc limit 3;"

request_2 = "Who are the most popular article authors of all time?\n"

query_2 = "Select authors.name,count(log.path) as views from authors \
           join articles on authors.id = articles.author \
           join log on articles.slug = substring(log.path,10) \
           group by authors.name order by views desc;"

request_3 = "On which days did more than 1% of requests lead to errors?\n"

query_3 = "select to_char(A.time,'Mon DD,YYYY'), round((A.requestfailed*100.00/B.requests),3) \
           as errors from failedlog A join requestlog B on A.time=B.time \
           where (A.requestfailed*100.00/B.requests)>1.00;"

print(request_1)
result = get_result(query_1)
show_result(result,1)

print(request_2)
result = get_result(query_2)
show_result(result,2)

print(request_3)
result = get_result(query_3)
show_result(result,3)
