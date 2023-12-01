#!/var/ossec/framework/python/bin/python3
import sys
import boto3
import glob
from datetime import datetime
from datetime import timedelta

a = datetime.today() - timedelta(days=1)
yesterday = a.strftime("%b/%d/%Y")
data = yesterday.split('/')

pwd = "/var/ossec/logs/alerts"
files = glob.glob(pwd + "/" + data[2]+ "/" + data[0] + "/ossec-alerts-" + data[1] + "*")
local_rules = glob.glob("/var/ossec/etc/rules/local*")

s3 = boto3.client("s3")
bucket = "wazuh-backup-prod"

try:
    #Alert Files
    for filename in files:
        s3.upload_file(
            Filename=filename,
            Bucket=bucket,
            Key="daily/" + data[2] + "/" + data[0] + "/" + data[1] + "/" + filename.rsplit('/', 1)[1],
        )
    #Local Rules   
    for rule in local_rules:
        s3.upload_file(
                Filename=rule,
                Bucket=bucket,
                Key="daily/" + data[2] + "/" + data[0] + "/" + data[1] + "/" + rule.rsplit('/', 1)[1],
            )
except:
    json="{\"task\":\"backup_daily\", \"result\":\"ERROR\", \"backup_date\":\"" + yesterday + "\", \"bucket\":\"" + bucket + "\"}"
    print(json)
    sys.exit()
    
json="{\"task\":\"backup_daily\", \"result\":\"SUCCESS\", \"backup_date\":\"" + yesterday + "\", \"bucket\":\"" + bucket + "\"}"
print(json)
