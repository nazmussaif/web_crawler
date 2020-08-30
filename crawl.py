from pywebcopy import Crawler, config


class Crawl:
    def crawl(self, project_name):
        kwargs = {
            'project_url': 'https://www.thedailystar.net/',
            'project_folder': 'thedailystar',
            'project_name': project_name,
            'bypass_robots': False,
            'load_css': False,
            'load_images': False,
            'load_javascript': False,
            'over_write': True
        }
        config.setup_config(**kwargs)

        wp = Crawler()
        wp.crawl()
