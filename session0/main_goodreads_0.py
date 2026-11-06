import csv

# https://docs.python.org/3/library/csv.html
def clean_goodreads_data_users():
    usersGoodreadsPathFile = "data/goodreads_etl_pipeline/SampleData/user.csv"

    with open(usersGoodreadsPathFile,newline="") as csvfile:
        samples = csv.reader(csvfile, delimiter=',')
        for user in samples:
            print(user)
            break

# ¿Cuantos usuarios únicos tenemos?

# ¿Podemos generar un nuevo fichero con los datos de usuarios únicos?
# TIP: https://docs.python.org/3/library/csv.html#csv.DictWriter





if __name__ == "__main__":
    clean_goodreads_data_users()