from django.shortcuts import render, HttpResponse
import mysql.connector
import pandas as pd
import seaborn as sns

# Create your views here.

def index(request):
    return HttpResponse('Welcome!')

def create(request):
    return HttpResponse('Create')

def read(request,id):
    con = mysql.connector.connect(
        host = 'localhost', user='inab1822',
        password = 'neinei955', db='classicmodels',
        charset = 'utf8'
    )
    cur = con.cursor()
    sql = 'select customernumber, customername, city, country from customers;'
    cur.execute(sql)
    rows = cur.fetchall()
    con.close()
    customers = pd.DataFrame(rows)
    return HttpResponse(rows)