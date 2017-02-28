from __future__ import print_function
from jinja2 import Environment, FileSystemLoader
import locale
import gettext

domain = 'helloworld'

current_locale = 'en_US'  # replace with 'nb_NO' to show norwegian text
# current_locale, encoding = locale.getdefaultlocale()
print('Current locale: {}'.format(current_locale))

locale_path = 'locale/'
gnu_translations = gettext.translation(
    domain='helloworld',
    localedir=locale_path,
    languages=[current_locale]
)
gnu_translations.install()

print(_('helloworld'))

env = Environment(
    extensions=['jinja2.ext.i18n'],
    loader=FileSystemLoader('templates')
)
env.install_gettext_translations(gnu_translations, newstyle=True)

template = env.get_template('my_template.jinja2')
result = template.render()
print(result)
