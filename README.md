# sample_web_scraper

Simple example of web scrapping Google search results and basic data archiving.

### Prerequisites

Python 3.5.3 and above

### Installing

To install use command line:

```
pip install git+https://github.com/FrancoJim/sample_web_scraper.git
```

### Examples of Usage

#### Obtaining U.S. Supreme Court Justices list and importing to CSV.
```
import scraper.supreme_court_to_disk as sc

url = 'https://www.supremecourt.gov/about/members_text.aspx'

# 'https://www.supremecourt.gov/about/members_text.aspx' is the default
html = sc.get_page(url=url)

# HTML Source code is downloaded and now reach for parsing.
# Parsing judges into a CSV compatible format.
judge_list = sc.parse_judges(html=html)

# Writing list of judges to CSV file.
# 'us_supreme_justices' is default name of CSV file. '.csv' extension is assumed.
# File path can be included in csv_file_path. i.e. /path/to/file or C:\path\to\file
sc.create_csv(data=judge_list, csv_file_path='us_supreme_justices')
```

## Built With

* [@{DEV_github_mention_name}](https://github.com/{DEV_github_mention_github_repository}) - {DEV_github_repository_name}

## Contributing

* [@FrancoJim](https://github.com/FrancoJim) (Kevin Lang)

## Authors

* **Kevin Lang** - *Initial work* - [@FrancoJim](https://github.com/FrancoJim)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

