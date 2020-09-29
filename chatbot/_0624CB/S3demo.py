# 目標: 上傳檔案到S3
#    創建客戶端
#    用客戶端上傳到S3的bucket


import boto3

#    創建客戶端
s3_client = boto3.client('s3',
                         aws_access_key_id="AKIAR4NDUH53GWDLQFNM",
                         aws_secret_access_key="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")

#    用客戶端上傳到S3的bucket
response = s3_client.upload_file("ngork_like_shit.txt",
                                 "iii-tutorial-v2",
                                 "student20/ngork_like_shit.txt")

print(response)