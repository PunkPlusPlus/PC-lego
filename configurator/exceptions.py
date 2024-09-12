class WrongComponentType(Exception):
    """
    Исключение выбрасывается, когда передается компонент не того типа.
    Например, если передать видеокарту в метод, который ждет процессор.
    """
    pass


class NotEnoughComponents(Exception):
    """
    Исключение выбрасывается если в сборке не хватает какого-то обязательного компонента
    """
    pass