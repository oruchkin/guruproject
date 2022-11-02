from django.db.models.base import ModelBase

def get_object(object:ModelBase, pk:int) -> ModelBase:
    """
    Функция возвращает конкретный обьект класса который в нее 
    передают, либо поднимает ошибку, если обьекта не существует.
    """
    try:
        return object.objects.get(pk=pk)
    except object.DoesNotExist:
        return None
