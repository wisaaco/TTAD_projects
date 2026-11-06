import csv

def unique_users(usersGoodreadsPathFile):
    with open(usersGoodreadsPathFile,newline="") as csvfile:
        samples = csv.reader(csvfile, delimiter=',')
        collection_users = {}
        for row in samples:
            collection_users[row[0]]= ""
        return len(collection_users.keys())-1 #header

if __name__ == "__main__":

    usersGoodreadsPathFile = "data/goodreads_etl_pipeline/SampleData/user.csv"
    total = unique_users(usersGoodreadsPathFile)
    print("Total users for file %s is: %i"%(usersGoodreadsPathFile,total))
