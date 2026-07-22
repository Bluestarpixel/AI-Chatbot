import hashlib
import requests
from apscheduler.schedulers.blocking import BlockingScheduler

URL = "https://en.wikipedia.org/wiki/Artificial_intelligence"

last_hash = None

def get_hash(text):
    return hashlib.sha256(
        text.encode("utf-8")
    ).hexdigest()

def update_knowledge():
    global last_hash

    print("Checking for updates...")

    response = requests.get(
        URL,
        headers={"User-Agent": "Mozilla/5.0"}
    )

    text = response.text

    current_hash = get_hash(text)

    if last_hash is None:
        last_hash = current_hash
        print("Initial version stored")

    elif current_hash != last_hash:
        print("Website changed! Update database.")
        last_hash = current_hash

    else:
        print("No changes detected")

scheduler = BlockingScheduler()

scheduler.add_job(
    update_knowledge,
    "interval",
    minutes=1
)

print("Updater started...")

scheduler.start()