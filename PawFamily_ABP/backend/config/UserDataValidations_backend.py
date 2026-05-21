import re


def validate_email_only(data):
    """Valida únicamente que el campo email sea correcto."""
    errors = []
    email = data.get('email', '').strip()

    if not email:
        errors.append({"field": "email", "message": "El correo electrónico es obligatorio."})
    elif not re.match(email):
        errors.append({"field": "email", "message": "El formato del correo no es válido."})

    return errors