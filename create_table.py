import boto3

# Get the service resource.
dynamodb = boto3.resource("dynamodb")


table = dynamodb.Table("users")


print(table.creation_date_time)
