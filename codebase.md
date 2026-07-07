# PyQt-PySide-Fluent-Widgets — Codebase Summary

> PySide6 desktop app boilerplate using [qfluentwidgets](https://qfluentwidgets.com/) (Microsoft Fluent Design).  
> Python 3.12+ · PySide6 · Fluent Design System

---

## Architecture Overview

```
main.py
 └── Window (FluentWindow) ─── navigation sidebar
       ├── HomeInterface (ScrollArea)
       │     └── BannerWidget ─── LinkCardView → LinkCard (×4)
       ├── TasksInterface (BlankWidget)
       ├── ContactsInterface (BlankWidget)
       ├── FolderInterface (BlankWidget)
       ├── Menu → Menu 1 → Menu 1.1 / Menu 2 (BlankWidget)
       └── SettingInterface (ScrollArea)
             └── SettingCardGroup (Personalization · Material · About)

Singletons: SignalBus · Config · StyleSheet enum
```

**Pattern**: Single-window app with a navigation sidebar (`FluentWindow`). Each nav item maps to a sub-interface (widget). Cross-component communication via `SignalBus`. Persisted config via `QConfig` + JSON. Dark/light theming via paired QSS files.

---

## Project Structure

```
.
├── main.py                       # Entry point — app init, DPI scaling, launches Window
├── pyproject.toml                # Project metadata & dependencies (uv/pip)
├── requirements.txt              # pip-compatible deps
├── uv.lock                       # uv lockfile
├── .python-version               # 3.12
├── .gitignore
├── README.md
├── codebase.md                   # this file
│
├── config/
│   └── config.json               # Persisted runtime config (theme, DPI, language, etc.) ignored coz autocreate by app
│
├── resource/
│   ├── img/
│   │   ├── icon.png              # App window icon
│   │   ├── header.png            # Banner image (unused?)
│   │   └── header1.png           # Banner image (used by BannerWidget)
│   └── styles/
│       ├── dark/                 # 8 × dark-theme QSS files
│       └── light/                # 8 × light-theme QSS files (mirror)
│
├── archive/                      # Empty — ignored by git
│
└── src/
    ├── __init__.py               # (not present — package root is implicit)
    │
    ├── common/
    │   ├── __init__.py
    │   ├── signal_bus.py         # SignalBus QObject — cross-component signals
    │   └── style_sheet.py        # StyleSheet enum — resolves QSS paths per theme
    │
    ├── components/
    │   ├── __init__.py
    │   ├── link_card.py          # LinkCard (clickable card) + LinkCardView (horizontal scroll)
    │   └── sample_card.py        # SampleCard (card widget) + SampleCardView (flow layout)
    │
    ├── config/
    │   ├── __init__.py
    │   └── config.py             # Config class + cfg singleton + constants (URLs, version)
    │
    ├── controllers/              # Empty — scaffolding
    ├── models/                   # Empty — scaffolding
    ├── utils/                    # Empty — scaffolding
    │
    └── views/
        ├── __init__.py
        ├── blank_widget.py       # BlankWidget — generic centered-label placeholder
        ├── home_window.py        # BannerWidget + HomeInterface (home page)
        ├── main_window.py        # Window (FluentWindow) — nav, badges, acrylic
        └── setting_interface.py  # SettingInterface — settings with card groups
```

---

## Modules

### Entry Point — `main.py`

Creates `QApplication`, applies DPI scaling from config, instantiates `Window`, shows it, runs event loop.

### Views

| File | Class(es) | Role |
|------|-----------|------|
| `main_window.py` | `Window(FluentWindow)` | Main window. Registers all sub-interfaces in nav. InfoBadge on Tasks (9) and Contacts (11). Acrylic navigation. 900×700. |
| `home_window.py` | `BannerWidget`, `HomeInterface` | Home page. Banner (336px) with gradient overlay + background image + 4 LinkCards (Getting started, GitHub, Code samples, Feedback). |
| `setting_interface.py` | `SettingInterface` | Settings page. Groups: Personalization (Mica, Theme, Color, Zoom, Language), Material (blur radius), About (Help, Feedback, About). |
| `blank_widget.py` | `BlankWidget` | Generic placeholder. Centered subtitle label. Used for Tasks, Contacts, Folder, Menu items. |

### Components

| File | Class(es) | Role |
|------|-----------|------|
| `link_card.py` | `LinkCard`, `LinkCardView` | Clickable link card (198×220) with icon/title/content. Opens URL on click. Horizontal scroll container. |
| `sample_card.py` | `SampleCard`, `SampleCardView` | Card (360×90) with icon/title/content. Emits `switchToSampleCard` on click. Flow-layout container. |

### Common

| File | Class(es) | Role |
|------|-----------|------|
| `signal_bus.py` | `SignalBus` | Singleton QObject with signals: `switchToSampleCard`, `micaEnableChanged`, `supportSignal`. |
| `style_sheet.py` | `StyleSheet` | Enum mapping component names to QSS file paths, resolved per theme. |

### Config

| File | Class(es) | Role |
|------|-----------|------|
| `config.py` | `Config`, `Language`, `LanguageSerializer` | `QConfig` subclass. Persisted settings: `micaEnabled`, `dpiScale`, `language`, `blurRadius`. Also exports constants: `YEAR`, `AUTHOR`, `VERSION`, URLs. |

---

## Configuration (`Config`)

Persisted to `config/config.json` via `qconfig.load()`. Fields:

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| `MainWindow.MicaEnabled` | bool | `isWin11()` | Mica backdrop effect |
| `MainWindow.DpiScale` | enum | `"Auto"` | UI zoom: 1, 1.25, 1.5, 1.75, 2, Auto |
| `MainWindow.Language` | enum | `AUTO` | UI language |
| `Material.AcrylicBlurRadius` | int (0–40) | 15 | Blur intensity |

Theme is forced to `Theme.DARK` at load.

---

## Theming

- **StyleSheet enum** resolves `./resource/styles/{theme}/{name}.qss`
- 16 QSS files (8 light + 8 dark), one per interface/component
- Theme switches at runtime via `qconfig.themeChanged` signal → `setTheme()`

---

## Signal Bus

Singleton `SignalBus` in `src/common/signal_bus.py`:

| Signal | Args | Purpose |
|--------|------|---------|
| `switchToSampleCard` | `str, int` | Navigate to a sample card by route key + index |
| `micaEnableChanged` | `bool` | Mica effect toggled |
| `supportSignal` | — | Support/coffee action |

---

## Dependencies (`pyproject.toml`)

| Package | Version | Purpose |
|---------|---------|---------|
| `pyside6` | ≥6.4.2 | Qt bindings |
| `pyside6-fluent-widgets[full]` | ≥1.11.2 | Fluent Design widgets |
| `pysidesix-frameless-window` | ≥0.8.0 | Frameless window support |
| `darkdetect` | ≥0.8.0 | OS theme detection |
| `pillow` | ≥12.3.0 | Image processing |
| `colorthief` | ≥0.2.1 | Color extraction |
| `scipy` | ≥1.18.0 | Scientific computing |
| `ruff` | ≥0.15.20 | Linter/formatter |

---

## Scaffolding

`src/controllers/`, `src/models/`, `src/utils/` exist as empty `__init__.py` stubs — ready for business logic, data models, and utility functions.

---

## Notes / Caveats

- `src/config/config.json` appears to be a stale duplicate of `config/config.json` with `ThemeMode: Light` vs the app's forced `Theme.DARK` — may cause confusion.
- `archive/` directory is empty and git-ignored.
- No test files exist yet.
- `BlankWidget` is used as a placeholder for 6 nav items — replace with real widgets.
- `SampleCard` emits `switchToSampleCard` but no slot connects to it yet.
