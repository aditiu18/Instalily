import requests
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

# Configs
CLAY_API_KEY = "your_clay_api_key"
CLAY_TABLE_ID = "your_table_id"
SENDGRID_API_KEY = "your_sendgrid_api_key"

# 1️⃣ Get Data from Clay
headers = {
    "Authorization": f"Bearer {CLAY_API_KEY}",
    "Content-Type": "application/json"
}

response = requests.get(
    f"https://api.clay.earth/v1/tables/{CLAY_TABLE_ID}/rows",
    headers=headers
)

data = response.json()
rows = data.get("rows", [])

# 2️⃣ Process Each Lead
for row in rows:
    name = row['fields'].get('Name', 'there')
    email = row['fields'].get('Email')
    company = row['fields'].get('Company', 'your company')
    title = row['fields'].get('Title', 'your team')

    if not email:
        continue  # Skip rows without email

    subject = f"Let's Connect, {name}"
    body = f"""
    Hi {name},

    I came across your work at {company} and was impressed by your role as {title}. 
    We'd love to explore potential synergies and see how we can collaborate.

    Let me know if you're open to a quick chat!

    Best regards,  
    Aditi Rani Uppari
    """

    # 3️⃣ Send Email via SendGrid
    message = Mail(
        from_email='your_email@example.com',
        to_emails=email,
        subject=subject,
        plain_text_content=body
    )
    try:
        sg = SendGridAPIClient(SENDGRID_API_KEY)
        response = sg.send(message)
        print(f"Email sent to {name} at {email}, Status: {response.status_code}")
    except Exception as e:
        print(f"Failed to send email to {email}: {e}")
