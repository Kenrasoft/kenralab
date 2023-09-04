import configparser


class Config:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Config, cls).__new__(cls)
            parser = configparser.ConfigParser()
            parser.read('core/config.conf')
            cls._instance.settings = parser

        return cls._instance

    def get_fmp_url(self):
        fmpapi_section = 'FMPAPI'
        uri = self.settings.get(fmpapi_section, 'uri')
        print(f'{fmpapi_section}: {uri}')
        return uri

    def get_pulsedb_host(self):
        pulsedb_section = 'PULSEDB'
        host = self.settings.get(pulsedb_section, 'host')
        print(f'{pulsedb_section}: {host}')
        return host


