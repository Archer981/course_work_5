from dataclasses import dataclass
from typing import List, Optional
from random import uniform
import marshmallow_dataclass
import marshmallow
import json


@dataclass
class Armor:
    id: int
    name: str
    defence: float
    stamina_per_turn: float


@dataclass
class Weapon:
    id: int
    name: str
    max_damage: float
    min_damage: float
    stamina_per_hit: float

    @property
    def damage(self) -> float:
        return round(uniform(self.min_damage, self.max_damage), 1)


@dataclass
class EquipmentData:
    # TODO содержит 2 списка - с оружием и с броней
    weapons: list[Weapon]
    armors: list[Armor]


class Equipment:

    def __init__(self):
        self.equipment = self._get_equipment_data()

    def get_weapon(self, weapon_name) -> Optional[Weapon]:
        # TODO возвращает объект оружия по имени
        for weapon in self.equipment.weapons:
            if weapon_name == weapon.name:
                return weapon
        return None

    def get_armor(self, armor_name) -> Optional[Armor]:
        # TODO возвращает объект брони по имени
        for armor in self.equipment.armors:
            if armor_name == armor.name:
                return armor
        return None

    def get_weapons_names(self) -> list:
        # TODO возвращаем список с оружием
        return [weapon.name for weapon in self.equipment.weapons]

    def get_armors_names(self) -> list:
        # TODO возвращаем список с броней
        return [armor.name for armor in self.equipment.armors]

    @staticmethod
    def _get_equipment_data() -> EquipmentData:
        # TODO этот метод загружает json в переменную EquipmentData
        with open("./data/equipment.json", encoding='utf-8') as equipment_data:
            data = json.load(equipment_data)
            equipment_schema = marshmallow_dataclass.class_schema(EquipmentData)
            try:
                return equipment_schema().load(data)
            except marshmallow.exceptions.ValidationError:
                raise ValueError
