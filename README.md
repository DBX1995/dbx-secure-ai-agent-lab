# DBX Secure AI Agent Lab

A hands-on AWS AI security lab built with Python, boto3, Amazon Bedrock, and Anthropic Claude.

The project explores how an AI application can process untrusted documents, how indirect prompt-injection attacks can affect that workflow, and how application-level trust boundaries can improve resilience.

## Current Project Status

Completed so far:

- Python virtual environment and dependency isolation
- AWS authentication through the standard credential chain
- Amazon Bedrock model discovery
- Claude Sonnet 4.6 inference-profile discovery
- Live Bedrock Runtime invocation through boto3
- Synthetic opportunity-document analysis
- Controlled indirect prompt-injection testing
- Application-level system instructions for untrusted document handling
- Retesting against multiple prompt-injection scenarios
- Public Git version history documenting each milestone

## Architecture

```text
Synthetic document
      |
      v
Python application
      |
      v
boto3
      |
      v
Amazon Bedrock Runtime
      |
      v
US Claude Sonnet 4.6 inference profile
      |
      v
Model response