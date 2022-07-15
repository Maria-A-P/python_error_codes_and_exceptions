import inspect
import sys
import types
import os
import errno
from errno_as_in_Linux_man import dict_of_errno_from_Linux_man
from errno_as_in_POSIX_1_2017 import dict_of_errno_as_in_POSIX
from errno_as_Win_sockets_err_codes import dict_of_errno_as_Win_sockets_err_codes

# from errno_as_from_os_strerror import dict_of_errno_from_os_strerror  # ТАК НЕ БУДУ - проще сразу тут


# просто напечатаем все сокращ назв ошибок из errno.errorcode, dict_of_errno_from_Linux_man,
#                      dict_of_errno_as_in_C   и   dict_of_errno_as_Win_sockets_err_codes
print("errno.errorcode.items()", errno.errorcode.items())
print("dict_of_errno_from_Linux_man ", dict_of_errno_from_Linux_man)
print("dict_of_errno_as_in_C ", dict_of_errno_as_in_POSIX)
print("dict_of_errno_as_Win_sockets_err_codes ", dict_of_errno_as_Win_sockets_err_codes)
# а из os.strerror создадим словарь прямо тут (но в нем не будет буквенных кодов):
dict_of_errno_from_os_strerror = dict(())
for k in range(1000000):
    result = str(os.strerror(k))
    if (result != "Unknown error"):  # on different systems this may vary, but for now I-ll leave this
        dict_of_errno_from_os_strerror[k] = result
print("dict_of_errno_from_os_strerror  ", dict_of_errno_from_os_strerror.items())

set_of_common_err_names = set(())  # {} - то есть set - без повторов, но unordered
for n in errno.errorcode.values():
    try:
        set_of_common_err_names.add(n)
    except:
        print('smth went wrong in for n in errno.errorcode.values() cycle')
for n in dict_of_errno_from_Linux_man.keys():
    try:
        set_of_common_err_names.add(n)
    except:
        print('smth went wrong in for n in dict_of_errno_from_Linux_man.keys() cycle')
for n in dict_of_errno_as_in_POSIX.keys():
    try:
        set_of_common_err_names.add(n)
    except:
        print('smth went wrong in for n in dict_of_errno_as_in_C.keys() cycle')
for n in dict_of_errno_as_Win_sockets_err_codes.keys():
    try:
        set_of_common_err_names.add(n)
    except:
        print('smth went wrong in for n in dict_of_errno_as_Win_sockets_err_codes.keys() cycle')

# now lets sort using a list:
list_of_common_err_names = list(set_of_common_err_names)
sorted_list_of_common_err_names = list_of_common_err_names[:]
sorted_list_of_common_err_names.sort()
print()
print("sorted_list_of_common_err_names  ", sorted_list_of_common_err_names)
print(len(sorted_list_of_common_err_names))

# найдем максимальную длину сокращенного имени ошибки:
max_len_of_name = 0
for n in sorted_list_of_common_err_names:
    current_len = len(str(n))
    if current_len > max_len_of_name: max_len_of_name = current_len
field_width_for_name = max_len_of_name + 2

