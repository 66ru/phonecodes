cd ./codeparser && \
scrapy crawl codes && \
cd .. && \
mv ./codes.db ./codes-backup.db && \
mv ./codes-in-process.db ./codes.db
