def what_to_do(instructions):
    if instructions.startswith("Simon says"):
        return ("I " + instructions.lstrip("Simon says")).strip()
    elif instructions.endswith("Simon says"):
        return ("I " + instructions.rstrip("Simon says")).strip()
    else:
        return "I won't do it!"
