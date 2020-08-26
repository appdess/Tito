#!/usr/bin/env python3

# sendTraces.py [request_duration] [home_address] [work_address]

import requests
import logging
import sys

logging.basicConfig(level=logging.INFO)

# get input values
requestDuration=float(sys.argv[1])
homeAddress=sys.argv[2]
workAddress=sys.argv[3]

payload = '\n'.join([
        '# TYPE tito_request_latency_seconds gauge',
        'tito_request_latency_seconds{homeAddress="%s",workAddress="%s"} %f' % (homeAddress, workAddress, requestDuration),
    ]) + '\n'

try:
    requests.post(
        'http://pushgateway-prometheus-pushgateway.default.svc.cluster.local:9091/metrics/job/tito',
        data=payload)
except IOError as e:
    logging.exception(f'Could not push request of {url}', e)