#dictionary program
def Dictionary(**details):
    for key,value in details.items():
        print(key,":",value)
Dictionary(Name="Kusma",
        age=21,
        address="Kurnool",
        phoneNumber=987654321)