import os


def handler(event, context):
    print(event)
    for k, v in os.environ.items():
        print(f"{k}: {v}")
