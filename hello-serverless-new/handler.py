import json

def hello(event, context):
    name = "Mundo"

    # Serverless local en Windows puede enviar el evento como string o dict
    if isinstance(event, dict):
        qs = event.get("queryStringParameters")
        if qs and "name" in qs:
            name = qs["name"]

    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps({
            "message": f"Hola {name} desde Serverless"
        })
    }
