from django.shortcuts import render
import os
# Create your views here.
from django.http import HttpResponse
import psycopg2 as py



from rest_framework.decorators import api_view
from rest_framework.response import Response
'''
	 conn = py.connect(host="localhost",
    database="gokul",
    user="postgres",
    password="pass")
    
	 '''



POSTGRESQL_ADDON_HOST=os.getenv('POSTGRESQL_ADDON_HOST')
POSTGRESQL_ADDON_DB=os.getenv('POSTGRESQL_ADDON_DB')
POSTGRESQL_ADDON_PASSWORD=os.getenv('POSTGRESQL_ADDON_PASSWORD')
POSTGRESQL_ADDON_USER=os.getenv('POSTGRESQL_ADDON_USER')

@api_view(['GET'])
def searchApi(request):
	print('inside searchapi')
	
	conn = py.connect(host=POSTGRESQL_ADDON_HOST,
	database=POSTGRESQL_ADDON_DB,
	user=POSTGRESQL_ADDON_USER,
	password=POSTGRESQL_ADDON_PASSWORD)  # which database ( gokul) to connect 
	print('got req and conn')

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
	
	print('query exec')
	try:
	    
		
	    records=cur.fetchall()
	    records={'branches':records}
	    print(records)
	    return Response(records)
	except Exception as e:
	    print(e)

@api_view(['GET'])
def autoCompleteApi(request):
	print('inside autoapi')
	conn = py.connect(host=POSTGRESQL_ADDON_HOST,
    	database=POSTGRESQL_ADDON_DB,
    	user=POSTGRESQL_ADDON_USER,
    	password=POSTGRESQL_ADDON_PASSWORD) #which database ( gokul) to connect 
	q=request.GET.get('q')
	limit=request.GET.get('limit')
	offset=request.GET.get('offset')
	print('got req')
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
