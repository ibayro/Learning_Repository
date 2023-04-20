import base64
steps = ["plan", "code", "test", "delivery", "deploy", "monitor"]
for step in steps:
    step = bytes(step.encode())
    step = base64.b64encode(step)
    print(step)