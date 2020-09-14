import sys, os, pathlib

def good_sysinfo():
    print(f"User {os.environ.get('USER')}")
    print(f"PID {os.getpid()}")
    ver = sys.version.split('|')[0].strip()
    print(f"Python {ver}")
    
def good_configinfo():
    home = pathlib.Path('~').expanduser()
    configs = {}
    for fname in home.glob('.*'):
        if fname.is_file():
            info = os.stat(fname)
            size = info.st_size
            configs[fname.name] = size
    return configs
