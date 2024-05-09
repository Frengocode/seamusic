from src.beats.models import Beat, BeatPack, Playlist, License
from src.services import SQLAlchemyRepository
from src.config import settings


class BeatsRepository(SQLAlchemyRepository):
    model = Beat
    
class BeatPacksRepository(SQLAlchemyRepository):
    model = BeatPack

class PlaylistsRepository(SQLAlchemyRepository):
    model = Playlist
    
class LicensesRepository(SQLAlchemyRepository):
    model = License
    