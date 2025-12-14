from .dynamo import dynamodb

MemesTable = dynamodb.Table("Memes")
FeedsTable = dynamodb.Table("Feeds")