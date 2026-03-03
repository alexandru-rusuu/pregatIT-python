from datetime import datetime

if __name__ == "__main__":
    birth_date: str = input("birthdate dd/mm/yyyy: ")
    name: str = input("name: ")
    country: str = input("country: ")

    parts: list[str] = birth_date.replace('.', '/').split('/')
    is_valid_format: bool = len(parts) == 3 and all([p.isdigit() for p in parts])

    if not is_valid_format:
        print("birth date must be valid! (dd/mm/yyyy)\n")
    else:
        day, month, year = [int(p) for p in parts]
        if not (1 <= month <= 12) or not (1 <= day <= 31) or year < 1900:
            print("birth date must be valid! (day 1-31, month 1-12, year > 1900).\n")
        else:
            now: datetime = datetime.now()
            has_birthday_passed: bool = (now.month, now.day) >= (month, day)
            age: int = now.year - year if has_birthday_passed else now.year - year - 1

            legal_age: int = 18

            output_messages: list[str] = [
                f"* congratulations, {name}, you are old enough to {action} in {country}!\n"
                for action, limit in [("vote", legal_age), ("drive", legal_age)]
                if age >= limit
            ]

            if output_messages:
                [print(message) for message in output_messages]
            else:
                print(f"unfortunately, {name}, you are too young!")