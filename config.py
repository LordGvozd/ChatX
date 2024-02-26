import os
from os.path import join
import dotenv

dotenv.load_dotenv()

ROOT_DIR = os.getenv("ROOT_DIR")
TEMPLATES_DIR_PATH = ROOT_DIR + "/templates"


