from typing import Final

from dataclasses import dataclass

FACE_RANK_TO_VALUE: Final[dict[str, int]] = {
    "jack": 10,
    "queen": 10,
    "king": 10,
}

@dataclass(frozen=True, slots=True)
class Card:
    rank: str

    @property
    def values(self) -> tuple[int, int | None]:
        if self.rank == "ace":
            return (1, 11)

        if self.rank.isdigit():
            return (int(self.rank), None)

        return (FACE_RANK_TO_VALUE[self.rank], None)

    @property
    def rank_img_path(self) -> str:
        return f"assets/{self.rank}_card.png"

