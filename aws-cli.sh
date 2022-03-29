#!/bin/sh
aws s3 mb s3://mardo-test-12345
aws s3api put-bucket-versioning --bucket mardo-test-12345 --versioning-configuration Status=Enabled

aws s3 cp test.txt s3://mardo-test-12345/hello.txt
aws s3 rm s3://mardo-test-12345/hello.txt