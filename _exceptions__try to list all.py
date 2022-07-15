import inspect
import sys

list_of_exc_names = []
for n1 in BaseException.__subclasses__():
    list_of_exc_names.append(n1)
    for n2 in n1.__subclasses__():
        list_of_exc_names.append(n2)
        for n3 in n2.__subclasses__():
            list_of_exc_names.append(n3)
            for n4 in n3.__subclasses__():
                list_of_exc_names.append(n4)
                for n5 in n4.__subclasses__():
                    list_of_exc_names.append(n5)
                    for n6 in n5.__subclasses__():
                        list_of_exc_names.append(n6)
                        for n7 in n6.__subclasses__():
                            list_of_exc_names.append(n7)

print(list_of_exc_names)
print(len(list_of_exc_names))

list_of_exc_names_modified = []
for n in range(len(list_of_exc_names)):
    s1 = str(list_of_exc_names[n])
    s2 = s1.replace('<class \'', '')
    s3 = s2.replace('\'>', '')
    list_of_exc_names_modified.append(s3)

list_of_exc_names_modified_and_sorted = list_of_exc_names_modified[:]
list_of_exc_names_modified_and_sorted.sort()

print(list_of_exc_names_modified)
print(list_of_exc_names_modified_and_sorted)
print(len(list_of_exc_names_modified_and_sorted))
print("= = = = =")

for n in list_of_exc_names_modified_and_sorted:
    print()
    print(n)
    try:
        nn = eval(n)
        print(nn)
        # print(type(nn))
        print("INSPECT_GETMODULE:", inspect.getmodule(nn))
        print("INSPECT_GETDOC (mozhet tianutjsja ot roditelya):",  inspect.getdoc(nn))
        #print("INSPECTGETCOMMENTS:", inspect.getcomments(nn))
        print("INSPECT_MRO (module resolution order):", inspect.getmro(nn))
    except:
        print('oi!')
        print("SYSEXECINFO:",  sys.exc_info())


