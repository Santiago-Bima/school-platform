from datetime import datetime

def date_validation(format):
    try:
        datetime.strptime(format, '%Y-%m-%d')
        return True
    except ValueError:
        return False
