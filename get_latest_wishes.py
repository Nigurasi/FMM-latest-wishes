import csv
import datetime

WISHES_PATH = "fmm_latest_wishes/file.csv"

if __name__ == "__main__":
    current_date = datetime.date.today()
    day, month, year = (current_date.day, current_date.month-1, current_date.year) if current_date.month != 1 else (current_date.day, 12, current_date.year-1)
    date_month_ago = current_date.replace(day=1, month=month, year=year)

    reader = None
    latest_wishes = []

    print(f"Marzenia spełnione między {date_month_ago} i {current_date}".upper())
    with open(WISHES_PATH, newline='', encoding="utf8") as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            wish_date = datetime.datetime.strptime(row["date"], "%Y-%m-%d").date()
            if wish_date > date_month_ago:
                latest_wishes.append({
                    "url": row["url"],
                    "wish": row["wish"],
                    "child_details": row["child_details"],
                    "wish_date": wish_date
                    })

    latest_wishes.sort(key=lambda x: x["wish_date"])
    for l in latest_wishes:
        print(f"\t Spełnione dnia: {l['wish_date']}")
        print(f"\t Url: {l['url']}")
        print(f"\t Dziecko: {l['child_details']}")
        print(f"\t Wish: {l['wish']}")
        print()
