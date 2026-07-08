# PyQt-PySide-Fluent-Widgets

A **PySide6 desktop application boilerplate** using [qfluentwidgets](https://qfluentwidgets.com/) — Microsoft Fluent Design for Qt/PySide. Provides a structured project scaffold with navigation, settings, sample cards, and light/dark theming.

Python 3.12+ · PySide6 · Fluent Design System

---

> **Requires Python ≥ 3.12**

## Quick Start

### Using uv (recommended)

```bash
# Install deps & create venv
uv sync

# Run
uv run python -m main
```

### Using pip

```bash
# Create virtual environment
python3 -m venv .venv

# Activate
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run
python -m main
```

---

## Project Structure

```
├── main.py                          # Entry point — app init, DPI scaling, launches Window
├── pyproject.toml                   # Project metadata & dependencies
├── requirements.txt                 # pip-compatible deps
│
├── config/
│   └── config.json                  # Persisted runtime config (theme, DPI, language)
│
├── resource/
│   ├── img/                         # App icons & banner images
│   └── styles/
│       ├── dark/                    # Dark-theme QSS stylesheets
│       └── light/                   # Light-theme QSS stylesheets
│── tests/*                          # All Test use by pytest
│
└── src/
    ├── common/
    │   ├── signal_bus.py            # SignalBus — cross-component signals (singleton)
    │   └── style_sheet.py           # StyleSheet enum — resolves QSS paths per theme
    │
    ├── components/
    │   ├── link_card.py             # LinkCard + LinkCardView — clickable link cards
    │   └── sample_card.py           # SampleCard + SampleCardView — sample gallery cards
    │
    ├── config/
    │   └── config.py                # QConfig subclass + cfg singleton + constants
    │
    ├── controllers/                 # Business logic (scaffolding)
    ├── models/                      # Data models (scaffolding)
    ├── utils/                       # Utilities (scaffolding)
    │
    └── views/
        ├── blank_widget.py          # Generic centered-label placeholder
        ├── home_window.py           # Home page — banner with link cards
        ├── main_window.py           # Main FluentWindow with navigation sidebar
        └── setting_interface.py     # Settings — personalization, material, about
```

---

## Architecture

```
main.py → Window (FluentWindow) → navigation sidebar
                ├── Home          — Banner + LinkCards (getting started, GitHub, etc.)
                ├── Tasks         — placeholder
                ├── Contacts      — placeholder
                ├── Folder        — placeholder
                ├── Menu (nested) — placeholder pages
                └── Settings      — Mica, Theme, Color, Zoom, Language, About
```

- **`FluentWindow`** — sidebar navigation with acrylic effect, collapsible to icons
- **InfoBadge** — notification badges on Tasks (9) and Contacts (11)
- **Settings** — persisted via `QConfig` + JSON; supports restart-to-apply options
- **Theming** — dark/light mode with paired QSS files, auto-switch support
- **SignalBus** — singleton for decoupled cross-component communication
- **Scaffolding** — `controllers/`, `models/`, `utils/` ready for your logic

---

## Configuration

Persisted in `config/config.json` (auto-created if user modify at setting at application this is — gitignored, not tracked):

| Setting | Options | Default |
|---------|---------|---------|
| Mica effect | on/off | Windows 11+ |
| DPI scale | 100%–200%, Auto | Auto |
| Theme | Light, Dark, System | Dark |
| Language | ID, EN, Auto | Auto |
| Blur radius | 0–40 | 15 |

---

## Dependencies

| Package | Version | Use |
|---------|---------|-----|
| PySide6 | ≥6.4.2 | Qt bindings |
| pyside6-fluent-widgets[full] | ≥1.11.2 | Fluent Design widgets |
| frameless-window | ≥0.8.0 | Frameless window support |
| darkdetect | ≥0.8.0 | OS theme detection |
| Pillow | ≥12.3.0 | Image processing |
| colorthief | ≥0.2.1 | Color extraction |
| scipy | ≥1.18.0 | Scientific computing |
| ruff | ≥0.15.20 | Linter |

---

## Development

```bash
# Lint
ruff check src/

# Format
ruff format src/

# Testing 
uv run pytest tests/
```

---

## Resources

- [qfluentwidgets Documentation](https://qfluentwidgets.com/)
- [PyQt-Fluent-Widgets GitHub](https://github.com/zhiyiYo/PyQt-Fluent-Widgets)
- [Examples](https://github.com/zhiyiYo/PyQt-Fluent-Widgets/tree/PySide6/examples)
