print("....FIND YOUR BIRTH MONTH....")
dic = {"viswa": "August", "venkat": "May", "likhit": "August"}
while True:
    a = input("\nEnter a name to find  birth_month : ").lower()
    

    if a in dic:
        b = dic.get(a)
        print(f"\n{a}'s birthday is in {b} ...")
    else:
        print("name not found !")
    print("\nWANT U ADD NEW ONE ! : (yes/no)")
    n=input("").lower()
    if n=="no":
        print("THANK YOU! EXITED..")
        break
    if n=="yes":
        name = input("\nEnter a name : ").lower()
        month = input("\nEnter  a birth month : ").capitalize()
        if name in dic:
            print("Name is already existed !")
        else:

            dic[name] = month
            print("\nAdded Successfully !")
    print("\nDo u want all birthday list, click (yes/no) : ")
    k=input("")
    if k=="yes":
        for name,month in dic.items():
            print(f"\n{name.title()}: {month}")
            
    else:
        
        print("\nAre u Want Exit (yes/no) : ")
        l=input("")
        if l=="yes":
            break
        else:
            continue