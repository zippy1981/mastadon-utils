import csv
from mastodon import Mastodon
from config import settings

# Read the CSV file
with open('following_accounts.csv', 'r') as f:
    reader = csv.DictReader(f)
    handles = [row['Account address'] for row in reader]

# Create a Mastodon API instance
mastodon = Mastodon(
#    client_id = 'your_client_key',
#    client_secret = 'your_client_secret',
    access_token = settings.MASTODON_API.KEY,
    api_base_url = f'https://{settings.MASTODON_API.SERVER or "mastadon.social"}'
)

# Get the display names
with open('output.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['Handle', 'Display Name', 'Profile Note'])

    for handle in handles:
        try:
            user = mastodon.account_lookup(handle)
            writer.writerow([handle, user['display_name'], user['note']])
            print(f"Handle: {handle}: {user['display_name']}")
        except IndexError:
            print(f"No user found for handle: {handle}")
