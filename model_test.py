import boto3

bedrock_runtime = boto3.client(
    "bedrock-runtime",
    region_name="us-east-1"
)

response = bedrock_runtime.converse(
    modelId="us.anthropic.claude-sonnet-4-6",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "text": "Reply with exactly: DBX Bedrock connection successful."
                }
            ]
        }
    ],
    inferenceConfig={
        "maxTokens": 30,
        "temperature": 0
    }
)

reply = response["output"]["message"]["content"][0]["text"]

print(reply)