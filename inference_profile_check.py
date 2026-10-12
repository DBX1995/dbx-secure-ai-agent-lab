import boto3

bedrock = boto3.client(
    "bedrock",
    region_name="us-east-1"
)

response = bedrock.list_inference_profiles(
    typeEquals="SYSTEM_DEFINED"
)

profiles = response["inferenceProfileSummaries"]

for profile in profiles:
    name = profile["inferenceProfileName"]

    if "Sonnet 4.6" in name:
        print(f"Name: {name}")
        print(f"ID: {profile['inferenceProfileId']}")
        print(f"Status: {profile['status']}")
        print()