from __future__ import print_function
import json
import hashlib
from virus_total_apis import PublicApi as VirusTotalPublicApi
import sklearn.ensemble as skensemble
import pefile 
import argparse
import hashlib
import array
import sys
import math
import csv
import urllib
API_KEY ='4c771b68534b80fafcaea4753dbe72ed88706e63f4df77335a72549d80014fdb'

def internet_on():
    try:
        urllib.request.urlopen('http://216.239.34.21', timeout=5)
        return True
    except urllib.error.URLError as err: 
        return False
def prelim(fname):
    #for signature based detection  
    print("Testing at VirusTotal")
    hash_md5 = hashlib.md5()
    with open(fname,"rb") as f:
        for chunk in iter(lambda: f.read(4096),b""):
            hash_md5.update(chunk)
    md5=hash_md5.hexdigest()        
   
    return md5
        

def virusTotalExtractor(fpath):

      
    x=internet_on()
    md5=prelim(fpath)
    

    EICAR_MD5 = md5
    if x:
        vt = VirusTotalPublicApi(API_KEY)
        response = vt.get_file_report(EICAR_MD5)
        jso=json.dumps(response, sort_keys=False, indent=4)
        pos=response["results"]["positives"]
        
        retu={"positives":pos,
              "connection":True
              }
        return retu
    else :
        print("Internet Connection Not Found")
        retu={"postitves":0,
              "connection":False
              }
        return retu
    
