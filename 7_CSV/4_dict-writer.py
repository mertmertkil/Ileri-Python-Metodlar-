import csv

with open("urunler.csv","w") as file:
    headers = ["Id", "ProductName", "Price", "IsActive", "Category", "Rating"]
    csv_writer = csv.DictWriter(file, headers)
    csv_writer.writeheader()
    # csv_writer.writerow({
    #     "Id" : 1,
    #     "ProductName": "Iphone 14",
    #     "Price": 40000,
    #     "IsActive": True,
    #     "Category" : "Phone",
    #     "Rating": 4.6
    # })

    # csv_writer.writerow({
    #     "Id" : 2,
    #     "ProductName": "Iphone 15",
    #     "Price": 50000,
    #     "IsActive": True,
    #     "Category" : "Phone",
    #     "Rating": 4.6
    # })

    # yukarıdakini tek satırda yazıcaz.

    csv_writer.writerows([
        {
            "Id" : 1,
            "ProductName": "Iphone 14",
            "Price": 40000,
            "IsActive": True,
            "Category" : "Phone",
            "Rating": 4.6
        },
        {
            "Id" : 2,
            "ProductName": "Iphone 15",
            "Price": 50000,
            "IsActive": True,
            "Category" : "Phone",
            "Rating": 4.6
        },
        {   
            "Id": 3,
            "ProductName": "Iphone 16",
            "Price": 60000,
            "IsActive": True,
            "Category": "Phone",
            "Rating": 4.8
        },
    ])