# FMM-latest-wishes

## TODO:
- [ ] Fix gitignore
- [ ] fix Lukasz with div case https://www.mammarzenie.org/marzyciele/10054-%C5%81ukasz
- [ ] Obliczyć customowy przedział czasu
- [ ] Create batch file to run automatically

## How to run
```bash
cd fmm_latest_wishes
scrapy crawl FMM --nolog -o file.csv:csv
cd ..
python get_latest_wishes.py
```