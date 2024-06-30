import requests
from bs4 import BeautifulSoup
import csv

urls = [
    "https://results.eci.gov.in/PcResultGenJune2024/index.htm",
    "https://results.eci.gov.in/AcResultGenJune2024/index.htm",
    "https://results.eci.gov.in/AcResultGenJune2024/partywiseresult-S01.htm",
    "https://results.eci.gov.in/AcResultGenJune2024/partywiseresult-S18.htm",
    "https://results.eci.gov.in/AcResultByeJune2024/index.htm",
    "https://results.eci.gov.in/AcResultGenJune2024/partywisewinresult-1745S01.htm",
    "https://results.eci.gov.in/AcResultGenJune2024/partywisewinresult-860S01.htm",
    "https://results.eci.gov.in/AcResultGenJune2024/partywisewinresult-1888S01.htm",
    "https://results.eci.gov.in/AcResultGenJune2024/partywisewinresult-1888S01.htm",
    "https://results.eci.gov.in/AcResultGenJune2024/partywisewinresult-369S01.htm",
    "https://results.eci.gov.in/AcResultGenJune2024/partywisewinresult-369S18.htm",
    "https://results.eci.gov.in/AcResultGenJune2024/partywisewinresult-350S18.htm",
    "https://results.eci.gov.in/AcResultGenJune2024/partywisewinresult-742S18.htm",
    "https://results.eci.gov.in/AcResultGenJune2024/partywisewinresult-547S18.htm",
    "https://results.eci.gov.in/AcResultGenJune2024/partywisewinresult-743S18.htm",
    "https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-369.htm",
    "https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-742.htm",
    "https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-1680.htm",
    "https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-140.htm",
    "https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-582.htm",
    "https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-1745.htm",
    "https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-805.htm",
    "https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-3369.htm",
    "https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-3620.htm"
]

data = []
for url in urls:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    tables = soup.find_all('table')
    for table in tables:
        rows = table.find_all('tr')
        for row in rows:
            cols = row.find_all('td')
            cols = [col.text.strip() for col in cols]
            data.append([col for col in cols if col])

with open('lok_sabha_election_results.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)