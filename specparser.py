import ConfigParser
from mercurial.dispatch import request

config = ConfigParser.RawConfigParser()

SECTION_APP = 'app'
SECTION_BUILDOZER = 'buildozer'


def init_default_spec(path='.', orientation='landscape', domain='org.test', name='myapp', title='My Application'):
    config.add_section(SECTION_BUILDOZER)
    set_buildozer_warn_on_root(1)
    set_buildozer_log_level(1)
    config.add_section(SECTION_APP)
    set_fullscreen(1)
    set_orientation(orientation)
    set_requirements()
    set_version_method_regex()
    set_include_exts()
    set_source_dir(path)
    set_package_domain(domain)
    set_package_name(name)
    set_title(title)

def save_spec(path=None):
    if not path:
        path = config.get(SECTION_APP, 'source.dir')
    with open(path+'/buildozer.spec', 'rwb') as specfile:
        config.write(specfile)

def load_spec(path=None):
    if not path:
        path = '.'
    config.read(path+'/buildozer.spec')

def set_title(title='My Application'):
    config.set(SECTION_APP, 'title', title)

def get_title():
    return config.get(SECTION_APP, 'title')

def set_package_name(package_name='myapp'):
    config.set(SECTION_APP, 'package.name', package_name)

def get_package_name():
    return config.get(SECTION_APP, 'package.name')

def set_package_domain(package_domain='org.test'):
    config.set(SECTION_APP, 'package.domain', package_domain)

def get_package_domain():
    return config.get(SECTION_APP, 'package.domain')

def set_source_dir(source_dir='.'):
    config.set(SECTION_APP, 'source.dir', source_dir)

def get_source_dir():
    return config.get(SECTION_APP, 'source.dir')

def set_include_exts(exts=None):
    if exts is None:
        exts = ['py','png','jpg','kv','atlas']
    config.set(SECTION_APP, 'source.include_exts', ','.join(exts))

def get_include_exts():
    exts = config.get(SECTION_APP, 'source.include_exts')
    return ','.split(exts)

def set_source_exclude_exts(exts=None):
    if exts is None:
        exts = ['spec']
    config.set(SECTION_APP, 'source.exclude_exts', ','.join(exts))

def get_source_exclude_exts():
    exts = config.get(SECTION_APP, 'source.exclude_exts')
    return ','.split(exts)

def set_source_exclude_dirs(dirs=None):
    if dirs is None:
        dirs = ['tests', 'bin']
    config.set(SECTION_APP, 'source.exclude_dirs', ','.join(dirs))

def get_source_exclude_dirs():
    dirs = config.get(SECTION_APP, 'source.exclude_dirs')
    return ','.split(dirs)

def set_source_exclude_patterns(patterns=None):
    if patterns is None:
        patterns = ['license','images/*/*.jpg']
    config.set(SECTION_APP, 'source.exclude_patterns', ','.join(patterns))

def get_source_exclude_patterns():
    patterns = config.get(SECTION_APP, 'source.exclude_patterns')
    return ','.split(patterns)

def set_version_method_regex(regex='__version__ = [\'"](.*)[\'"]', filename='%(source.dir)s/main.py'):
    config.set(SECTION_APP, 'version.regex', regex)
    config.set(SECTION_APP, 'version.filename', filename)
    config.remove_option(SECTION_APP, 'version')

def get_version_method_regex():
    regex = config.get(SECTION_APP, 'version.regex')
    filename = config.get(SECTION_APP, 'version.filename')
    return (regex, filename)

def set_version_method_static(version='1.2.0'):
    config.set(SECTION_APP, 'version', version)
    config.remove_option(SECTION_APP, 'version.regex')
    config.remove_option(SECTION_APP, 'version.filename')

def get_version_method_static():
    return config.get(SECTION_APP, 'version')

def set_requirements(requirements=None):
    if requirements is None:
        requirements = ['kivy']
    config.set(SECTION_APP, 'requirements', ','.join(requirements))

def get_requirements():
    requirements = config.get(SECTION_APP, 'requirements')
    return ','.split(requirements)

def set_garden_requirements(requirements=None):
    if requirements is None:
        requirements = []
    config.set(SECTION_APP, 'garden_requirements', ','.join(requirements))

def get_garden_requirements():
    requirements = config.get(SECTION_APP, 'garden_requirements')
    return ','.split(requirements)

def set_presplash(filename='%(source.dir)s/data/presplash.png'):
    config.set(SECTION_APP, 'presplash.filename', filename)

def get_presplash():
    return config.get(SECTION_APP, 'presplash.filename')

def set_icon_filename(filename='%(source.dir)s/data/icon.png'):
    config.set(SECTION_APP, 'icon.filename', filename)

def get_icon_filename():
    return config.get(SECTION_APP, 'icon.filename')

def set_orientation(orientation='all'):
    config.set(SECTION_APP, 'orientation', orientation)

def get_orientation():
    return config.get(SECTION_APP, 'orientation')

