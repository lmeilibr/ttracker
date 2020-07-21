from ttracker.settings import ARENA_FOLDER
import os


def test_arena_folder():
    assert os.path.exists(ARENA_FOLDER)
