from dotenv import load_dotenv
import requests
import json
import os

load_dotenv()

xc_token = os.getenv("API_KEY")
base_name = os.getenv("BASE_NAME")
table_name = os.getenv("TABLE_NAME")

OUTPUT = "data/response.json"
URL = f"https://app.nocodb.com/api/v3/data/{base_name}/{table_name}/records"

HEADERS = {
    "accept": "application/json",
    "user-agent": "aksbdc/nocodb-to-gpt-via-api/0.2.2",
    "xc-token": xc_token,
}

PARAMETERS = {}


def project_description():
    """
    Example entrypoint for command-line interface (CLI).
    """
    print(">> Hello from nocodb-to-gpt-via-api!")
    print(">> This is a simple script that fetches data from an instance via the API.")
    print(">> The data is then used to train a GPT model.")


def fetch_data(location):
    """
    Retrieve data from the instance.
    """
    try:
        response = requests.request("GET", URL, headers=HEADERS, params=PARAMETERS)

        response.raise_for_status()

        data = response.json()

        os.makedirs(os.path.dirname(location), exist_ok=True)

        with open(location, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

        print(f">> Captured output: {location}")

    except requests.exceptions.RequestException as e:
        print(f"[!] Error w/ API request: {e}")

    except ValueError as e:
        print(f"[?] Error w/ JSON response parsing: {e}")

    except IOError as e:
        print(f"[*] Error w/ file write: {e}")


def main():
    project_description()
    fetch_data(OUTPUT)


if __name__ == "__main__":
    main()
