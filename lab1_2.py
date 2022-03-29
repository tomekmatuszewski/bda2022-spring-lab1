import io
import json
import time

import boto3
import psutil
from datetime import datetime

start_time = time.time()

while True:
    # do work
    data = {'free_cpu': psutil.cpu_times_percent(interval=1.0, percpu=False).idle,
            'fee_mem': 100 - psutil.virtual_memory().percent}
    file_obj = io.BytesIO(json.dumps(data).encode('utf-8'))
    # upload file
    s3_client = boto3.client('s3')
    s3_client.upload_fileobj(file_obj, 'mardo-test-1234', datetime.now().strftime("%Y-%m-%dT%H:%M:%S") + '.json')
    print('Uploaded data to S3.')
    time.sleep(60)
    # time.sleep(60.0 - ((time.time() - start_time) % 60.0))

