#!/usr/bin/env python
import boto3
import logging
logging.basicConfig(loglevel="INFO",format='%(asctime)s:%(message)s')
s3 = boto3.resource('s3')
for bucket in s3.buckets.all():
    print bucket.name
    print "---"
    for item in bucket.objects.all():
        print "\t%s" % item.key
