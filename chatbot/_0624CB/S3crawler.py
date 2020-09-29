import requests
# res = requests.get("http://facemood.grtimed.com/")
#
# text_file = open("sample.html", "w", encoding="utf8")
# n = text_file.write(res.text)
# text_file.close()


import boto3
# s3_client = boto3.client('s3',
#                          aws_access_key_id="AKIAR4NDUH53GWDLQFNM",
#                          aws_secret_access_key="DHHfSg5PrBysKBzcNaEo2qTWYQksrhTFgPqwNKm7")
#
# #    用客戶端上傳到S3的bucket
# response = s3_client.upload_file("sample.html",
#                                  "iii-tutorial-v2",
#                                  "student20/sample.html")
#
# print(response)

s3_client = boto3.client('s3')
# 已透過 "awscli" 建立 access key id & secret access key

s3_client.download_file("iii-tutorial-v2",
                        "student20/sample.html",
                        "sampledownload.html")
