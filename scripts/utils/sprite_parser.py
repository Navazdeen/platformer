from pathlib import Path
import xml.etree.ElementTree as ET
from PIL import Image, ImageFile
from typing import List, Dict, Tuple, TypeVar

import re


T = TypeVar("T", bound="SpriteParser")


class TileSprite:
    def __init__(self, name: str, x: int, y: int, width: int, height: int, sprite_sheet: Image.Image):
        self.name = name
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.sprite_sheet = sprite_sheet

    def get_image(self) -> Image.Image:
        """Extracts the tile image from the sprite sheet."""
        return self.sprite_sheet.crop((self.x, self.y, self.x + self.width, self.y + self.height))

    def save(self, path: Path) -> None:
        """Saves the tile image to the specified path."""
        self.get_image().save(path.joinpath(self.name))


class SpriteParser:
    def __init__(self, sprite_sheet_path: str, xml_data: str) -> None:
        # Load the sprite sheet image
        self.sprite_sheet_path = sprite_sheet_path
        self.sprite_sheet = Image.open(sprite_sheet_path)
        self.sprite_collection: Dict[str, List[TileSprite]] = dict()

        # Parse the XML data
        self.parse_xml(xml_data)

    def _extract_name(self, name: str):
        """Split the name by the first capital letter"""
        return re.split(r"(?=[A-Z]|\.|_)", name)[0]

    def parse_xml(self, xml_data: str) -> None:
        """Parses the XML and creates TileSprite objects."""
        root = ET.fromstring(xml_data)
        for subtexture in root.findall('SubTexture'):
            name = subtexture.get('name')
            x = int(subtexture.get('x'))
            y = int(subtexture.get('y'))
            width = int(subtexture.get('width'))
            height = int(subtexture.get('height'))
            _sprite = TileSprite(name, x, y, width, height, self.sprite_sheet)
            self.sprite_collection.setdefault(
                self._extract_name(name), []).append(_sprite)

    def saveTiles(self, path: Path) -> None:
        """Saves the tile images to the specified path."""
        for name, tiles in self.sprite_collection.items():
            for tile in tiles:
                _path = path.joinpath(name)
                if not _path.exists():
                    _path.mkdir(parents=True)
                tile.save(_path)

    def genTemplate(self, path: Path) -> None:
        """Generates a collection sprite class for the tile with the tile as states."""
        for name, tiles in self.sprite_collection.items():
            _path = path.joinpath(f"{name}.py")
            if not _path.exists():
                _path.touch()
            with open(_path, "w") as f:
                f.write()


if __name__ == "__main__":
    _HERE = Path(__file__).parent
    # Example usage
    # Replace with the actual path to the sprite sheet image
    sprite_sheet_path = _HERE.joinpath(
        "../Assets/tiles/tiles_spritesheet.png").resolve()
    # Replace with your actual XML data
    xml_data_path = _HERE.joinpath(
        "../Assets/tiles/tiles_spritesheet.xml").resolve()
    with open(xml_data_path, "r") as xml_file:
        xml_data = xml_file.read()

    sprite_parser = SpriteParser(sprite_sheet_path, xml_data)
    sprite_parser.saveTiles(_HERE.joinpath(
        "../Assets/tiles/parsed/").resolve())
