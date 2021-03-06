from django.db import models
import json

class DictField(models.TextField):

    description = 'Класс, хранящий в себе одну и более записей объекта в виде списка'

    def __init__(self, *args, **kwargs):
        super(DictField, self).__init__(*args, **kwargs)

    def to_python(self, value):

        if not value:
            return dict()
        
        if isinstance(value, dict):
            return value

        return json.loads(value)

    def from_db_value(self, value, expression, connection):

        return self.to_python(value)

    def get_prep_value(self, value):

        if value is None:
            return None

        return json.dumps(value, ensure_ascii=False)

    def value_to_string(self, obj):
        value = self._get_val_from_obj(obj)
        return self.get_db_prep_value(value)

    
