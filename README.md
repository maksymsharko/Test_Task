# Clockify API

It is based on https://github.com/pieye/toggl2clockify and significant part of the code is just copied from there.
Credits to Markus Proeller, markus.proeller@pieye.org.

## Setup

* Create virtual env: `python -m venv venv` and activate it: `. ./venv/bin/activate `.
* Run PyCharm or other IDEs
* From GitHub Pull `main.py` file or download and Open this file.
* Open Terminal and Run commands: `pip install clockify-api-client`.
* Run : `python3 main.py`

## Configuration

- `Workspace` - Workspace in Clockify
- `Projects` - list of all projects
- `Current User` - Available user
- `Users` - list of all users
- `Tasks` - list of tasks

#### Example

```json
{
  "id": "635d4bdf183cb0136125a416", 
  "email": "maks.xxxxxx@gmail.com", 
  "name": "Xxxx Xxxxx", 
  "memberships": [], 
  "profilePicture": "https://img.clockify.me/no-user-image.png", 
  "activeWorkspace": "635d4bdf183cb0136125a417", 
  "defaultWorkspace": "635d4bdf183cb0136125a417", 
  "settings": {
    "weekStart": "MONDAY",
    "timeZone": "Europe/Kiev",
    "timeFormat": "HOUR24",
    "dateFormat": "DD/MM/YYYY"
  },
  ...
}

```
