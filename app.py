import os
import random
import time
import pandas as pd
from flask import Flask, request, render_template, redirect, url_for
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_emails', methods=['POST'])
def send_emails():
    # Get form data
    sender_email = request.form['sender_email']
    sender_password = request.form['sender_password']
    subject = request.form['subject']
    body = request.form['body']
    
    # Save uploaded files
    excel_file = request.files['excel_file']
    excel_filename = secure_filename(excel_file.filename)
    excel_filepath = os.path.join(app.config['UPLOAD_FOLDER'], excel_filename)
    excel_file.save(excel_filepath)
    
    resume_file = request.files['resume_file']
    resume_filename = secure_filename(resume_file.filename)
    resume_filepath = os.path.join(app.config['UPLOAD_FOLDER'], resume_filename)
    resume_file.save(resume_filepath)
    
    # Read the Excel file with email addresses
    df = pd.read_excel(excel_filepath)
    df['Email'] = df['Email'].astype(str).str.strip()
    df = df[df['Email'].str.contains('@') & ~df['Email'].isna()]
    
    # Email server configuration (for Gmail)
    smtp_server = 'smtp.gmail.com'
    smtp_port = 465
    
    # Establish a connection to the SMTP server
    server = smtplib.SMTP_SSL(smtp_server, smtp_port)
    server.login(sender_email, sender_password)
    
    cnt = 0
    # Iterate through the email addresses and send emails
    for index, row in df.iterrows():
        recipient_email = row['Email']
        cnt += 1

        # Compose the email message
        message = MIMEMultipart()
        message['From'] = sender_email
        message['To'] = recipient_email
        message['Subject'] = subject

        # Add the body of the email
        message.attach(MIMEText(body, 'html'))

        # Attach the resume file
        with open(resume_filepath, 'rb') as resume_file:
            resume_attachment = MIMEApplication(resume_file.read())
        resume_attachment.add_header('Content-Disposition', f'attachment; filename="{resume_filename}"')
        message.attach(resume_attachment)

        # Send the email
        try:
            server.sendmail(sender_email, recipient_email, message.as_string())
            print(f"Email sent to {recipient_email}")
        except Exception as e:
            print(f"Failed to send email to {recipient_email}: {e}")

    # Quit the SMTP server
    server.quit()
    
    return f"Total emails sent: {cnt}"

if __name__ == '__main__':
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    app.run(debug=True)