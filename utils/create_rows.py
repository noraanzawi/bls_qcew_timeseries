import pandas
import requests
import urllib.request
import urllib

def qcew_CreateDataRows(csv):
    dataRows = []
    try: dataLines = csv.decode().split('\r\n')
    except er: dataLines = csv.split('\r\n');
    for row in dataLines:
        dataRows.append(row.split(','))
    return dataRows


def qcew_GetAreaData(year,qtr,area):
    urlPath = "http://data.bls.gov/cew/data/api/[YEAR]/[QTR]/area/[AREA].csv"
    urlPath = urlPath.replace("[YEAR]",year).replace("[QTR]",qtr.lower()).replace("[AREA]",area.upper())
    httpStream = urllib.request.urlopen(urlPath)
    csv = httpStream.read()
    httpStream.close()
    return qcew_CreateDataRows(csv)
