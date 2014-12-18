try:
    import ConfigParser
except:
    import configparser as ConfigParser
import os

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
    set_source_include_exts()
    set_source_dir(path)
    set_package_domain(domain)
    set_package_name(name)
    set_title(title)

def save_spec(path=None):
    if not path:
        path = config.get(SECTION_APP, 'source.dir')
    with open(path+'/buildozer.spec', 'w') as specfile:
        config.write(specfile)

def load_spec(path=None):
    if not path:
        path = '.'
    config.read(path+'/buildozer.spec')

def set_title(title='My Application'):
    config.set(SECTION_APP, 'title', title)

def get_title():
    try:
        return config.get(SECTION_APP, 'title')
    except:
        return ''

def set_package_name(package_name='myapp'):
    config.set(SECTION_APP, 'package.name', package_name)

def get_package_name():
    try:
        return config.get(SECTION_APP, 'package.name')
    except:
        return ''

def set_package_domain(package_domain='org.test'):
    config.set(SECTION_APP, 'package.domain', package_domain)

def get_package_domain():
    try:
        return config.get(SECTION_APP, 'package.domain')
    except:
        return ''

def set_source_dir(source_dir='.'):
    config.set(SECTION_APP, 'source.dir', source_dir)

def get_source_dir():
    try:
        return config.get(SECTION_APP, 'source.dir')
    except:
        return ''

def set_source_include_exts(exts=None):
    if exts is None:
        exts = 'py,png,jpg,kv,atlas'
    if exts == '':
        config.remove_option(SECTION_APP, 'source.include_exts')
    else:
        config.set(SECTION_APP, 'source.include_exts', exts)

def get_source_include_exts():
    try:
        exts = config.get(SECTION_APP, 'source.include_exts')
    except:
        exts = ''
    return exts

def set_source_exclude_exts(exts=None):
    if exts is None:
        exts = 'spec'
    if exts == '':
        config.remove_option(SECTION_APP, 'source.exclude_exts')
    else:
        config.set(SECTION_APP, 'source.exclude_exts', exts)

def get_source_exclude_exts():
    try:
        exts = config.get(SECTION_APP, 'source.exclude_exts')
    except:
        exts = ''
    return exts

def set_source_exclude_dirs(dirs=None):
    if dirs is None:
        dirs = 'tests,bin'
    if dirs == '':
        config.remove_option(SECTION_APP, 'source.exclude_dirs')
    else:
        config.set(SECTION_APP, 'source.exclude_dirs', dirs)

def get_source_exclude_dirs():
    try:
        dirs = config.get(SECTION_APP, 'source.exclude_dirs')
    except:
        dirs = ''
    return dirs

def set_source_exclude_patterns(patterns=None):
    if patterns is None:
        patterns = 'license,images/*/*.jpg'
    if patterns == '':
        config.remove_option(SECTION_APP, 'source.exclude_patterns')
    else:
        config.set(SECTION_APP, 'source.exclude_patterns', patterns)

def get_source_exclude_patterns():
    try:
        patterns = config.get(SECTION_APP, 'source.exclude_patterns')
    except:
        patterns = ''
    return patterns

def set_version_method_regex(regex='__version__ = [\'"](.*)[\'"]', filename='%(source.dir)s/main.py'):
    if regex == '':
        config.remove_option(SECTION_APP, 'version.regex')
        config.remove_option(SECTION_APP, 'version.filename')
    else:
        config.set(SECTION_APP, 'version.regex', regex)
        config.set(SECTION_APP, 'version.filename', filename)
        config.remove_option(SECTION_APP, 'version')

def get_version_method_regex():
    try:
        regex = config.get(SECTION_APP, 'version.regex')
        filename = config.get(SECTION_APP, 'version.filename')
    except:
        regex = '__version__ = [\'"](.*)[\'"]'
        filename = '%(source.dir)s/main.py'
    return (regex, filename)

def set_version_method_static(version='1.2.0'):
    if version == '':
        config.remove_option(SECTION_APP, 'version')
    else:
        config.set(SECTION_APP, 'version', version)
        config.remove_option(SECTION_APP, 'version.regex')
        config.remove_option(SECTION_APP, 'version.filename')

