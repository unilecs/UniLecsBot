from core.models import Puzzle
from config import PUZZLES_URL, PUZZLES_URL_VERSION, DATA_ACCESS_KEY

import requests
from requests.structures import CaseInsensitiveDict


headers = CaseInsensitiveDict()
headers["X-ACCESS-KEY"] = DATA_ACCESS_KEY


class PuzzleService:
    def __init__(self, data=None, version=None):
        self.data = data
        self.version = version

    def get_puzzle_data(self):
        if self.data is None or self.version != PUZZLES_URL_VERSION:
            response = requests.get(PUZZLES_URL, headers=headers)
            self.version = PUZZLES_URL_VERSION
            self.data = (
                response.json()["record"]
                if response and response.status_code == 200
                else None
            )
        return self.data

    def get_puzzles(self):
        puzzles_from_server = self.get_puzzle_data()["puzzles"]
        puzzle_list = []

        for puzzle in puzzles_from_server:
            puzzle_list.append(
                Puzzle(
                    puzzle.get("id", None),
                    puzzle.get("name", None),
                    puzzle.get("telegramLink", None),
                    puzzle.get("announcement", None),
                    puzzle.get("solution", None),
                    puzzle.get("tags", None),
                )
            )
        return puzzle_list
