import os

import PyInstaller.__main__
import os

package_name = 'test2'
PyInstaller.__main__.run([
    '--name=%s' % package_name,
    '--windowed',
    '--add-data=%s' % os.path.join('img;img'),
    '--add-data=%s' % os.path.join('View/html/map.html;View/html'),
    '--icon=%s'% os.path.join('img','icon.ico'),
    os.path.join('about.py'),
])

# PyInstaller.__main__.run([
#     '--name=%s' % package_name,
#     '--onefile',
#     '--windowed',
#     '--add-binary=%s' % os.path.join('resource', 'path', '*.png'),
#     '--add-data=%s' % os.path.join('resource', 'path', '*.txt'),
#     '--icon=%s' % os.path.join('resource', 'path', 'icon.ico'),
#     os.path.join('my_package', '__main__.py'),
# ])