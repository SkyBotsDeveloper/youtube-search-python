# YouTube Search Python v2.0.1

<div align="center">

<p align="center">
  <img src="https://i.ibb.co/fGdbNGDs/photo-2026-03-06-21-34-16.jpg" alt="YouTube Search Python Banner" width="100%">
</p>

[![GitHub Stars](https://img.shields.io/github/stars/SkyBotsDeveloper/youtube-search-python?style=for-the-badge\&logo=github)](https://github.com/SkyBotsDeveloper/youtube-search-python/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/SkyBotsDeveloper/youtube-search-python?style=for-the-badge\&logo=github)](https://github.com/SkyBotsDeveloper/youtube-search-python/network)
[![Python Version](https://img.shields.io/badge/python-3.7+-blue.svg?style=for-the-badge\&logo=python\&logoColor=white)](https://www.python.org/downloads/)
[![License](https://img.shields.io/github/license/SkyBotsDeveloper/youtube-search-python?style=for-the-badge)](https://github.com/SkyBotsDeveloper/youtube-search-python/blob/main/LICENSE)
[![Latest Release](https://img.shields.io/github/v/release/SkyBotsDeveloper/youtube-search-python?style=for-the-badge)](https://github.com/SkyBotsDeveloper/youtube-search-python/releases)

**A lightweight Python library to search YouTube without using the official YouTube Data API.**

Search videos, channels, playlists, suggestions, comments, transcripts, and more with simple sync and async APIs.

[Features](#-features) • [Installation](#-installation) • [Quick Start](#-quick-start) • [Documentation](#-documentation) • [Examples](#-examples) • [Testing](#-testing)

</div>

---

## Features

* **No YouTube Data API key required** — search YouTube without official API keys or quota setup.
* **Sync and async support** — use the library in normal scripts or async apps.
* **Video, channel, and playlist search** — search multiple YouTube content types.
* **Rich metadata** — fetch video info, channels, playlists, comments, suggestions, recommendations, and transcripts.
* **Advanced filtering** — sort and filter by upload date, duration, relevance, views, and more.
* **Multi-region support** — use language and region preferences.
* **Stream helper utilities** — optional helpers for working with stream URLs.
* **Modern HTTP client** — built with modern `httpx` support.
* **Type hints** — improved developer experience with IDE autocomplete and type checking.
* **Docs and tests included** — examples and test files are available in the repository.

---

## Project Status

This project is actively maintained by [SkyBotsDeveloper](https://github.com/SkyBotsDeveloper).

The goal of this library is to make YouTube search integration easier for Python developers building bots, search tools, automation workflows, and apps.

> This project is not affiliated with YouTube or Google.

---

## Migration Note for Old Users

If you used the older `youtube-search-python` style imports and are migrating to this version, update future/async imports like this:

```python
# Old style
from youtubesearchpython.__future__ import VideosSearch

# New style
from youtubesearchpython.future import VideosSearch
```

---

## Installation

### Install directly from GitHub

```bash
pip install git+https://github.com/SkyBotsDeveloper/youtube-search-python.git
```

### Add to `requirements.txt`

```text
git+https://github.com/SkyBotsDeveloper/youtube-search-python.git
```

### Optional dependency for stream helpers

Some stream URL features may require `yt-dlp` to be installed:

```bash
pip install yt-dlp
```

---

## Quick Start

### Search for Videos

```python
from youtubesearchpython import VideosSearch

search = VideosSearch("NoCopyrightSounds", limit=10)
result = search.result()

print(result)
```

### Get Video Information

```python
from youtubesearchpython import Video

video = Video.get("https://www.youtube.com/watch?v=aqz-KE-bpKQ")

print(video["title"])
print(video["viewCount"])
```

### Async Usage

```python
import asyncio
from youtubesearchpython.future import VideosSearch, Video

async def main():
    search = VideosSearch("Python Tutorial", limit=5)
    result = await search.next()
    print(result)

    video = await Video.get("video_id_here")
    print(video)

asyncio.run(main())
```

---

## Documentation

### Core Documentation

* [API Reference](docs.md) — complete API documentation with classes and methods.
* [Usage Examples](docs/) — examples for search, video info, playlists, streams, and more.
* [Search Examples](docs/search_examples.md) — search classes and filters.
* [Video and Extras Examples](docs/extras_examples.md) — video, playlist, comments, and related features.
* [Stream URL Examples](docs/stream_examples.md) — stream URL helper usage.

---

## Key Classes

### Search Classes

* `VideosSearch` — search for videos.
* `ChannelsSearch` — search for channels.
* `PlaylistsSearch` — search for playlists.
* `CustomSearch` — search with custom filters.
* `ChannelSearch` — search inside a specific channel.

### Content Classes

* `Video` — get video information and formats.
* `Playlist` — get playlist information and videos.
* `Channel` — get channel information.
* `Comments` — get video comments.
* `Transcript` — get video transcripts or captions.
* `Suggestions` — get search suggestions.
* `Recommendations` — get video recommendations.
* `Hashtag` — get videos by hashtag.

### Utility Classes

* `StreamURLFetcher` — get stream URLs with supported formats.
* `ResultMode` — control output format such as `dict` or `json`.

---

## Examples

### Advanced Search with Filters

```python
from youtubesearchpython import CustomSearch, VideoSortOrder

search = CustomSearch("Python", VideoSortOrder.viewCount, limit=10)
print(search.result())
```

### Get Playlist Videos

```python
from youtubesearchpython import Playlist

playlist = Playlist.get("PLRBp0Fe2GpgmsW46rJyudVFlY6IYjFBIK")

print(f"Playlist: {playlist['title']}")
print(f"Videos: {len(playlist['videos'])}")
```

### Fetch Comments

```python
from youtubesearchpython import Comments

comments = Comments.get("https://www.youtube.com/watch?v=aqz-KE-bpKQ")

for comment in comments["result"][:5]:
    print(f"{comment['author']}: {comment['content']}")
```

### Get Search Suggestions

```python
from youtubesearchpython import Suggestions

suggestions = Suggestions.get("Arijit Singh", language="en", region="US")
print(suggestions["result"])
```

---

## Advanced Features

### Pagination

```python
from youtubesearchpython import VideosSearch

search = VideosSearch("Python", limit=10)

print(search.result())

search.next()
print(search.result())
```

### Language and Region

```python
from youtubesearchpython import VideosSearch

search = VideosSearch("Music", limit=10, language="es", region="ES")
print(search.result())
```

### Custom Filters

Available filter groups include:

* **Upload Date:** `VideoUploadDateFilter.lastHour`, `.today`, `.thisWeek`, `.thisMonth`, `.thisYear`
* **Duration:** `VideoDurationFilter.short`, `.long`
* **Sort Order:** `VideoSortOrder.relevance`, `.uploadDate`, `.viewCount`, `.rating`

---

## Testing

### Quick Test

```bash
cd tests
python3 full_execution.py
```

The test suite covers:

* Search classes such as videos, channels, playlists, and custom search.
* Content retrieval such as video, playlist, and channel details.
* Social features such as comments, recommendations, and suggestions.
* Advanced features such as stream helpers and transcripts.
* Both synchronous and asynchronous usage.

For more details, see [tests/README.md](tests/README.md).

---

## Contributing

Contributions are welcome.

You can help by:

* Reporting bugs
* Suggesting features
* Improving documentation
* Adding tests
* Fixing compatibility issues
* Improving reliability when YouTube changes its structure

Please read [CONTRIBUTING.md](CONTRIBUTING.md) before opening a pull request.

---

## Security

If you find a security issue, please do not open a public issue.

Read [SECURITY.md](SECURITY.md) for responsible reporting instructions.

---

## License

This project is licensed under the MIT License.

See the [LICENSE](LICENSE) file for more details.

---

## Disclaimer

This library is not affiliated with YouTube or Google.

It may use YouTube internal endpoints or publicly available web data that can change without notice. Features may break if YouTube changes its structure.

Use this library responsibly and follow YouTube's Terms of Service and content usage rules.

---

## Credits

* **Maintainer:** [SkyBotsDeveloper](https://github.com/SkyBotsDeveloper)
* **Telegram:** [@iflexelite](https://t.me/iflexelite)
* **forked from:** [Billaspace](https://github.com/BillaSpace/yt-search-python)
---

## Support the Project

If you find this library useful, please consider supporting it by giving the repository a star and fork on GitHub.

<div align="center">

**Made with ❤️ for the developer community**

[Report Bug](https://github.com/SkyBotsDeveloper/youtube-search-python/issues) • [Request Feature](https://github.com/SkyBotsDeveloper/youtube-search-python/issues)

</div>
