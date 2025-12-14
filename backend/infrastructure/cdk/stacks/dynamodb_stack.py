from aws_cdk import Stack
from aws_cdk import aws_dynamodb as dynamodb

class DynamoDBStack(Stack):
    def __init__(self, scope, id, **kwargs):
        super().__init__(scope, id, **kwargs)

        dynamodb.Table(
            self,
            "Memes",
            table_name="Memes",
            partition_key={"name": "PK", "type": dynamodb.AttributeType.STRING},
            sort_key={"name": "SK", "type": dynamodb.AttributeType.STRING},
            billing_mode=dynamodb.BillingMode.PAY_PER_REQUEST
        )