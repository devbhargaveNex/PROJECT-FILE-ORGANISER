def operate(iteminfo,items):
    print(f"No. of files found {len(iteminfo)}")
    choice = 0
    finallist = items
    while choice != '4':
        print("1.Show files\n2.Remove files\n3.DRY Run\n4.Move files")
        choice = input("_")
        if choice == '1':
            for ext , name in iteminfo.items():
                print(f"Name of file is {name} and it is a {ext}")
                print(f"No. of files found {len(iteminfo)}")
        elif choice == '2':
            rmfiles = input("enter files to remove with name and ext: ")
            rmfiles = rmfiles.split(",")
            for files in rmfiles:
                finallist.remove(files)
        elif choice == '3':
            pass
        elif choice == '4':
            operation = "move"
    return finallist , operation