import os
import datetime
import crawl
import write_to_csv
import to_json
import clean_csv
import logger
import parse

if __name__ == '__main__':
    project_name = datetime.datetime.now().strftime("%d_%m_%Y")

    logger.write('Crawling start')
    web_crawler = crawl.Crawl()
    web_crawler.crawl(project_name)
    logger.write('Crawling end')

    csv_path = 'data.csv'
    to_csv = write_to_csv.ToCSV(csv_path)

    rootDir = 'thedailystar/' + project_name
    i = 0
    for current_folder, sub_folders, fileList in os.walk(rootDir):
        # Skip the folders that has bangla news
        if 'bangla' in current_folder:
            # print(current_folder)
            continue
        for file in fileList:
            if file.endswith('.html') and '__rss' not in file:
                full_path = os.path.join(current_folder, file)
                normalised_html_file_path = os.path.normpath(full_path)
                normalised_html_file_path = normalised_html_file_path.replace('\\', '/')

                data = parse.Parse(normalised_html_file_path).get_data()
                to_csv.add(data)
                # @todo add kafka
                to_json.get_json(data)

                i += 1
                print(i, normalised_html_file_path)

    logger.write(str(i) + ' article(s) parsed')
    clean_csv.CleanCSV(csv_path)
