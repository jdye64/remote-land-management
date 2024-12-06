import logging
import json
from typing import List
from pydantic import BaseModel
from enum import Enum

logger = logging.getLogger(__name__)


class DimensionUnit(str, Enum):
    """Dimensional unit used for a measurement"""
    INCHES = "INCHES"
    FEET = "FEET"


class Dimension(BaseModel):
    """Represents physical dimensions"""
    x_width: int
    y_width: int
    unit: DimensionUnit

    def to_dict(self):
        return {"x_width": self.x_width, "y_width": self.y_width, "unit": self.unit}


class Asset(BaseModel):
    """Represents a physical asset that will need to be stored somewhere"""
    name: str
    dimension: Dimension

    def to_dict(self):
        return {"name": self.name, "dimension": self.dimension}


class AssetDB(BaseModel):
    """Abstraction that holds all of the Assets and metadata about them"""
    assets: List[Asset]

    def to_dict(self):
        return {
            'assets': self.assets,
        }

    @classmethod
    def from_dict(cls, dict_obj):
        return cls(dict_obj['assets'])

    def add_asset(self, asset: Asset):
        self.assets.append(asset)

    def save_assets(self, file_name):
        """Persist the localled referenced assets"""
        with open(file_name, 'w') as f:
            json.dump(self.to_dict(), f, indent=4)
