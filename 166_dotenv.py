import os

import dotenv

if __name__ == "__main__":
    # automatically loads .env in root:
    dotenv.load_dotenv()

    os.environ.get('ABC')

    # load from different location
    dotenv.load_dotenv('./data/.env', )
    os.environ.get('DATA')

    # what about existing settings?
    os.environ['ENVIRONMENT'] = 'PROD'
    dotenv.load_dotenv()
    assert os.environ.get('ENVIRONMENT') == 'PROD'
    # --> dotenv does not override per default

    dotenv.load_dotenv(override=True)
    assert os.environ.get('ENVIRONMENT') == 'DEV'
