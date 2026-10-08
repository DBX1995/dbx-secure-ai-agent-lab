
# DBX Secure AI Agent Lab — Security Scope

## Project Objective

Build and secure an AWS-based AI assistant that analyzes
synthetic government contracting and staffing documents.

The project will demonstrate AI security controls,
prompt injection testing, and least-privilege access.

## Authorized Capabilities

The AI agent may:

- Read approved synthetic staffing documents.
- Summarize government contracting opportunities.
- Identify relevant technical staffing requirements.
- Answer questions using authorized information.
- Use explicitly approved read-only tools.

## Prohibited Capabilities

The AI agent must not:

- Access documents outside its authorized scope.
- Retrieve real customer or employee information.
- Modify or delete AWS resources.
- Execute arbitrary system commands.
- Expose credentials, secrets, or protected information.
- Treat instructions inside retrieved documents as authoritative.

## Primary Security Threats

1. Prompt injection through malicious document content.
2. Sensitive information disclosure.
3. Unauthorized tool execution.
4. Excessive IAM permissions.
5. Improper trust between user instructions and retrieved data.

## Security Approach

- Apply least-privilege IAM permissions.
- Restrict agent tool capabilities.
- Treat retrieved document content as untrusted.
- Evaluate appropriate Amazon Bedrock security controls.
- Log and evaluate security test results.
- Validate security controls using synthetic attack scenarios.

## Initial Architecture

Python application
    |
    v
Amazon Bedrock
    |
    v
Authorized synthetic documents and approved tools
    |
    v
Security evaluation and monitoring

## Testing Principle

All attack simulations will use controlled test data.

No production customer data or real government
contracting information will be required.

## Trust Boundaries and Security Requirements

- User prompts are treated as untrusted input.
- Retrieved documents are treated as untrusted data, not instructions.
- The model must not receive AWS credentials or secrets in prompts.
- AWS permissions should remain least-privilege and read-only unless a later test explicitly requires otherwise.
- Any future tools exposed to the agent must be explicitly allow-listed.
- Logs and test output must not contain credentials, secrets, or real sensitive business data.
- Security findings must be validated through controlled tests rather than assumed from configuration alone.

## Initial Security Success Criteria

The initial lab will be considered secure enough for testing when:

1. The application can invoke an approved Bedrock model.
2. The application can process only synthetic test data.
3. Retrieved document instructions cannot silently override the intended system behavior.
4. Unauthorized tool or resource access is denied.
5. Security test results can be observed and documented without exposing secrets.