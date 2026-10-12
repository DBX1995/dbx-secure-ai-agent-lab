import boto3

bedrock = boto3.client(
    "bedrock",
    region_name="us-east-1"
)

response = bedrock.list_foundation_models()

models = response["modelSummaries"]

print(f"Bedrock returned {len(models)} foundation models.\n")

for model in models[:5]:
    print(f"- {model['providerName']}: {model['modelName']}")