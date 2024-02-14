import boto3


def lambda_handler(event, context):
    """Handler to update an item inside a DynamoDB table."""

    client = boto3.client('dynamodb')
    table = "fyc"

    # Retrieve the current count
    data = client.get_item(
        TableName=table,
        Key={
            "visiteurs": {
                "S": "compteur"
            }
        }
    )
    count = int(data["Item"]["v"]["S"])
    count += 1

    # Mise à jour du compteur dans la dynamoDB.
    client.update_item(
        TableName=table,
        Key={
            "visiteurs": {
                "S": "compteur"
            }
        },
        UpdateExpression="SET v = :val",
        ExpressionAttributeValues={
            ":val": {"S": str(count)}
        }
    )

    return {
        'statusCode': 200,
        'body': f"Vous avez eu {count} visiteurs!"
    }
