# RCB Tickets Notification Script

This Python script automatically checks the availability of Royal Challengers Bangalore (RCB) match tickets for a upcoming fixture date and sends SMS notifications using Twilio when tickets become available.

## Features

- **Automated Checking**: Continuously checks the RCB ticket booking page for ticket availability on a upcoming fixture dates.
- **SMS Notifications**: Sends SMS notifications through Twilio API when tickets for the desired date are available.
- **Customizable**: Allows setting the number of SMS notifications and the interval between them.

## Prerequisites

Before running this script, you need to have Python installed on your machine along with the necessary Python packages, and a Twilio account set up for sending SMS messages.

### Required Python Packages

- `twilio`: For sending SMS notifications.
- `requests`: For making HTTP requests to fetch the webpage content.

You can install these packages using pip:

```bash
pip install twilio requests
```
or, use the requirements.txt file to install all the required packages at once:
```bash
pip install -r requirements.txt
```

### Setting Up Twilio

1. **Sign Up or Log In to Twilio**: Go to the [Twilio website](https://www.twilio.com/) and sign up for a new account or log in if you already have one.

2. **Get Twilio Credentials**: Navigate to the [Console Dashboard](https://www.twilio.com/console) to find your `Account SID` and `Auth Token`. These credentials are required for the script to send SMS messages.

3. **Purchase a Twilio Phone Number**: You need a Twilio phone number to send SMS messages. You can purchase one from the [Twilio Console](https://www.twilio.com/console/phone-numbers/incoming).

4. **Verify Your Phone Number**: If you're using a Twilio trial account, you need to verify your recipient's phone number in the Twilio Console under the [Verified Caller IDs section](https://www.twilio.com/console/phone-numbers/verified).

## Configuration

Before running the script, update the following variables in the script with your information:

- `recipient_contact_number`: The phone number (with country code) where you want to receive ticket availability notifications.
- `fixture_dates`: List of upcoming fixture dates you are interested in for purchasing tickets.
- `account_sid`: Your Twilio Account SID.
- `auth_token`: Your Twilio Auth Token.
- `twilio_contact_number`: Your Twilio phone number from which SMS notifications will be sent.

## Running the Script

To run the script, navigate to the script's directory in your terminal and execute the following command:

```bash
python main.py
```

If you want to run it in background, you can use the following command:

```bash
nohup python main.py &
```

## How It Works

The script continuously checks the specified RCB tickets booking page for the availability of tickets for the next upcoming fixture date. If tickets become available, it sends the configured number of SMS notifications to the specified phone number, with an interval between each message.