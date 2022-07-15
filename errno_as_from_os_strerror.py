import os
import errno
import sys


# ЭТОТ МОДУЛЬ НЕ ИСПОЛЬЗУЕТСЯ В ДАЛЬНЕЙШЕМ, В НЕМ ПРОСТО ОТДЕЛЬНО СРАВНИВАЮТСЯ os.strerror И  errno.errorcode

# сравним os.strerror и errno.errorcode
for i in range(100000):  # вряд ли есть коды больше 100000 - но не факт
    result = os.strerror(i)
    result_errno_errorcode = errno.errorcode.get(i)           # lets also compare to errno.errorcode:
    if not ((str(result) == "Unknown error") and (str(result_errno_errorcode) == "None")):
        print('i = ', i, 'os.strerror(i) = ', result, '   errno.errorcode.get(i) = ', result_errno_errorcode)
        # os.strerror знает и все те цифровые коды, которые знает errno.errorcode (если они имеют один смысл - ?)
        #   и плюс os.strerror знает дополнительные коды цифровые
        # но поскольку os.strerror не выдает буквенного кода, достоверно сопоставить описание с другими источниками нереально
        # то есть плюс errno.errorcode - в том, что он выдаёт буквенное сокращение стандартное,
        # а os.strerror хоть и не знает буквенных сокращений, но самих ошибок детектирует больше.
print()


dict_of_errno_from_os_strerror = dict(())
for k in range(1000000):
    result = os.strerror(k)
    if (result != "Unknown error"):    # on different systems this may vary, but for now I-ll leave this
        dict_of_errno_from_os_strerror[k] = result
print(dict_of_errno_from_os_strerror.items())


#create_dict_os_strerror()
#print(dict_of_errno_from_os_strerror.items())

#os.error = 137
#print(os.strerror(os.error))
# print("---")
#
# n = 2
# os.error = n
# print("S: ", sys.exc_info())
# m = 1/0
# print("S: ", sys.exc_info())
