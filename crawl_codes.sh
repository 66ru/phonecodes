cd ./codeparser && \
scrapy crawl codes && \
scrapy crawl kzcodes && \
cd .. && \
mv ./codes.db ./codes-backup.db && \
mv ./codes-in-process.db ./codes.db
