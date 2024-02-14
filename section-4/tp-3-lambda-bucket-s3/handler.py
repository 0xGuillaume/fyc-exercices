import boto3
import os

def lambda_handler(event, context):
    """Lambda handler to fecth a file stored in a s3 bucket."""
    
    # Nom du bucket S3 : Il doit être unique à tous les comptes AWS.
    bucket = ""

    # Chemin du fichier dans le bucket S3.
    file = "home/index.html"
    client = boto3.client("s3")

    try:
        # Récupérer le fichier du bucket S3
        file = client.get_object(Bucket=bucket, Key=file)
        file_content = file["Body"].read().decode("utf-8")

        return {
            "statusCode": 200,
            "headers": {"Content-Type": "text/html"},
            "body": file_content
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": str(e)
        }