# и теперь для каждого сокращ назв ошибки выведем его числовой код из errno.errorcode и
#    три расшифровки смысла: из dict_of_errno_from_Linux_man,   из   dict_of_errno_as_in_C  и
#           из dict_of_errno_as_Win_sockets_err_codes - и сравним
print()
print("--------------------------------------------------------------")
print("comparison of different sources (for abbreviated error names):")
print("'errno' - from  errno.errorcode")
print("'os_str by #' - from  os.strerror, match by errno.errorcode number (+ see below)")
print("'Linux' - from  dict_of_errno_from_Linux_man")
print("'POSIX' - from  dict_of_errno_as_in_POSIX")
print("'WinS' - from  dict_of_errno_as_Win_sockets_err_codes")
field_width_2 = 16  # пока вручную: дб чуть больше, чем (длина слов errno, Linux, POSIX, WinS, 'os_str by #' плюс пробелы и двоеточие)
for n in sorted_list_of_common_err_names:
    print(n.center(field_width_for_name, ' '), end=":")
    # -----------
    key_from_errno_errorcode = "-"
    value_from_os_strerror = "? (see below)"
    for k, v in errno.errorcode.items():
        try:
            if v == n:  # так можно, потому что в этом словаре точно нет повторов -
                key_from_errno_errorcode = str(k)  # - хотя по-хорошему надо и это перепроверять - но пока не буду
                value_from_os_strerror = dict_of_errno_from_os_strerror.get(k)
            # то есть здесь os.strerror берем только тогда, когда аббревиатура = errno.errorcode.value
            # а это не все значения - поэтому потом (below) дополнительно выведем и то, и то для всех сущ. номеров
        except:
            print('smth was wrong')  # надо конкретизировать, где, но не буду
    print("  errno :".ljust(field_width_2), key_from_errno_errorcode)
    print(" ".center(field_width_for_name), "  os_str by # :".ljust(field_width_2), value_from_os_strerror)
    # -----------
    value_from_dict_Linux = "-"  # не нужно: и так возвращает None (но оставлю - мало ли что)
    try:
        value_from_dict_Linux = dict_of_errno_from_Linux_man.get(n)
    except:
        print('smth was wrong')  # надо конкретизировать, где, но не буду
    print(' '.center(field_width_for_name), "  Linux :".ljust(field_width_2), value_from_dict_Linux)
    # -----------
    value_from_dict_C = "-"  # не нужно: и так возвращает None (но оставлю - мало ли что)
    try:
        value_from_dict_C = dict_of_errno_as_in_POSIX.get(n)
    except:
        print('smth was wrong')  # надо конкретизировать, где, но не буду
    print(' '.center(field_width_for_name), "  C :".ljust(field_width_2), value_from_dict_C)
    # -----------
    value_from_dict_WinS = "-"  # не нужно: и так возвращает None (но оставлю - мало ли что)
    try:
        value_from_dict_WinS = dict_of_errno_as_Win_sockets_err_codes.get(n)
    except:
        print('smth was wrong')  # надо конкретизировать, где, но не буду
    print(' '.center(field_width_for_name), "  WinS :".ljust(field_width_2), value_from_dict_WinS)
    # -----------
    print()

print()
print()
print()
# теперь выведу для цифровых кодов - без использования dict, в лоб (так короче и надежнее - на всякий случай)
print("--------------------------------------------------------------")
print("comparison of different sources (for numeric codes of errors):")
print("'errno' - from  errno.errorcode")
print("'os_str' - from  os.strerror")
field_width_3 = 11
for i in range(1000000):  # вряд ли есть коды больше 100000 - но не факт
    result_errno = str(errno.errorcode.get(i))
    result_os = str(os.strerror(i))
    if not ((result_errno == "None") and (result_os == "Unknown error")):
        print(str(i).center(field_width_for_name, ' '), end=":")
        print("  errno :".ljust(field_width_3), result_errno.ljust(field_width_for_name), end="")
        print("  os_str :".ljust(field_width_3), result_os)
        # os.strerror знает и все те цифровые коды, которые знает errno.errorcode (если они имеют один смысл - ?)
        #   и плюс os.strerror знает дополнительные коды цифровые
        # но поскольку os.strerror не выдает буквенного кода, достоверно сопоставить описание с другими источниками нереально
        # то есть плюс errno.errorcode - в том, что он выдаёт буквенное сокращение стандартное,
        # а os.strerror хоть и не знает буквенных сокращений, но самих ошибок детектирует больше.
        print()

print()
print()
print("--------------------------------------------------------------")
print("CONCLUSION:")
print(""" (to the moment this text is being written, manually)
    We have compared three external sources of information concerning error names abbreviations
    (... from_Linux_man, ... as_in_POSIX and ... as_Win_sockets_err_codes)
    - which are the most extensive and cover 223 unique abbeviated error names,

    and two python means (errno.errorcode and os.strerror)
    - which both do not cover all possible errors.
    ------------------------------------------------------------------
    53 errors are common to errno.errorcode and os.strerror, if mapped by error number.

    errno.errorcode   maps an error number to error name abbreviation and covers  101 errors (53 of which are common)

    os.strerror       maps an error number to error description phrase and covers 78 errors (53 of which are common)

    (!!!) As the error numbers are subject to change, 
    the correspondence between  os.strerror  and  errno.errorcode  is controversial.
    ------------------------------------------------------------------
    """)


