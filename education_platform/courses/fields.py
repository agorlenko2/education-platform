from typing import Any
from django.db import models
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Model


class OrderField(models.PositiveIntegerField):
    def __init__(self, for_fields=None, *args, **kwargs) -> None:
        self.for_fields = for_fields
        super().__init__(*args, **kwargs)

    def pre_save(self, model_instance: Model, add: bool) -> Any:
        if getattr(model_instance, self.attname) is None:
            try:
                queryset = self.model.objects.all()
                if self.for_fields:
                    query = {
                        field: getattr(model_instance, field) for field in (
                            self.for_fields
                        )
                    }
                    queryset = queryset.filter(**query)
                    value = queryset.latest(self.attname).order + 1
            except ObjectDoesNotExist:
                value = 0
            setattr(model_instance, self.attname, value)
            return value
        else:
            return super().pre_save(model_instance, add)
