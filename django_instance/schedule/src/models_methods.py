import abc
from datetime import datetime
from django_instance.settings import JS_TIME_FORMAT

class ModelsUtils():
    @classmethod
    @abc.abstractmethod
    def to_dict(self) -> dict[str]:
        ...

class ModelsWithTimeFIelds(ModelsUtils):
    def time_field_to_string(self, fieeld_key:str, TIME_FORMAT = JS_TIME_FORMAT):
        if self.__dict__[fieeld_key] is not None:
            return self.__dict__[fieeld_key].strftime(TIME_FORMAT)
        else:
            return None
        
    def convert_time_field_to_json(self,  TIME_FORMAT = JS_TIME_FORMAT):
        self_dict_to_json = self.to_dict()
        for key in self_dict_to_json:
            if "date" in key:
                self_dict_to_json[key] = self.time_field_to_string(key, TIME_FORMAT=TIME_FORMAT)
        
        return self_dict_to_json