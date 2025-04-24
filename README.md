# Calling AWS AI Services
Code samples to make API calls to different AWS AI Services

## Setup

*To call AWS Machine Learning APIs, you'll generally follow these steps:*

* Set up AWS Credentials: Configure your AWS credentials so your local machine can authenticate with AWS.
* Install AWS SDK: Install the AWS SDK for your chosen programming language (Java or Python).
* Write Code: Write code in your chosen language to interact with the specific AWS ML API you want to use.
* Run Code: Execute your code from VS Code.

## Set up AWS Credentials

Option1: AWS CLI (Recommended for most users)
- Install AWS CLI: Download and install the AWS Command Line Interface (CLI) from the official AWS website.
- Configure AWS CLI:
- Open your terminal or command prompt.

Run aws configure.
Enter your AWS Access Key ID, Secret Access Key, default region, and output format. You can create these keys in the IAM Management Console. Important: Handle your credentials securely. Do not embed them directly in your code.

Option 2: Environment Variables

Set the following environment variables on your system:
- AWS_ACCESS_KEY_ID
- AWS_SECRET_ACCESS_KEY
- AWS_REGION

## Python Setup
- Install Python
- Install Boto3 (pip install boto3)

### Note: If you are using Java, then install the JDK and setup your Maven project.


