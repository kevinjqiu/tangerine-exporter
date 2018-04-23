import time
from prometheus_client import start_http_server, Gauge
from tangerine import InteractiveSecretProvider, TangerineClient


ACCOUNT_BALANCE = Gauge(
    'tangerine_account_balance', 'Tangerine Account Balance', [
        'currency_type',
        'account_description',
        'account_type',
        'nickname',
        'display_name',
    ]
)


def scrape_account_metrics(client, session):
    with session:
        while True:
            accounts = client.list_accounts()
            for account in accounts:
                ACCOUNT_BALANCE.labels(
                    currency_type=account['currency_type'],
                    account_description=account['description'],
                    account_type=account['type'],
                    nickname=account.get('nickname'),
                    display_name=account['display_name'],
                ).set(account['account_balance'])
        time.sleep(60)


def main():
    secret_provider = InteractiveSecretProvider()
    client = TangerineClient(secret_provider)

    start_http_server(8000)

    session = client.login()
    scrape_account_metrics(client, session)
