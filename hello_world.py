from __future__ import print_function
from jinja2 import Environment
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

env = Environment(extensions=['jinja2.ext.i18n'])
env.install_gettext_translations(gnu_translations, newstyle=True)

template = env.from_string(
    """
    {% trans %}Jinja 2 is awesome{% endtrans %}
    {{ gettext('Gettext works') }}
    """
)
result = template.render()
print(result)
