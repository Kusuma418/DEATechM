#implement all the errors using exception handling
def all_errors():
    try:
        # TypeError example
        print("TypeError example:")
        x = "10" + 5  # This will raise TypeError

        # ValueError example
        print("ValueError example:")
        num = int("ten")  # Invalid literal

        # ZeroDivisionError example
        print("ZeroDivisionError example:")
        result = 10 / 0

        # IndexError example
        print("IndexError example:")
        lst = [1, 2, 3]
        print(lst[5])

        # KeyError example
        print("KeyError example:")
        d = {"a": 1}
        print(d["b"])

        # FileNotFoundError example
        print("FileNotFoundError example:")
        with open("non_existing_file.txt", "r") as f:
            content = f.read()

    except TypeError as te:
        print("Caught TypeError:", te)
    except ValueError as ve:
        print("Caught ValueError:", ve)
    except ZeroDivisionError as zde:
        print("Caught ZeroDivisionError:", zde)
    except IndexError as ie:
        print("Caught IndexError:", ie)
    except KeyError as ke:
        print("Caught KeyError:", ke)
    except FileNotFoundError as fe:
        print("Caught FileNotFoundError:", fe)
    except Exception as e:
        print("Caught a general exception:", e)
    finally:
        print("All exceptions handled. Program ended.")

all_errors()


#validate password
def validate_password(password):
    try:
        if type(password) != str:
            raise TypeError("Password must be a string")

        if len(password) < 8:
            raise ValueError("Password must be at least 8 characters long")

        has_upper = has_lower = has_digit = has_special = False
        special_chars = "!@#$%^&*()_+=-"

        for char in password:
            if char.isupper():
                has_upper = True
            elif char.islower():
                has_lower = True
            elif char.isdigit():
                has_digit = True
            elif char in special_chars:
                has_special = True

        if not has_upper:
            raise ValueError("Password must include at least one uppercase letter")
        if not has_lower:
            raise ValueError("Password must include at least one lowercase letter")
        if not has_digit:
            raise ValueError("Password must include at least one digit")
        if not has_special:
            raise ValueError("Password must include at least one special character")

        print("Password is valid")

    except TypeError as te:
        print("Type Error:", te)
    except ValueError as ve:
        print("Value Error:", ve)
    except Exception as e:
        print("Unexpected Error:", e)
    finally:
        print("Password validation complete.")

# Example usage
validate_password("Welcome123!")



#validate url
def validate_url(url):
    try:
        if type(url) != str:
            raise TypeError("URL must be a string")

        # Basic structure check
        if not (url.startswith("http://") or url.startswith("https://")):
            raise ValueError("URL must start with 'http://' or 'https://'")

        if "." not in url:
            raise ValueError("URL must contain at least one '.' symbol")

        if " " in url:
            raise ValueError("URL must not contain spaces")

        print("URL format is valid")

    except TypeError as te:
        print("Type Error:", te)
    except ValueError as ve:
        print("Value Error:", ve)
    except Exception as e:
        print("Unexpected Error:", e)
    finally:
        print("URL validation complete.")

# Example usage
validate_url("http://www.google.com/")
validate_url("invalid_url")