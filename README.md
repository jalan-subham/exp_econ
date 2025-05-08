## Experimental Economics Group Project

## Experimental Design

We have 4 games with 2 control variables - Altruism and Income Reveal. This is directly copied from what was presented in class.


## Comments

The file [volunteer_dilemma_v1/__init__.py](volunteer_dilemma_v4/__init__.py) has been commented well. Other files are derived from this, so understanding this file should be enough.

Commenting the Jinja2 templates is not required because of their trivial nature.

### How to use?
Go to the website link (might take some time to load for the first time) and play a demo. This runs in PRODUCTION mode with AUTHENTICATION. In the online version, the atabase is not persistent, so after doing some data collection, be sure to download the `.csv` right away!

[Website](https://exp-econ.onrender.com)

Or, you can clone this repository and run 
+ `python3 -m venv .venv`
+ `source .venv/bin/activate`
+ `pip install -r requirements.txt`
+ `otree devserver`

This runs in DEBUG mode without AUTHENTICATION.

## Running the Demo
We have currently set the Group Size to 3 (so you can test out the demo without having to open 5 tabs at once). In the presentation, we presented the group size being equal to 5. If you wish to make this change, modify `volunteer_dilemma_v[1-4]/__init__.py` and [settings.py](settings.py).

### Folder Structure
- Don't touch any folders beginning with `_`.
- Don't delete `requirements.txt`.
- `archive/` contains some old versions of the game.
- All the main code files are in `volunteer_dilemma_v[1-4]`

### Admin Creds

If you feel the need to use these, you should contact me first.

```
username: admin
password: zendaya
```
