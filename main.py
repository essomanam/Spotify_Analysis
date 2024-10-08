from pipeline_utils import get_token, extract, transform, load

def main():
    # Step 1: Obtain access token
    token = get_token()

    # Step 2: Extract data from Spotify API
    extract()

    # Step 3: Transform the extracted data
    transform()

    # Step 4: Load the transformed data into MongoDB
    load()

if __name__ == "__main__":
    main()
