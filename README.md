# Setup

```bash
[sudo] pip install -r requirements.txt
```

## Compile `po` files

The `po` files (human readable) need to be compiled into machine readable `mo` files before gettext can use them

```bash
pybabel compile --domain=helloworld --directory=locale --use-fuzzy
```

# Run

```bash
python hello_world.py
```

# Workflow

When working on the application, you might want to add new messages. For example, add the following line to `templates/my_template.jinja2`:

```jinja2
{{ gettext('Yet another message') }}
```

Babel can automatically detect that this message was added. First we need to use the `extract` command to extract all localizable messages from the source files:

```bash
pybabel extract --mapping babel.cfg --output-file=locale/helloworld.pot .
```

Then update the *.po files so they contain the new localizable message:

```bash
pybabel update --domain=helloworld --input-file=locale/helloworld.pot --output-dir=locale
```

You can now see in the git diff for the *.po files where the new message was added, and you can hand-edit these files to localize the new message.

For example, open `locale/nb_NO/LC_MESSAGES/helloworld.po` and edit
```pot
#: templates/my_template.jinja2:3
msgid "Yet another message"
msgstr ""
```
to
```pot
#: templates/my_template.jinja2:3
msgid "Yet another message"
msgstr "Enda en melding"
```

[Poedit](https://poedit.net/) is a good editor for doing this. For example, it'll highlight missing translations and suggest translations, and you'll just have to press a keyboard shortcut to apply the suggestion.

## Command line aliases

Since the `pybabel` commands can be quite long, and you might want to use them frequently, it is recommended to add short aliases to these commands to save time
