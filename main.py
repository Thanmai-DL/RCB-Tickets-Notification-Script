# Standard library imports
import time
import json
from datetime import datetime
from urllib import request

# Third party imports
from twilio.rest import Client

# User-defined constants
fixture_dates = ["2025-05-13", "2025-05-17"]  # List of fixture dates to check for ticket availability
recipient_contact_number = "+91123456789"  # Recipient's phone number for notifications
num_of_messages_to_send = 2  # Number of notification messages to send once tickets are available
interval_between_messages = 120  # Seconds between each notification message

# Twilio account details for sending SMS
account_sid = '123456789'  # Twilio account SID
auth_token = 'apikey1234abcdefghij0123456789'  # Twilio auth token
client = Client(account_sid, auth_token)  # Twilio client initialization
twilio_contact_number = "+123456789"  # Twilio phone number used for sending SMS

# RCB tickets booking page URL
rcb_ticketgenie_url = "https://rcbmpapi.ticketgenie.in/ticket/eventlist/0"
rcb_tickets_url = "https://shop.royalchallengers.com/ticket"

# Script execution control variables
sent_messages_count = 0  # Counter for messages sent
fetch_status_delay = 150  # Delay in seconds for script re-execution if tickets are not available


def getPage(url: str) -> request:
    """
    Fetches and returns the content of a webpage at a given URL.

    This function sends a GET request to the specified URL and returns the
    response object. It sets a custom User-Agent and other headers to simulate a
    browser request.

    Parameters:
    - url (str): The URL of the webpage to fetch.

    Returns:
    - request: A `urllib.request.urlopen` object containing the response from the
      webpage.
    """
    req = request.Request(
        url,
        headers={
        'authority': 'www.amazon.com',
        'pragma': 'no-cache',
        'cache-control': 'no-cache',
        'dnt': '1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'none',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-dest': 'document',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        }
    )
    return request.urlopen(req)

while fixture_dates:
    ticket_data = getPage(rcb_ticketgenie_url)
    ticket_data_content = ticket_data.read().decode('utf-8')  # Read the response content once
    ticket_data_json = json.loads(ticket_data_content)  # Parse the JSON once
    fixture_name = ticket_data_json['result'][-1].get('event_Name')   # Fetching the latest event name
    fixture_date = ticket_data_json['result'][-1].get('event_Date')   # Fetching the latest event date
    formatted_date = datetime.strptime(fixture_date, "%Y-%m-%dT%H:%M:%S").strftime("%Y-%m-%d")  # Formatting the date to "YYYY-MM-DD"

    if formatted_date == fixture_dates[0]:
        print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} Tickets available. Sending message...")
        tickets_available = True

        for message_num in range(num_of_messages_to_send):
            message = client.messages.create(
                from_=twilio_contact_number,
                body=f'The match tickets for {str(fixture_name)} on {str(formatted_date)} are available. Login to {rcb_tickets_url} to book the tickets immediately.',
                to=recipient_contact_number
            )
            print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} Message sent successfully - {message_num + 1} time(s)")
            sent_messages_count += 1

            if sent_messages_count == num_of_messages_to_send:
                fixture_dates.pop(0)  # Remove the first date from the list after sending the message
                break

            time.sleep(interval_between_messages)

    else:
        print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} Tickets not available for match on {str(fixture_dates[0])}. Retrying in {fetch_status_delay} seconds...")
        time.sleep(fetch_status_delay)