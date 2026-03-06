"""
youtube-search-python v2 as yt-search-python (upgraded & enhanced)
Maintained by SkyBotsDeveloper with reliability and compatibility improvements.
"""

from youtubesearchpython.search import Search, VideosSearch, ChannelsSearch, PlaylistsSearch, CustomSearch, ChannelSearch
from youtubesearchpython.extras import Video, Playlist, Suggestions, Hashtag, Comments, Transcript, Channel
from youtubesearchpython.streamurlfetcher import StreamURLFetcher
from youtubesearchpython.core.constants import *
from youtubesearchpython.core.utils import *

__title__        = 'youtube-search-python'
__version__      = '2.0.0'
__author__       = 'SkyBotsDeveloper (@iflexelite)'
__license__      = 'MIT'

''' Deprecated. Present for legacy support. '''
from youtubesearchpython.legacy import SearchVideos, SearchPlaylists
from youtubesearchpython.legacy import SearchVideos as searchYoutube
