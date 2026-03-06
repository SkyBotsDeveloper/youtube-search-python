from inspect import signature

from youtubesearchpython import __version__
from youtubesearchpython import Hashtag, ResultMode
from youtubesearchpython.core.utils import get_cleaned_url


def test_package_version_is_exposed():
    assert isinstance(__version__, str)
    assert len(__version__) > 0


def test_hashtag_signature_legacy_call_order_supported():
    params = list(signature(Hashtag.get).parameters.keys())
    assert params[:3] == ["hashtag", "mode", "timeout"]
    assert ResultMode.dict.value == 1


def test_url_cleaner_keeps_video_id():
    cleaned = get_cleaned_url("https://youtu.be/dQw4w9WgXcQ?t=42")
    assert cleaned.endswith("v=dQw4w9WgXcQ")
