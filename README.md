# Setup

```bash
[sudo] pip install -r requirements.txt
```

## Compile `po` files to `mo`

```bash
pybabel compile --domain=helloworld --directory=locale --use-fuzzy
```

# Run
```bash
python hello_world.py
```
