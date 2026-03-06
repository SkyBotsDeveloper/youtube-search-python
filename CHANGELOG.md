# Changelogs

All notable changes to this project will be documented in this file.

## [2.0.0] - 2026-01-18

### ðŸŽ‰ Major Refactoring Release

### Added
- âœ¨ **`future` module** - Clear naming for async operations
- ðŸ§ª **Comprehensive testing** - Tested with Indian & Myanmar songs
- ðŸ“š **Professional README** - Complete rewrite with extensive examples
- ðŸ“ **CHANGELOG** - Version tracking
- ðŸŒ **Regional examples** - Indian and Myanmar content examples
-  Channel , Playlist , Comments , Recommendations , Suggestions 

### Changed
- ðŸ“¦ **Module structure**: async operations now in `youtubesearchpython.future`
- ðŸ“ˆ **Version**: 1.6.6+master â†’ 2.0.0

### Fixed
- ðŸ› **Duplicate method**: Removed duplicate `__enhanceThumbnailsAsync` in video.py
- âš¡ **Async correctness**: Fixed async/sync inconsistencies
- ðŸ”— **Import paths**: Updated all module imports

### what i Tested personally
- âœ… Indian songs (Kesariya, Arijit Singh, T-Series)
- âœ… Myanmar songs (love songs, Burmese music)
- âœ… Video search (sync & async)
- âœ… Channel search
- âœ… Pagination
- âœ… Video metadata retrieval

---

## [2.0.0] - Current Release

### Added
- ðŸ“± ANDROID client as default
- âœ¨ Async Video methods
- ðŸ”„ Enhanced stream URL handling

### Changed
- ðŸ”¢ Updated Latest web client versions & parsing
- âš™ï¸ httpx 0.28+ compatibility

### Fixed
- Multiple bug fixes & code cleaned for rediabilty across modules

---

## Migration Guide

### To 2.0.0

**Async imports:**
```python
# Use this
from youtubesearchpython.future import VideosSearch

# Sync remains same  
from youtubesearchpython import VideosSearch
```

---

[2.0.0]: https://github.com/SkyBotsDeveloper/youtube-search-python/releases/tag/v2.0.0

