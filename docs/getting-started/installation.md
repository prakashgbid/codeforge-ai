# Installation

## Requirements

- Python 3.8 or higher
- pip package manager

## Installation Methods

### From GitHub

```bash
pip install git+https://github.com/prakashgbid/osa-auto-coder.git
```

### From Source

```bash
git clone https://github.com/prakashgbid/osa-auto-coder.git
cd osa-auto-coder
pip install -e .
```

### Development Installation

```bash
git clone https://github.com/prakashgbid/osa-auto-coder.git
cd osa-auto-coder
pip install -e ".[dev]"
```

## Verify Installation

```python
import auto_coder
print(auto_coder.__version__)
```