def get_version_method_static():
    try:
        return config.get(SECTION_APP, 'version')
    except:
        return ''

def set_requirements(requirements=None):
    if requirements is None:
        requirements = 'kivy'
    if requirements == '':
        config.remove_option(SECTION_APP, 'requirements')
    else:
        config.set(SECTION_APP, 'requirements', requirements)

def get_requirements():
    try:
        requirements = config.get(SECTION_APP, 'requirements')
    except:
        requirements = ''
    return requirements

def set_garden_requirements(requirements=None):
    if requirements is None:
        requirements = ''
    if requirements == '':
        config.remove_option(SECTION_APP, 'garden_requirements')
    else:
        config.set(SECTION_APP, 'garden_requirements', requirements)

def get_garden_requirements():
    try:
        requirements = config.get(SECTION_APP, 'garden_requirements')
    except:
        return ''
    return requirements

def set_presplash(filename='%(source.dir)s/data/presplash.png'):
    if filename == '':
        config.remove_option(SECTION_APP, 'presplash.filename')
    else:
        config.set(SECTION_APP, 'presplash.filename', filename)

def get_presplash():
    try:
        return config.get(SECTION_APP, 'presplash.filename')
    except:
        return ''

def set_icon_filename(filename='%(source.dir)s/data/icon.png'):
    if filename == '':
        config.remove_option(SECTION_APP, 'icon.filename')
    else:
        config.set(SECTION_APP, 'icon.filename', filename)

def get_icon_filename():
    try:
        return config.get(SECTION_APP, 'icon.filename')
    except:
        return ''

def set_orientation(orientation='all'):
    if orientation == '':
        config.remove_option(SECTION_APP, 'orientation')
    else:
        config.set(SECTION_APP, 'orientation', orientation)

def get_orientation():
    try:
        return config.get(SECTION_APP, 'orientation')
    except:
        return 'all'

def set_fullscreen(fullscreen=1):
    if fullscreen == '':
        config.remove_option(SECTION_APP, 'fullscreen')
    else:
        config.set(SECTION_APP, 'fullscreen', str(fullscreen))

def get_fullscreen():
    try:
        return config.get(SECTION_APP, 'fullscreen')
    except:
        return 0

def set_android_permissions(permissions=None):
    if permissions is None:
        permissions = ''
    if permissions == '':
        config.remove_option(SECTION_APP, 'android.permissions')
    else:
        config.set(SECTION_APP, 'android.permissions', permissions)

def get_android_permissions():
    try:
        permissions = config.get(SECTION_APP, 'android.permissions')
    except:
        permissions = ''
    return permissions

def set_android_api_level(level=14):
    if level == '':
        config.remove_option(SECTION_APP, 'android.api')
    else:
        config.set(SECTION_APP, 'android.api', str(level))

def get_android_api_level():
    try:
        return config.get(SECTION_APP, 'android.api')
    except:
        return ''

def set_android_min_api_level(level=8):
    if level == '':
        config.remove_option(SECTION_APP, 'android.minapi')
    else:
        config.set(SECTION_APP, 'android.minapi', str(level))

def get_android_min_api_level():
    try:
        return config.get(SECTION_APP, 'android.minapi')
    except:
        return ''

def set_android_sdk(version=21):
    if version == '':
        config.remove_option(SECTION_APP, 'android.sdk')
    else:
        config.set(SECTION_APP, 'android.sdk', str(version))

def get_android_sdk():
    try:
        return config.get(SECTION_APP, 'android.sdk')
    except:
        return ''

def set_android_ndk(version='9c'):
    if version == '':
        config.remove_option(SECTION_APP, 'android.ndk')
    else:
        config.set(SECTION_APP, 'android.ndk', version)

def get_android_ndk():
    try:
        return config.get(SECTION_APP, 'android.ndk')
    except:
        return ''

def set_android_use_private_storage(value=True):
    if value == '':
        config.remove_option(SECTION_APP, 'android.private_storage')
    else:
        config.set(SECTION_APP, 'android.private_storage', str(value))

def get_android_use_private_storage():
    try:
        return config.getboolean(SECTION_APP, 'android.private_storage')
    except:
        return ''

