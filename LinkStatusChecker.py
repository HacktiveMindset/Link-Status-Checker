import requests

def check_link_status(url):
    try:
        response = requests.head(url)
        if response.status_code == 200:
            return f"Live (Status Code: {response.status_code})"
        else:
            return f"Dead (Status Code: {response.status_code})"
    except requests.ConnectionError:
        return "Dead (Connection Error)"
    except requests.Timeout:
        return "Dead (Timeout Error)"
    except requests.RequestException:
        return "Dead (General Request Exception)"

def main():
    print("Link Checking Tool")
    while True:
        link = input("Enter the URL you want to check (or type 'exit' to quit): ")
        if link.lower() == 'exit':
            break
        status = check_link_status(link)
        print(f"Status for {link}: {status}\n")

if __name__ == "__main__":
    main()
