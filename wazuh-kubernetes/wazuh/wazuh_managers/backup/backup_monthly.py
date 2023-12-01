#!/var/ossec/framework/python/bin/python3
import sys
import boto3
import glob
from datetime import datetime
from datetime import timedelta
from dateutil.relativedelta import relativedelta


a = datetime.today() + relativedelta(months=-1)
yesterday = a.strftime("%b/%d/%Y")
data = yesterday.split('/')

pwd = "/var/ossec/logs/alerts"
files = glob.glob(pwd + "/" + data[2]+ "/" + data[0] + "/*")

s3 = boto3.client("s3")
bucket = "wazuh-backup-prod"

try:
    for filename in files:
        s3.upload_file(
            Filename=filename,
            Bucket=bucket,
            Key="monthly/" + data[2] + "/" + data[0] + "/"+ filename.rsplit('/', 1)[1],
        )
except:
    json="{\"task\":\"backup_monthly\", \"result\":\"ERROR\", \"backup_date\":\"" + data[2]+ "/" + data[0] + "\", \"bucket\":\"" + bucket + "\"}"
    print(json)
    sys.exit()

json="{\"task\":\"backup_monthly\", \"result\":\"SUCCESS\", \"backup_date\":\"" + data[2]+ "/" + data[0] + "\", \"bucket\":\"" + bucket + "\"}"
print(json)