def set_android_ndk_path(path):
    if path == '':
        config.remove_option(SECTION_APP, 'android.ndk_path')
    else:
        config.set(SECTION_APP, 'android.ndk_path', path)

def get_android_ndk_path():
    try:
        return config.get(SECTION_APP, 'android.ndk_path')
    except:
        return ''

def set_android_sdk_path(path):
    if path == '':
        config.remove_option(SECTION_APP, 'android.sdk_path')
    else:
        config.set(SECTION_APP, 'android.sdk_path', path)

def get_android_sdk_path():
    try:
        return config.get(SECTION_APP, 'android.sdk_path')
    except:
        return ''

def set_android_p4a_path(path):
    if path == '':
        config.remove_option(SECTION_APP, 'android.p4a_dir')
    else:
        config.set(SECTION_APP, 'android.p4a_dir', path)

def get_android_p4a_path():
    try:
        return config.get(SECTION_APP, 'android.p4a_dir')
    except:
        return ''

def set_android_p4a_whitelist(whitelist=None):
    if whitelist is None:
        whitelist = ''
    if whitelist == '':
        config.remove_option(SECTION_APP, 'android.p4a_whitelist')
    else:
        config.set(SECTION_APP, 'android.p4a_whitelist', whitelist)

def get_android_p4a_whitelist():
    try:
        whitelist = config.get(SECTION_APP, 'android.p4a_whitelist')
    except:
        whitelist = ''
    return whitelist

def set_android_entrypoint(name='org.renpy.android.PythonActivity'):
    if name == '':
        config.remove_option(SECTION_APP, 'android.entrypoint')
    else:
        config.set(SECTION_APP, 'android.entrypoint', name)

def get_android_entrypoint():
    try:
        return config.get(SECTION_APP, 'android.entrypoint')
    except:
        return ''

def set_android_add_jars(names=None):
    if names is None:
        names = ''
    if names == '':
        config.remove_option(SECTION_APP, 'android.add_jars')
    else:
        config.set(SECTION_APP, 'android.add_jars', names)

def get_android_add_jars():
    try:
        jars = config.get(SECTION_APP, 'android.add_jars')
    except:
        jars = ''
    return jars

def set_android_add_src(names=None):
    if names is None:
        names = ''
    if names == '':
        config.remove_option(SECTION_APP, 'android.add_src')
    else:
        config.set(SECTION_APP, 'android.add_src', names)

def get_android_add_src():
    try:
        names = config.get(SECTION_APP, 'android.add_src')
    except:
        names = ''
    return names

def set_android_p4a_branch(branch='master'):
    if branch == '':
        config.remove_option(SECTION_APP, 'android.branch')
    else:
        config.set(SECTION_APP, 'android.branch', branch)

def get_android_p4a_branch():
    try:
        return config.get(SECTION_APP, 'android.branch')
    except:
        return ''

def set_android_ouya_category(category='GAME'):
    if category == '':
        config.remove_option(SECTION_APP, 'android.ouya.category')
    else:
        config.set(SECTION_APP, 'android.ouya.category', category)

def get_android_ouya_category():
    try:
        return config.get(SECTION_APP, 'android.ouya.category')
    except:
        return ''

def set_android_ouya_icon(path='%(source.dir)s/data/ouya_icon.png'):
    if path == '':
        config.remove_option(SECTION_APP, 'android.ouya.icon.filename')
    else:
        config.set(SECTION_APP, 'android.ouya.icon.filename', path)

def get_android_ouya_icon():
    try:
        return config.get(SECTION_APP, 'android.ouya.icon.filename')
    except:
        return ''

def set_android_manifest_intent_filters(path):
    if path == '':
        config.remove_option(SECTION_APP, 'android.manifest.intent_filters')
    else:
        config.set(SECTION_APP, 'android.manifest.intent_filters', path)

def get_android_manifest_intent_filters():
    try:
        return config.get(SECTION_APP, 'android.manifest.intent_filters')
    except:
        return ''

def set_android_add_libs_armeabi(libs=None):
    if libs is None:
        libs = 'libs/android/*.so'
    if libs == '':
        config.remove_option(SECTION_APP, 'android.add_libs_armeabi')
    else:
        config.set(SECTION_APP, 'android.add_libs_armeabi', libs)

