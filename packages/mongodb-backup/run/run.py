from pymongo import MongoClient

def main(args):
  mongodb_url = os.environ['DATABASE_URL']
  client = MongoClient(mongodb_url)
  return {"body": client.list_databases()}
