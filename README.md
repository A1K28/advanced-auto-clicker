# Advanced Auto-Clicker

An Auto-Clicker with an ability to modify the **CPS** with a huge availability to be modded. 

E.g. the auto-clicking will stop when holding down space (aka when sprinting in game); the script has 2 simultaneous listeners: for keyboard and for controller (mouse)
and each can be modified from one-another; etc. 

To use it, install the requirements

```
pip install -r requirements.txt
```

then simply edit the global variables at the top of the script (if needed)

```python
maximum_time_on = 5
delay = 0.04
button = Button.left
start_stop_button = Button.x1
exit_button = Button.x2
```

and run it:
```
python auto-clicker.py
```

The possibilities are endless. Have fun!
