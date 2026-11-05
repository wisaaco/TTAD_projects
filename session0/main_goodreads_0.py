import csv
#skjdksjdksjdksdjksdjksdsjldfldgñjfgj
def unique_users(usersGoodreadsPathFile):
    with open(usersGoodreadsPathFile,newline="") as csvfile:
        samples = csv.reader(csvfile, delimiter=',')
        collection_ids = {}
        for row in samples:
            collection_ids[row[0]]=""
        total_users = len(collection_ids.keys())-1 #header
        return total_users

if __name__ == "__main__":
    usersGoodreadsPathFile = "data/goodreads_etl_pipeline/SampleData/user.csv"
    total = unique_users(usersGoodreadsPathFile)

    usersGoodreadsPathFile2 = "data/goodreads_etl_pipeline/SampleData/user2.csv"
    total2 = unique_users(usersGoodreadsPathFile2)


    total3 = unique_users()
    print(total+total2+total3)
