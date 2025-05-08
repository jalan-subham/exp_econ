## Experimental Economics Group Project

## Experimental Design

We have 4 games with 2 control variables - Altruism and Income Reveal. This is direct copied from what was presented in class.


## Comments

The file [volunteer_dilemma_v4/__init__.py](volunteer_dilemma_v4/__init__.py) has been commented well. Other files are derived from this, so understanding this file should be enough.

Commenting the Jinja2 templates is not required because of its trivial nature.

### How to use?
Go to the website link (might take some time to load for the first time) and play a demo.
[Website](exp-econ.onrender.com)

Or, you can clone this repository (not recommended) and run 
+ `python3 -m venv .venv`
+ `pip install -r requirements.txt`
+ `source .venv/bin/activate`
+ `otree devserver`

Database is not persistent, so after doing some data collection, be sure to download the `.csv` right away!

### Folder Structure
- Don't touch any folders beginning with `_`.
- Don't delete `requirements.txt`.
- `archive/` contains some old versions of the game.
- All the main code files are in `volunteer_dilemma_v[4-7]`

### Admin Creds

If you feel the need to use these, you should contact me first.

```
username: admin
password: zendaya
```
