import os
from dotenv import load_dotenv
load_dotenv()
class Environment:
    # https://www.geeksforgeeks.org/how-to-create-and-use-env-files-in-python/
    def __init__(self):
        self.SESSIONID = os.getenv('USER_SESSION')
        self.USER_AGENT = os.getenv('USER_AGENT')