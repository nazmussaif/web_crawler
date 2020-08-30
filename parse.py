from bs4 import BeautifulSoup


class Parse:

    def __init__(self, file_path):
        with open(file_path) as html:
            self.soup = BeautifulSoup(html, "lxml")

        self.file_path = file_path

        self.link = self.get_site_link()

        try:
            self.categories = ''
            for span in self.soup.find('div', class_='breadcrumb').find_all('span', itemprop="name"):
                if span.text != 'Home':
                    self.categories += (span.text + ', ')
            self.categories = self.categories[:-2]
        except:
            self.categories = None

        try:
            self.date_published = self.soup.find('meta', itemprop="datePublished").get('content')
        except:
            self.date_published = None

        try:
            self.date_modified = self.soup.find('meta', itemprop="dateModified").get('content')
        except:
            self.date_modified = None

        try:
            self.headline = self.soup.find('h1', itemprop="headline").text
        except:
            self.headline = None

        try:
            self.short_description = self.soup.find('meta', itemprop="description").get("content")
        except:
            self.short_description = None

        try:
            self.full_description = ''
            for p in self.soup.find('div', class_="field-body").find_all('p'):
                self.full_description += p.text
                self.full_description += '\n'
            self.full_description = self.full_description.strip()
        except:
            self.full_description = None

    def get_site_link(self):
        # link
        raw_link = str(self.file_path).split('/')
        file_name = raw_link[-1].split('_')[-1].split('.')[0]

        link = ''
        for i in raw_link[2:-1]:
            link += i + '/'
        link += file_name
        return link

    def get_data(self):
        return [self.link,
                self.categories,
                self.date_published,
                self.date_modified,
                self.headline,
                self.short_description,
                self.full_description
                ]

    def __str__(self):
        return (self.link + '\n' +
                self.categories + '\n' +
                self.date_published + '\n' +
                self.date_modified + '\n' +
                self.headline + '\n' +
                self.short_description + '\n' +
                self.full_description + '\n'
                )
