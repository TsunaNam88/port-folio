import re


def clean_phone_numbers(lista):
    """ "
    Clean contact data and make sure all numbers are consistent.

    Parameters:

    Telephone numbers (List): Telephone numbers with differents formats.

    Returns: a list of numbers formatted in a consistent manner. 10 numbers, no special characters or spaces.
    """
    clean_numbers = []
    for i in lista:
        clean = re.sub(r"[-+() ]", "", i)

        if len(clean) > 10:
            clean = clean[-10:]

        if len(clean) == 10 and clean.isdigit():
            clean_numbers.append(clean)
        else:
            print(f"{i} invalido")
    return clean_numbers


resultado = clean_phone_numbers(
    ["+1 (555) 123-4567", "555-123-4567", "1234567890", "+52 55 1234 5678"]
)
print(resultado)
