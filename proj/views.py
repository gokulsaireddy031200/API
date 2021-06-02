from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import psycopg2 as py


from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def searchApi(request):
	conn = py.connect(host="localhost",
    database="gokul",
    user="postgres",
    password="pass")   # which database ( gokul) to connect 


	q=request.GET.get('q')
	q=q.upper()
	limit=request.GET.get('limit')
	offset=request.GET.get('offset')
	if(limit==None):
		limit='NULL'
	if(offset==None):
		offset=0
	cur=conn.cursor()
	
	query=  " select row_to_json(b.*) from bank_branches2 b WHERE (b.*)::text LIKE '%{}%' order by ifsc asc limit {} offset {}".format(q,limit,offset)  # query to the table

	cur.execute(query)
	records=cur.fetchall()
	records={'branches':records}
	return Response(records)

@api_view(['GET'])
def autoCompleteApi(request):

	conn = py.connect(host="localhost",
    database="gokul",
    user="postgres",
    password="pass")   # which database ( gokul) to connect 
	q=request.GET.get('q')
	limit=request.GET.get('limit')
	offset=request.GET.get('offset')
	if(limit==None):
		limit='NULL'
	if(offset==None):
		offset=0

	cur=conn.cursor()
	
	query="select row_to_json(bank_branches2) from bank_branches2 where branch like '%{}%' order by ifsc asc limit {} offset {} ";   # query to the table
	query=query.format(q,limit,offset)

	cur.execute(query)
	records=cur.fetchall()
	records={'branches':records}
	return Response(records)

def main(request):
	conn = py.connect(host="localhost",
    database="gokul",
    user="postgres",
    password="pass")   # which database ( gokul) to connect 



	cur=conn.cursor()
	'''
	query='select city from bank_branches limit 10'   # query to the table

	cur.execute(query)
	records=cur.fetchall()
	for i in records:
		print(i)
	'''
	if conn:
		cur.close()
		conn.close()
		print("PostgreSQL connection is closed")

	return HttpResponse('Main is executed !')