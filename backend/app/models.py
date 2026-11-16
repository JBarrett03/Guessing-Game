from sqlalchemy import Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from .database import Base

class Character(Base):

    __tablename__ = "one_piece_characters"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True
    )

    name: Mapped[str] = mapped_column(
        String(150),
        nullable=False
    )

    gender: Mapped[str | None] = mapped_column(
        String(20),
        nullable=True
    )

    devil_fruit: Mapped[str | None] = mapped_column(
        Text,
        nullable=True
    )

    devil_fruit_type: Mapped[str | None]= mapped_column(
        Text,
        nullable=True
    )

    haki: Mapped[str | None] = mapped_column(
        Text,
        nullable=True
    )

    first_appearance_arc: Mapped[str | None] = mapped_column(
        Text,
        nullable=True
    )

    affiliation: Mapped[str | None] = mapped_column(
        Text,
        nullable=True
    )
