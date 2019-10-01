# throttle.py
a python decorator for throttlling functions
## useage
```python
import throttle
@throttle(1000) #seting up function
def get_mouse():
    return mouse.x, mouse.y
while True:
    get_mouse() #will only call get mouse every 1 secound
```