def get_android_add_libs_armeabi():
    try:
        libs = config.get(SECTION_APP, 'android.add_libs_armeabi')
    except:
        libs = ''
    return libs

def set_android_add_libs_armeabi_v7a(libs=None):
    if libs is None:
        libs = 'libs/android-v7/*.so'
    if libs == '':
        config.remove_option(SECTION_APP, 'android.add_libs_armeabi_v7a')
    else:
        config.set(SECTION_APP, 'android.add_libs_armeabi_v7a', libs)

def get_android_add_libs_armeabi_v7a():
    try:
        libs = config.get(SECTION_APP, 'android.add_libs_armeabi_v7a')
    except:
        libs = ''
    return libs

def set_android_add_libs_x86(libs=None):
    if libs is None:
        libs = 'libs/android-x86/*.so'
    if libs == '':
        config.remove_option(SECTION_APP, 'android.add_libs_x86')
    else:
        config.set(SECTION_APP, 'android.add_libs_x86', libs)

def get_android_add_libs_x86():
    try:
        libs = config.get(SECTION_APP, 'android.add_libs_x86')
    except:
        libs = ''
    return libs

def set_android_add_libs_mips(libs=None):
    if libs is None:
        libs = 'libs/android-mips/*.so'
    if libs == '':
        config.remove_option(SECTION_APP, 'android.add_libs_mips')
    else:
        config.set(SECTION_APP, 'android.add_libs_mips', libs)

def get_android_add_libs_mips():
    try:
        libs = config.get(SECTION_APP, 'android.add_libs_mips')
    except:
        libs = ''
    return libs

def set_android_wakelock(value):
    if value == '':
        config.remove_option(SECTION_APP, 'android.wakelock')
    else:
        config.set(SECTION_APP, 'android.wakelock', str(value))

def get_android_wakelock():
    try:
        return config.get(SECTION_APP, 'android.wakelock')
    except:
        return ''

def set_android_meta_data(data=None):
    if data is None:
        data = ''
    if data == '':
        config.remove_option(SECTION_APP, 'android.meta_data')
    else:
        config.set(SECTION_APP, 'android.meta_data', data)

def get_android_meta_data():
    try:
        data = config.get(SECTION_APP, 'android.meta_data')
    except:
        data = ''
    return data

def set_android_library_references(references=None):
    if references is None:
        references = ''
    if references == '':
        config.remove_option(SECTION_APP, 'android.library_references')
    else:
        config.set(SECTION_APP, 'android.library_references', references)

def get_android_library_references():
    try:
        references = config.get(SECTION_APP, 'android.library_references')
    except:
        references = ''
    return references

def set_ios_codesign_debug(lastname, firstname, hexstring):
    if lastname == '' and firstname == '':
        config.remove_option(SECTION_APP, 'ios.codesign.debug')
    else:
        config.set(SECTION_APP, 'ios.codesign.debug', '"iPhone Developer: '+lastname+' '+firstname+' ('+hexstring+')"')

def get_ios_codesign_debug():
    try:
        codesign = config.get(SECTION_APP, 'ios.codesign.debug')
        #TODO think about a way to solve this. perhaps regex?
    except:
        return ''

def set_ios_codesign_release():
    config.set(SECTION_APP, 'ios.codesign.release', config.get(SECTION_APP, 'ios.codesign.debug'))

def get_ios_codesign_release():
    try:
        return get_ios_codesign_debug()
    except:
        return ''

def set_buildozer_log_level(value):
    if value == '':
        config.remove_option(SECTION_APP, 'log_level')
    else:
        config.set(SECTION_BUILDOZER, 'log_level', value)

def get_buildozer_log_level():
    try:
        return config.get(SECTION_BUILDOZER, 'log_level')
    except:
        return ''

def set_buildozer_warn_on_root(value):
    if value == '':
        config.remove_option(SECTION_APP, 'warn_on_root')
    else:
        config.set(SECTION_BUILDOZER, 'warn_on_root', value)

def get_buildozer_warn_on_root():
    try:
        return config.get(SECTION_BUILDOZER, 'warn_on_root')
    except:
        return ''
