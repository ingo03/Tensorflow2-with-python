from subprocess import call
with open("outdated.txt",'r') as packages_file:
    #these two readline() for first 2 rows
    packages_file.readline()
    packages_file.readline()

    package= True

    while package:
        package= packages_file.readline()
        if package.split():
            package_name =package.split()[0]
            print("Update-->",package_name)
            call(f"pip install --upgrade {package_name} " , shell=True)