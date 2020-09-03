import os
import datetime
import crawl
import add_to_csv
import clean_csv
import logger


if __name__ == '__main__':
    project_name = datetime.datetime.now().strftime("%d_%m_%Y")

    logger.write('Crawling start')
    web_crawler = crawl.Crawl()
    web_crawler.crawl(project_name)
    logger.write('Crawling end')

    csv_path = 'data.csv'
    to_csv = add_to_csv.ToCSV(csv_path)

    rootDir = 'thedailystar/' + project_name
    for current_folder, sub_folders, fileList in os.walk(rootDir):
        if 'bangla' in current_folder:
            # print(current_folder)
            continue
        for file in fileList:
            if file.endswith('.html') and '__rss' not in file:
                full_path = os.path.join(current_folder, file)
                normalised = os.path.normpath(full_path)
                normalised = normalised.replace('\\', '/')
                print(normalised)
                to_csv.add(normalised)
    logger.write('Data added')
    clean_csv.CleanCSV(csv_path)
