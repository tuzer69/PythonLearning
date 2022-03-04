class Data:
    """
    Класс для проверки конвертации и проверки даты на корректность
    """
    @classmethod
    def from_string(cls, data: str) -> str:
        if Data.is_date_valid(data):
            dt = data.split('-')
            return f'День: {dt[0]} Месяц: {dt[1]} Год: {dt[2]}'
        else:
            return 'Дата введена некорректно!'

    @classmethod
    def is_date_valid(cls, data: str) -> bool:
        dt = data.split('-')
        if (1 > int(dt[0]) or int(dt[0]) > 31) or (
                1 > int(dt[1]) or int(dt[1]) > 12) or (
                1900 > int(dt[2]) or int(dt[2]) > 2099):
            return False
        else:
            return True
