```
       ___                          __      __    _ __             _                            
  ____/ (_)_____________  _________/ /     / /_  (_) /__________  (_)___        _________  _____
 / __  / / ___/ ___/ __ \/ ___/ __  /_____/ __ \/ / __/ ___/ __ \/ / __ \______/ ___/ __ \/ ___/
/ /_/ / (__  ) /__/ /_/ / /  / /_/ /_____/ /_/ / / /_/ /__/ /_/ / / / / /_____/ /  / /_/ / /__  
\__,_/_/____/\___/\____/_/   \__,_/     /_.___/_/\__/\___/\____/_/_/ /_/     /_/  / .___/\___/  
                                                                                 /_/            
```

# Prerequisites 
```
python 3.7+
pip
# bitcoind running
# discord server token
```

# Gettings Started 
```bash
# create virtual environment
$ python3 -m venv venv

# initialize virtual environment
$ source venv/bin/activate 

# install dependencies
$ pip install -r requirements.txt
```

# Settings

Remember modifying settings in your `settings.py`

```bash
$ mv settings.py.example settings.py
# then modify the file as you wish
```

# Run
```bash
python main.py
# then try typing !blockchaininfo in your discord channel
```
