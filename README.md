📰 News Headline Scraper
🧠 Objective

Scrape top news headlines automatically from any public news website.

⚙️ Tools Used

Python
Requests
BeautifulSoup

🚀 How It Works

This project contains one main file:
news_scraper.py

Inside the code, there are comments from Step 1 to Step 4 explaining what each part does:

🧩 Code Breakdown

🪜 Step 1: Fetch HTML using requests

---The program takes a website URL from the user.
---It sends an HTTP request to that website using the requests library.
---If the website responds successfully, the HTML data is stored for processing.

🪜 Step 2: Parse the HTML using BeautifulSoup

---The HTML data is passed to BeautifulSoup, which helps read and navigate HTML structure easily.
---It allows the script to search for specific tags like <h1>, <h2>, and <h3> (common headline tags).

🪜 Step 3: Extract Headline Tags

---The program collects all text inside those headline tags.
---It removes unnecessary spaces and ensures clean, readable text.

🪜 Step 4: Save Headlines to a File

---All headlines are saved inside a text file named headlines.txt.
---Each headline is written with numbering for easy reading.

💡 Key Concepts

HTTP Requests → Getting webpage data from the internet

Web Scraping → Extracting useful information from web pages

HTML Parsing → Reading and analyzing webpage structure


📂 Output

A file named headlines.txt containing all extracted news headlines.

🏁 Outcome

Automate the process of collecting top news headlines from any public website using Python.