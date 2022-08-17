import argparse
import csv
import os
import subprocess
import json
from os import access
from io import BytesIO

import pandas as pd
import requests
from click import command
from dagster import get_dagster_logger, job, op
from dotenv import load_dotenv
from minio import Minio
from minio.error import S3Error

from Downloader import download_tweets

minio_url = ""
minio_accessk = ""
minio_secretk = ""
minio_bucket_name = ""

start_date = ""
end_date = ""
lang_code = ""
topic = ""
category = ""

@op
def run_download_tweets():
    load_dotenv()
    result = download_tweets(
        start_date,
        end_date,
        lang_code,
        os.environ.get("BEARER_TOKEN"),
        topic,
        category,
    )
    return result
    
@op
def upload_minio(result):
    client = Minio(
        minio_url,
        access_key=minio_accessk,
        secret_key=minio_secretk,
    )

    found = client.bucket_exists(minio_bucket_name)
    if not found:
        client.make_bucket(minio_bucket_name)
    else:
        print("Bucket {} already exists".format(minio_bucket_name))

    df = pd.DataFrame(result)
    csv_bytes = df.to_csv().encode('utf-8')
    csv_buffer = BytesIO(csv_bytes)

    client.fput_object(
        minio_bucket_name, "twitter.json", data=csv_buffer,length=len(csv_bytes), content_type='application/csv',
    )

@job
def download_and_upload():
    output = run_download_tweets()
    upload_minio(output)

