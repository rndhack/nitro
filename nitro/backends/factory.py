from nitro.libvmi import VMIOS, Libvmi
from nitro.backends.linux import LinuxBackend
from nitro.backends.windows import WindowsBackend

BACKENDS = {
    VMIOS.LINUX: LinuxBackend,
    VMIOS.WINDOWS: WindowsBackend
}

def BackendNotFoundError(Exception):
    pass

def get_backend(domain):
    """Return backend based on libvmi configuration. If analyze if False, returns a dummy backend that does not analyze system calls. Returns None if the backend is missing"""
    libvmi = Libvmi(domain.name())
    os_type = libvmi.get_ostype()
    try:
        return BACKENDS[os_type](domain, libvmi)
    except KeyError:
        raise BackendNotFoundError('Unable to find an appropritate backend for'
                                   'this OS: {}'.format(os_type))