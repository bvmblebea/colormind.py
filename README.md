# colormind.py
Web-API for [colormind.io](http://colormind.io/) website that uses deep learning to generate color schemes

## Example
```python
import colormind
colormind = colormind.ColorMind()
random_palette = colormind.get_random_color_palette()
print(random_palette)
```
