# Phishing Detector

## Overview

Phishing Detector is a web application designed to detect and analyze phishing attempts through email and URLs. The application leverages Flask for the web framework and integrates with AlienVault OTX to fetch known phishing domains. It also includes various validation and analysis techniques to identify suspicious emails and URLs.

## Project Structure

```sh

    .
    ├── .env
    ├── .gitignore
    ├── .idea/
    ├── alienvault_phishing_domains.json
    ├── app/
    │   ├── __init__.py
    │   ├── routes.py
    │   ├── static/
    │   ├── templates/
    │   └── __pycache__/
    ├── phishing_detector/
    │   ├── __init__.py
    │   ├── main.py
    │   ├── phishing_domain.py
    │   └── __pycache__/
    ├── Readme.md
    ├── requirements.txt
    └── run.py

```


## Features

- **Email and URL Analysis**: Analyzes emails and URLs for phishing indicators.
- **Phishing Domain Detection**: Fetches and checks against known phishing domains from AlienVault OTX.
- **Form Submission**: Handles form submissions and sends analyzed results via email.
- **Frontend**: Includes a frontend with various sections like Home, About, Skills, Projects, Research, CV, Publications, and Contact.

- **Portfolio Website**: Showcases web development techniques used to create a portfolio website for a friend.


## How It Works

1. **Email and URL Validation**: The application validates the format of emails and URLs using the `validators` library.
2. **Phishing Domain Check**: It checks if the email or URL domain is listed in the known phishing domains fetched from AlienVault OTX.
3. **Suspicious Character Detection**: It looks for suspicious characters in emails and URLs that are commonly used in phishing attempts.
4. **Disposable Email Detection**: It checks if the email is from a known disposable email provider.
5. **Form Handling**: The application handles form submissions from the contact form, analyzes the input, and sends the results via email.

## Cybersecurity Concepts Applied

- **Phishing Detection**: Implemented techniques to detect phishing attempts by analyzing email and URL patterns.
- **Domain Analysis**: Integrated with AlienVault OTX to fetch and use a list of known phishing domains.
- **Input Validation**: Ensured that all inputs (emails and URLs) are validated to prevent injection attacks.
- **Regular Expressions**: Used regex to identify and analyze patterns in emails and URLs.
- **Environment Variables**: Used environment variables to securely manage sensitive information like API keys and email credentials.

## Setup

1. **Clone the repository**:
    ```sh
    git clone <repository-url>
    cd <repository-directory>
    ```

2. **Create and activate a virtual environment**:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

4. **Set up environment variables**:
    Create a [.env](http://_vscodecontentref_/10) file in the root directory and add your environment variables:
    ```
    EMAIL_USER=your-email@example.com
    EMAIL_PASS=your-email-password
    my_apikey_OTX=your-alienvault-otx-api-key
    ```

5. **Run the application**:
    ```sh
    python run.py
    ```

6. **Access the application**:
    Open your browser and go to `http://127.0.0.1:5000/`.

## Usage

- Navigate to the contact form and submit an email and message.
- The application will analyze the input and send an email with the analysis results.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## License

MIT License

Copyright (c) 2025 Shubhrajit pallob.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.