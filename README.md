# minecraft Server Admin Tools 🛠️

[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue)](https://www.python.org/)
[![License: GPL-3.0 license](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://opensource.org/licenses/GPL-3.0)
[![Code style: Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

A powerful CLI tool for Minecraft server administrators, designed to simplify server management tasks with AI-powered features.

## Features ✨

### Core Functionalities
- **Configuration Translation** 🌐
  - Translate YAML, Properties, and TOML files using AI (Google/Hugging Face)
  - Preserve comments and structure during translation
  
- **Format Conversion** 🔄
  - Convert between JSON ↔ YAML ↔ TOML
  - Transform MiniMessage ↔ Bukkit Format ↔ Tellraw JSON

- **Configuration Validation** 🔎
  - Validate server.properties, spigot.yml, and other configuration files

- **Player Save Data Management** 📂
  - Manage player save data (playerdata, playerlist, etc.)

## Roadmap 🗺️

we are working on the following features:

- [ ] tests cases for all functions

- [ ] automated tests for all functions

- [ ] docker support, docker-compose support

- [ ] documentation.

## Installation 📦

is recommended to use a pipx for encapsulating the package in a virtual environment.

pipx:
```bash
pipx install git+https://github.com/DiegoRiveraR/minecraft-server-admin-tools.git
```

pip:
```bash
pip install git+https://github.com/DiegoRiveraR/minecraft-server-admin-tools.git
```

## Usage 🚀

 ```bash
python -m minecraft-server-admin-tools
```

## Tech Stack 💻

- Core: Python 3.10+

- CLI Framework: Fire

- AI Integration: Google Translate API, Hugging Face Transformers

- Database: SQLite for configuration tracking

- Code Quality: Ruff linting, pre-commit hooks

- CI/CD: GitHub Actions for automated testing


## Contributing 🤝

We welcome contributions! Please see our Contribution Guidelines and:

1. Fork the repository

2. Create your feature branch (git checkout -b feature/AmazingFeature)

3. Commit your changes (git commit -m 'Add some AmazingFeature')

4. Push to the branch (git push origin feature/AmazingFeature)

5. Open a Pull Request