from operator import itemgetter
import boto3

# 1 Get the service resource.
dynamodb = boto3.resource("dynamodb")

table = dynamodb.Table("users")

print(table.creation_date_time)


# 2 putting an item
table.put_item(
    Item={
        "username": "janedoe",
        "first_name": "Jane",
        "last_name": "Doe",
        "age": 25,
        "account_type": "standard_user",
    }
)

# 3 getting an item

response = table.get_item(Key={"username": "janedoe", "last_name": "Doe"})
item = response["Item"]
print(item)

# 4 Updating an item
table.update_item(
    Key={"username": "janedoe", "last_name": "Doe"},
    UpdateExpression="SET age = :val1",
    ExpressionAttributeValues={":val1": 26},
)

# 4.1 now check if the item is updated or not
response = table.get_item(Key={"username": "janedoe", "last_name": "Doe"})
item = response["Item"]
print(item)

# 5 deleting an item
table.delete_item(Key={"username": "janedoe", "last_name": "Doe"})
