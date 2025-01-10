from flask import Blueprint, request, render_template
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
import re  # Import the re module for regular expressions
from phishing_detector import analyze_url, analyze_email

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/design')
def design():
    return render_template('design.html')

@main.route('/research1')
def research1():
    return render_template('research1.html')

@main.route('/research2')
def research2():
    return render_template('research2.html')

@main.route('/manufacturing')
def manufacturing():
    return render_template('manufacturing.html')

@main.route('/fsae')
def fsae():
    return render_template('fsae.html')

@main.route('/send_email', methods=['POST'])
def send_email():
    try:
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        # Analyze the email address
        email_analysis_result = analyze_email(email)

        # Analyze URLs in the email and message body
        email_urls = re.findall(r'http[s]?://[^\s]+', email)
        message_urls = re.findall(r'http[s]?://[^\s]+', message)
        all_urls = email_urls + message_urls
        analysis_results = [analyze_url(url) for url in all_urls]

        # Customize the message body based on analysis results
        safe_urls = []
        suspicious_urls = []
        for result in analysis_results:
            if "Safe" in result:
                safe_urls.append(result)
            else:
                suspicious_urls.append(result)

        # Email configuration
        sender_email = os.getenv('EMAIL_USER')
        receiver_email = os.getenv('EMAIL_USER')
        password = os.getenv('EMAIL_PASS')

        # Create the email content
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = f"New message from {name}"

        body = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}\n\n"

        # Add email analysis result
        body += f"Email Analysis:\n{email_analysis_result}\n\n"

        # Add URL analysis results
        if analysis_results:
            if suspicious_urls:
                body += "Suspicious URLs detected:\n" + "\n".join(suspicious_urls) + "\n\n"
            if safe_urls:
                body += "Safe URLs:\n" + "\n".join(safe_urls) + "\n\n"
        else:
            body += "No URLs found in the email or message.\n\n"

        msg.attach(MIMEText(body, 'plain'))

        try:
            # Connect to the server and send the email
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(sender_email, password)
            text = msg.as_string()
            server.sendmail(sender_email, receiver_email, text)
            server.quit()
            return 'Form submitted successfully!'
        except Exception as e:
            return str(e)
    except KeyError as e:
        return f"Missing form field: {e}", 400