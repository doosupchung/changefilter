```markdown
# changefilter

A lightweight Python module for filtering out redundant time-series or streaming data.

## Features
- Keeps only entries whose `value` changes more than a given threshold.
- Useful for real-time plotting or logging where most values stay constant.
- Works with both lists and generators for large datasets.

## Installation
```bash
git clone https://github.com/doosupchung/changefilter.git
cd changefilter
pip install -e .

## Usage Example

You can run the module directly to test it:

```bash
python -m changefilter.core
```
## Result example
```bash
[
  {
    "param": "A",
    "time": 0.01,
    "value": 100.0
  },
  {
    "param": "A",
    "time": 0.03,
    "value": 100.6
  }
]
```