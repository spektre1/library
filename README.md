# The Third Library

* [GitHub Repo](https://github.com/spektre1/library)
* [License - AGPL 3](https://www.gnu.org/licenses/agpl-3.0.txt)

This is a technical proof of concept of a REST
API backend that manages licenses to books, and serves the books to users. This
is connected to a VR Chat world that acts as the user interface to this backend.

The world will function by providing the player an interface to the searchable
database of books. Books can be selected by a search term, keywords, categories,
and other collation methods.

## Install

Setup with `venv/` subdir in project.

TODO: Create an install script.


## Getting Started

This application is structured in a common pattern, using Flask with
Connexion, SQLAlchemy, and Alembic to keep the data models in sync as the system
grows in complexity. 

dependency-injector? YES

Connexion is for the public facing API,
flask blueprints and hardcoded endpoints is for Admin UI interface
