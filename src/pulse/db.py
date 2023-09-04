from core.config import Config


class Repository:
    def load_data(self):

        conf = Config()
        print(conf.get_fmp_url())

        print(conf.get_pulsedb_host())
