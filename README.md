# tiobeindexpy


[![GitHub](https://img.shields.io/badge/license-MIT-brightgreen.svg)](https://raw.githubusercontent.com/amrs/tiobeindexpy/master/LICENSE.txt)
[![PyPI Downloads](https://img.shields.io/pypi/dm/tiobeindexpy.svg)](https://pypi.org/project/tiobeindexpy/)
[![PyPI](https://img.shields.io/pypi/v/tiobeindexpy.svg)](https://pypi.org/project/tiobeindexpy/)

A Python package to extract TIOBE Index (Programming Rankings)

### Dependencies

+ requests
+ beautifulsoup4
+ pandas

### Installation

```python
pip install tiobeindexpy
```

### Example

To extract Top 20 Programming Languges by TIOBE Index

```python
from tiobeindexpy import tiobeindexpy as tb
tb.top_20()
```

Courtesy: https://www.tiobe.com/tiobe-index/
