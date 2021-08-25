# TermDecorator

## Overview

実行しようとしている関数の情報を表示し、単体テストのログを視覚的にわかりやすくするモジュール。

## Usage

```python
from termdecorator import termdecorate
import unittest

class testXXX(unittest.TestCase):
    
    @termdecorate
    def testMethod1(self):
        print("Testing...")

```

and run test:

```
--- START: testMethod1 (module: testXXX) ---
Testing...
--- finished ---
```

## LICENSE

All files of this repository is published under MIT License.
In details, see [LICENSE](LICENSE);