def set_fullscreen(fullscreen=1):
    config.set(SECTION_APP, 'fullscreen', str(fullscreen))

def get_fullscreen():
    return config.getint(SECTION_APP, 'fullscreen')

def set_android_permissions(permissions=None):
    if permissions is None:
        permissions = []
    config.set(SECTION_APP, 'android.permissions', ','.join(permissions))

def get_android_permissions():
    permissions = config.get(SECTION_APP, 'android.permissions')
    return ','.split(permissions)

def set_android_api_level(level=14):
    config.set(SECTION_APP, 'android.api', str(level))

def get_android_api_level():
    return config.getint(SECTION_APP, 'android.api')

def set_android_min_api_level(level=8):
    config.set(SECTION_APP, 'android.minapi', str(level))

def get_android_min_api_level():
    return config.getint(SECTION_APP, 'android.minapi')

def set_android_sdk(version=21):
    config.set(SECTION_APP, 'android.sdk', str(version))

def get_android_sdk():
    return config.getint(SECTION_APP, 'android.sdk')

def set_android_ndk(version='9c'):
    config.set(SECTION_APP, 'android.ndk', version)

def get_android_ndk():
    return config.get(SECTION_APP, 'android.ndk')

def set_android_use_private_storage(value=True):
    config.set(SECTION_APP, 'android.private_storage', str(value))

def get_android_use_private_storage():
    return config.getboolean(SECTION_APP, 'android.private_storage')

def set_android_ndk_path(path):
    config.set(SECTION_APP, 'android.ndk_path', path)

def get_android_ndk_path():
    return config.get(SECTION_APP, 'android.ndk_path')

def set_android_sdk_path(path):
    config.set(SECTION_APP, 'android.sdk_path', path)

def get_android_sdk_path():
    return config.get(SECTION_APP, 'android.sdk_path')

def set_android_p4a_path(path):
    config.set(SECTION_APP, 'android.p4a_dir', path)

def get_android_p4a_path():
    return config.get(SECTION_APP, 'android.p4a_dir')

def set_android_p4a_whitelist(whitelist=None):
    if whitelist is None:
        whitelist = []
    config.set(SECTION_APP, 'android.p4a_whitelist', ','.join(whitelist))

def set_android_entrypoint(name='org.renpy.android.PythonActivity'):
    config.set(SECTION_APP, 'android.entrypoint', name)

def set_android_add_jars(names=None):
    if names is None:
        names = []
    config.set(SECTION_APP, 'android.add_jars', ','.join(names))

def set_android_add_src(names=None):
    if names is None:
        names = []
    config.set(SECTION_APP, 'android.add_src', ','.join(names))

def set_android_p4a_branch(branch='master'):
    config.set(SECTION_APP, 'android.branch', branch)

def set_android_ouya_category(category='GAME'):
    config.set(SECTION_APP, 'android.ouya.category', category)

def set_android_ouya_icon(path='%(source.dir)s/data/ouya_icon.png'):
    config.set(SECTION_APP, 'android.ouya.icon.filename', path)

def set_android_manifest_intent_filters(path):
    config.set(SECTION_APP, 'android.manifest.intent_filters', path)

def set_android_add_libs_armeabi(libs=None):
    if libs is None:
        libs = ['libs/android/*.so']
    config.set(SECTION_APP, 'android.add_libs_armeabi', libs)

def set_android_add_libs_armeabi_v7a(libs=None):
    if libs is None:
        libs = ['libs/android-v7/*.so']
    config.set(SECTION_APP, 'android.add_libs_armeabi_v7a', libs)

def set_android_add_libs_x86(libs=None):
    if libs is None:
        libs = ['libs/android-x86/*.so']
    config.set(SECTION_APP, 'android.add_libs_x86', libs)

def set_android_add_libs_mips(libs=None):
    if libs is None:
        libs = ['libs/android-mips/*.so']
    config.set(SECTION_APP, 'android.add_libs_mips', libs)

def set_android_wakelock(value):
    config.set(SECTION_APP, 'android.wakelock', str(value))

def set_android_meta_data(data=None):
    if data is None:
        data = []
    config.set(SECTION_APP, 'android.meta_data', ','.join(data))

def set_android_library_references(references=None):
    if references is None:
        references = []
    config.set(SECTION_APP, 'android.library_references', ','.join(references))

def set_ios_codesign_debug(lastname, firstname, hexstring):
    config.set(SECTION_APP, 'ios.codesign.debug', '"iPhone Developer: '+lastname+' '+firstname+' ('+hexstring+')"')

def set_ios_codesign_release():
    config.set(SECTION_APP, 'ios.codesign.release', config.get(SECTION_APP, 'ios.codesign.debug'))

def set_buildozer_log_level(value):
    config.set(SECTION_BUILDOZER, 'log_level', value)

def set_buildozer_warn_on_root(value):
    config.set(SECTION_BUILDOZER, 'warn_on_root', value)