import json
import os
import re
import time
import uuid
from urllib import parse

import boto3
from botocore.client import Config
from botocore.exceptions import ClientError

# Allowlist of permitted file extensions
ALLOWED_EXTENSIONS = {'.jpg', '.jpeg', '.png', '.gif', '.pdf', '.txt'}

def lambda_handler(event, context):
    print(json.dumps(event))

    if "file" in event:
        s3 = boto3.client(
            's3',
            region_name=os.environ["AWS_REGION"],
            endpoint_url=f'https://s3.{os.environ["AWS_REGION"]}.amazonaws.com',
            config=Config(s3={'addressing_style': 'virtual'})
        )

        filename = event["file"]

        # FIX 1: Validate file extension before generating presigned URL
        ext = os.path.splitext(filename)[1].lower()
        if ext not in ALLOWED_EXTENSIONS:
            return json.dumps({"status": "err", "msg": "File type not permitted"})

        uuidv4 = str(uuid.uuid4())
        safe_key = uuidv4 + ext  # FIX 2: Use only UUID + extension, drop original name

        try:
            response = s3.generate_presigned_post(
                os.environ["FEEDBACK_BUCKET"],
                safe_key,
                ExpiresIn=120
            )
            print(response)
        except ClientError as e:
            print(str(e))
            return json.dumps({"status": "err", "msg": "could not get signed url"})

        return response

    elif "Records" in event:
        filename = parse.unquote_plus(event["Records"][0]["s3"]["object"]["key"])

        if not is_safe(filename):
            return {"status": "error", "message": "invalid filename"}

        # FIX 3: Never pass filename to shell — use Python's open() instead
        safe_tmp = "/tmp/" + re.sub(r'[^a-zA-Z0-9._-]', '_', filename)
        open(safe_tmp, 'w').close()           # replaces os.system touch
        open(safe_tmp + ".txt", 'w').close()

    else:
        return {"status": "ok", "message": "Thank you."}


def is_safe(s):
    # FIX 4: Uncomment and restore the actual security check
    if s.find(";") > -1 or s.find("'") > -1 or s.find("|") > -1:
        return False
    return True