iimport boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

# Replace with your own email addresses
SENDER = "test@example.com"
RECIPIENT = "test@example.com"

# If necessary, replace with your own region
AWS_REGION = "eu-central-1"

# The subject line for the email
SUBJECT = "Amazon SES Test (Python)"

# The email body for recipients with non-HTML email clients
BODY_TEXT = ("Amazon SES Test (Python)\r\n"
             "This email was sent with Amazon SES using the "
             "AWS SDK for Python (Boto)."
            )

# The HTML body of the email
BODY_HTML = """<html>
<head></head>
<body>
  <h1>Amazon SES Test (Python)</h1>
  <p>This email was sent with
    <a href='https://aws.amazon.com/ses/'>Amazon SES</a> using the
    <a href='https://boto3.amazonaws.com/v1/documentation/api/latest/index.html'>AWS SDK for Python (Boto)</a>.
  </p>
</body>
</html>
            """

# The character encoding for the email
CHARSET = "UTF-8"

# Create a new SES resource and specify a region
client = boto3.client('ses', region_name=AWS_REGION)

# Try to send the email
try:
    # Provide the contents of the email
    response = client.send_email(
        Destination={
            'ToAddresses': [
                RECIPIENT,
            ],
        },
        Message={
            'Body': {
                'Html': {
                    'Charset': CHARSET,
                    'Data': BODY_HTML,
                },
                'Text': {
                    'Charset': CHARSET,
                    'Data': BODY_TEXT,
                },
            },
            'Subject': {
                'Charset': CHARSET,
                'Data': SUBJECT,
            },
        },
        Source=SENDER,
    )
# Display an error if something goes wrong
except (NoCredentialsError, PartialCredentialsError) as e:
    print("Credentials not available or partial credentials provided. Error:", e)
except Exception as e:
    print("Error sending email. Error:", e)
else:
    print("Email sent! Message ID:"),
    print(response['MessageId'])
