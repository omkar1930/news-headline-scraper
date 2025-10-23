import requests
from bs4 import BeautifulSoup

def scrape_headlines():
    
    url = input("🔗 Enter the news website URL (e.g., https://www.bbc.com/news): ").strip()

    try:
        # Step 1:
        response = requests.get(url)
        response.raise_for_status()  

        # Step 2: 
        soup = BeautifulSoup(response.text, "html.parser")

        # Step 3: 
        headline_tags = soup.find_all(["h1", "h2", "h3"])  # common headline tags

        # Step 4: 
        with open("headlines.txt", "w", encoding="utf-8") as file:
            for i, tag in enumerate(headline_tags, start=1):
                text = tag.get_text(strip=True)
                if text:
                    file.write(f"{i}. {text}\n")

        print("\n✅ Headlines have been successfully saved to 'headlines.txt'!")

    except requests.exceptions.RequestException as e:
        print(f"❌ Error fetching the webpage: {e}")

# Run function.
if __name__ == "__main__":
    scrape_headlines()
