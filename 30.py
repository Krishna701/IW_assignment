def check_key(dict , key):
    if key in dict.key():
        print(f"{dict[key]} is present.")
    else:
        print(f"{dict[key]} is not present.")


dict={1: "assignments",2:"are fun",3:"to workon."}

key= 1
check_key(dict,key)

key= 'a'
check_key(dict,key)