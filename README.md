# Leak Reporter

Leak Reporter is a Python script that checks a list of emails against the **Leak Lookup API** and generates a professional email report with the results. 

---

## Features

- Checks multiple emails for leaks using the Leak Lookup API.
- Handles API **rate limits** automatically (429 errors).
- Sends a **professional HTML email report** with color-coded results:
  - **Green** = safe / no leaks
  - **Red** = leaked / compromised
  - **Orange** = unknown
- Fully configurable via a **`.env` file**.

---

## Requirements

```bash
pip install requests python-dotenv
```

#### Setup

Clone the repository:
```
git clone https://github.com/yourusername/leak-check-bot.git
cd leak-check-bot
```

Create a .env file in the project root:

- USER=username
- PASS=password
- PORT=1025
- SENDER_EMAIL=example@yahoo.com
- RECEIVER_EMAIL=recipient@example.com
- API_KEY=your_api_key_here

Add the emails you want to check in emails.txt, one per line.

---

### Usage

python leak_check_bot.py

The script will query the Leak Lookup API for each email.
Results are formatted in an HTML email and sent to the configured recipient.

Each email subject includes a timestamp for easy tracking.

---

**Important Notes**

Leak Lookup API limit: You can only make 10 requests per day with your API key.

Sending more than 10 emails may result in 429 Too Many Requests.
The script includes automatic retry with backoff for 429 errors.

Keep your .env file secure and do not commit it to version control.

Customization
Change email styling, colors, or add more fields in build_html_payload() function.

Adjust retry delays in LeakLookup class if you encounter rate-limiting.

---

## License

This project is for educational and internal use only. Do not distribute your API key publicly.
