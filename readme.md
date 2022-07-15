Файл "_exceptions__try to list all.py" служит для вывода всех известных exceptions при условии, что они изначально наследуются от класса BaseException (глубину поиска "наследников" можно менять, сейчас это семь уровней).
Выводятся имя модуля, в котором описано exception, описание (записанное в модуле как комментарий) и вся цепочка наследования.
Информация собирается при помощи модуля inspect (замечено, что часть информации при ее отсутствии данный модуль может заменять информацией для родительского класса). 

====================

Файл "_errno__try to list all.py" служит для вывода собственно кодов ошибок - буквенных и цифровых.
Были использованы следующие источники:
1) встроенный словарь errno.errorcode (буквенный и цифровой коды)
2) встроенная функция os.strerror (цифровой код и текстовое описание)
3) описание errno.h из справочника (man3) линукса (буквенный код и текстовое описание - заведены в "errno_as_in_Linux_man.py")
4) описание errno.h из стандарта POSIX.1-2017 (буквенный код и текстовое описание - заведены в "errno_as_in_POSIX_1_2017.py")
5) описание Windows Sockets Error Codes (буквенный код и текстовое описание - заведены в "errno_as_Win_sockets_err_codes.py")

Поскольку источник 2 (os.strerror) не содержит буквенного кода, сопоставление его со всеми остальными производилось только по цифровому коду, но это ненадёжно.

Программа выводит вначале список буквенных кодов ошибок и соответствующие им данные из всех пяти источников (из os.strerror - только опосредованно, через цифровой код из errno.errorcode).

Затем (чтобы вывести все доступные данные из os.strerror), выводятся цифровые коды ошибок и соответствующие им данные из errno.errorcode и os.strerror

============================
Пример (часть) вывода информации об exceptions (с помощью "_exceptions__try to list all.py"):
============================
```
Warning
<class 'Warning'>
INSPECT_GETMODULE: <module 'builtins' (built-in)>
INSPECT_GETDOC (mozhet tianutjsja ot roditelya): Base class for warning categories.
INSPECT_MRO (module resolution order): (<class 'Warning'>, <class 'Exception'>, <class 'BaseException'>, <class 'object'>)

ZeroDivisionError
<class 'ZeroDivisionError'>
INSPECT_GETMODULE: <module 'builtins' (built-in)>
INSPECT_GETDOC (mozhet tianutjsja ot roditelya): Second argument to a division or modulo operation was zero.
INSPECT_MRO (module resolution order): (<class 'ZeroDivisionError'>, <class 'ArithmeticError'>, <class 'Exception'>, <class 'BaseException'>, <class 'object'>)
```
============================
Ниже приводится списки ошибок (вначале - с группировкой по буквенным кодам, затем - по цифровым), 
генерируемые с помощью "_errno__try to list all.py":
============================

```
comparison of different sources (for abbreviated error names):
'errno' - from  errno.errorcode
'os_str by #' - from  os.strerror, match by errno.errorcode number (+ see below)
'Linux' - from  dict_of_errno_from_Linux_man
'POSIX' - from  dict_of_errno_as_in_POSIX
'WinS' - from  dict_of_errno_as_Win_sockets_err_codes
           E2BIG            :  errno :        7
                               os_str by # :  Arg list too long
                               Linux :        Argument list too long (POSIX.1-2001).
                               POSIX :        Argument list too long.
                               WinS :         None

           EACCES           :  errno :        13
                               os_str by # :  Permission denied
                               Linux :        Permission denied (POSIX.1-2001).
                               POSIX :        Permission denied.
                               WinS :         None

         EADDRINUSE         :  errno :        -
                               os_str by # :  ? (see below)
                               Linux :        Address already in use (POSIX.1-2001).
                               POSIX :        Address in use.
                               WinS :         None

       EADDRNOTAVAIL        :  errno :        -
                               os_str by # :  ? (see below)
                               Linux :        Address not available (POSIX.1-2001).
                               POSIX :        Address not available.
                               WinS :         None

        EAFNOSUPPORT        :  errno :        -
                               os_str by # :  ? (see below)
                               Linux :        Address family not supported (POSIX.1-2001).
                               POSIX :        Address family not supported.
                               WinS :         None

           EAGAIN           :  errno :        11
                               os_str by # :  Resource temporarily unavailable
                               Linux :        Resource temporarily unavailable (may be the same value as EWOULDBLOCK) (POSIX.1-2001).
                               POSIX :        Resource unavailable, try again (may be the same value as EWOULDBLOCK).
                               WinS :         None

          EALREADY          :  errno :        -
                               os_str by # :  ? (see below)
                               Linux :        Connection already in progress (POSIX.1-2001).
                               POSIX :        Connection already in progress.
                               WinS :         None

           EBADE            :  errno :        -
                               os_str by # :  ? (see below)
                               Linux :        Invalid exchange.
                               POSIX :        None
                               WinS :         None

           EBADF            :  errno :        9
                               os_str by # :  Bad file descriptor
                               Linux :        Bad file descriptor (POSIX.1-2001).
                               POSIX :        Bad file descriptor.
                               WinS :         None

           EBADFD           :  errno :        -
                               os_str by # :  ? (see below)
                               Linux :        File descriptor in bad state.
                               POSIX :        None
                               WinS :         None

          EBADMSG           :  errno :        104
                               os_str by # :  bad message
                               Linux :        Bad message (POSIX.1-2001).
                               POSIX :        Bad message.
                               WinS :         None

           EBADR            :  errno :        -
                               os_str by # :  ? (see below)
                               Linux :        Invalid request descriptor.
                               POSIX :        None
                               WinS :         None

          EBADRQC           :  errno :        -
                               os_str by # :  ? (see below)
                               Linux :        Invalid request code.
                               POSIX :        None
                               WinS :         None

          EBADSLT           :  errno :        -
                               os_str by # :  ? (see below)
                               Linux :        Invalid slot.
                               POSIX :        None
                               WinS :         None

           EBUSY            :  errno :        16
                               os_str by # :  Resource device
                               Linux :        Device or resource busy (POSIX.1-2001).
                               POSIX :        Device or resource busy.
                               WinS :         None

         ECANCELED          :  errno :        105
                               os_str by # :  operation canceled
                               Linux :        Operation canceled (POSIX.1-2001).
                               POSIX :        Operation canceled.
                               WinS :         None

           ECHILD           :  errno :        10
                               os_str by # :  No child processes
                               Linux :        No child processes (POSIX.1-2001).
                               POSIX :        No child processes.
                               WinS :         None

           ECHRNG           :  errno :        -
                               os_str by # :  ? (see below)
                               Linux :        Channel number out of range.
                               POSIX :        None
                               WinS :         None

           ECOMM            :  errno :        -
                               os_str by # :  ? (see below)
                               Linux :        Communication error on send.
                               POSIX :        None
                               WinS :         None

        ECONNABORTED        :  errno :        -
                               os_str by # :  ? (see below)
                               Linux :        Connection aborted (POSIX.1-2001).
                               POSIX :        Connection aborted.
                               WinS :         None

        ECONNREFUSED        :  errno :        -
                               os_str by # :  ? (see below)
                               Linux :        Connection refused (POSIX.1-2001).
                               POSIX :        Connection refused.
                               WinS :         None

         ECONNRESET         :  errno :        -
                               os_str by # :  ? (see below)
                               Linux :        Connection reset (POSIX.1-2001).
                               POSIX :        Connection reset.
                               WinS :         None

          EDEADLK           :  errno :        -
                               os_str by # :  ? (see below)
                               Linux :        Resource deadlock avoided (POSIX.1-2001).
                               POSIX :        Resource deadlock would occur.
                               WinS :         None

         EDEADLOCK          :  errno :        36
                               os_str by # :  Resource deadlock avoided
                               Linux :        On most architectures, a synonym for EDEADLK.  On some architectures (e.g., Linux MIPS, PowerPC, SPARC), it is a separate error code File_locking_deadlock_error.
                               POSIX :        None
                               WinS :         None

        EDESTADDRREQ        :  errno :        -
                               os_str by # :  ? (see below)
                               Linux :        Destination address required (POSIX.1-2001).
                               POSIX :        Destination address required.
                               WinS :         None

            EDOM            :  errno :        33
                               os_str by # :  Domain error
                               Linux :        Mathematics argument out of domain of function (POSIX.1, C99).
                               POSIX :        Mathematics argument out of domain of function.
                               WinS :         None

           EDQUOT           :  errno :        -
                               os_str by # :  ? (see below)
                               Linux :        Disk quota exceeded (POSIX.1-2001).
                               POSIX :        Reserved.
                               WinS :         None

           EEXIST           :  errno :        17
                               os_str by # :  File exists
                               Linux :        File exists (POSIX.1-2001).
                               POSIX :        File exists.
                               WinS :         None

           EFAULT           :  errno :        14
                               os_str by # :  Bad address
                               Linux :        Bad address (POSIX.1-2001).
                               POSIX :        Bad address.
                               WinS :         None

           EFBIG            :  errno :        27
                               os_str by # :  File too large
                               Linux :        File too large (POSIX.1-2001).
                               POSIX :        File too large.
                               WinS :         None

         EHOSTDOWN          :  errno :        -
                               os_str by # :  ? (see below)
                               Linux :        Host is down.
                               POSIX :        None
                               WinS :         None

        EHOSTUNREACH        :  errno :        -
                               os_str by # :  ? (see below)
                               Linux :        Host is unreachable (POSIX.1-2001).
                               POSIX :        Host is unreachable.
                               WinS :         None

         EHWPOISON          :  errno :        -
                               os_str by # :  ? (see below)
                               Linux :        Memory page has hardware error.
                               POSIX :        None
                               WinS :         None

           EIDRM            :  errno :        111
                               os_str by # :  identifier removed
                               Linux :        Identifier removed (POSIX.1-2001).
                               POSIX :        Identifier removed.
                               WinS :         None

           EILSEQ           :  errno :        42
                               os_str by # :  Illegal byte sequence
                               Linux :        Invalid or incomplete multibyte or wide character (POSIX.1, C99). The text shown here is the glibc error description; in POSIX.1, this error is described as Illegal_byte_sequence.
                               POSIX :        Illegal byte sequence.
                               WinS :         None

        EINPROGRESS         :  errno :        -
                               os_str by # :  ? (see below)
                               Linux :        Operation in progress (POSIX.1-2001).
                               POSIX :        Operation in progress.
                               WinS :         None

           EINTR            :  errno :        4
                               os_str by # :  Interrupted function call
                               Linux :        Interrupted function call (POSIX.1-2001); see signal(7).
                               POSIX :        Interrupted function.
                               WinS :         None

           EINVAL           :  errno :        22
                               os_str by # :  Invalid argument
                               Linux :        Invalid argument (POSIX.1-2001).
                               POSIX :        Invalid argument.
                               WinS :         None

            EIO             :  errno :        5
                               os_str by # :  Input/output error
                               Linux :        Input/output error (POSIX.1-2001).
                               POSIX :        I/O error.
                               WinS :         None

          EISCONN           :  errno :        -
                               os_str by # :  ? (see below)
                               Linux :        Socket is connected (POSIX.1-2001).
                               POSIX :        Socket is connected.
                               WinS :         None

           EISDIR           :  errno :        21
                               os_str by # :  Is a directory
                               Linux :        Is a directory (POSIX.1-2001).
                               POSIX :        Is a directory.
                               WinS :         None

           EISNAM           :  errno :        -
                               os_str by # :  ? (see below)
                               Linux :        Is a named type file.
                               POSIX :        None
                               WinS :         None

        EKEYEXPIRED         :  errno :        -
                               os_str by # :  ? (see below)
                               Linux :        Key has expired.
                               POSIX :        None
                               WinS :         None

        EKEYREJECTED        :  errno :        -
                               os_str by # :  ? (see below)
                               Linux :        Key was rejected by service.
                               POSIX :        None
                               WinS :         None

        EKEYREVOKED         :  errno :        -
                               os_str by # :  ? (see below)
                               Linux :        Key has been revoked.
                               POSIX :        None
                               WinS :         None

           EL2HLT           :  errno :        -
                               os_str by # :  ? (see below)
                               Linux :        Level 2 halted.
                               POSIX :        None
                               WinS :         None

          EL2NSYNC          :  errno :        -
                               os_str by # :  ? (see below)
                               Linux :        Level 2 not synchronized.
                               POSIX :        None
                               WinS :         None

           EL3HLT           :  errno :        -
                               os_str by # :  ? (see below)
                               Linux :        Level 3 halted.
                               POSIX :        None
                               WinS :         None

           EL3RST           :  errno :        -
                               os_str by # :  ? (see below)
                               Linux :         Level 3 reset.
                               POSIX :        None
                               WinS :         None

          ELIBACC           :  errno :        -
                               os_str by # :  ? (see below)
                               Linux :        Cannot access a needed shared library.
                               POSIX :        None
                               WinS :         None

          ELIBBAD           :  errno :        -
                               os_str by # :  ? (see below)
                               Linux :        Accessing a corrupted shared library.
                               POSIX :        None
                               WinS :         None

          ELIBEXEC          :  errno :        -
                               os_str by # :  ? (see below)
                               Linux :        Cannot exec a shared library directly.
                               POSIX :        None
                               WinS :         None

          ELIBMAX           :  errno :        -
                               os_str by # :  ? (see below)
                               Linux :        Attempting to link in too many shared libraries.
                               POSIX :        None
                               WinS :         None

          ELIBSCN           :  errno :        -
                               os_str by # :  ? (see below)
                               Linux :        .lib section in a.out corrupted
                               POSIX :        None
                               WinS :         None

          ELNRANGE          :  errno :        -
                               os_str by # :  ? (see below)
                               Linux :        Link number out of range.
                               POSIX :        None
                               WinS :         None

           ELOOP            :  errno :        -
                               os_str by # :  ? (see below)
                               Linux :        Too many levels of symbolic links (POSIX.1-2001).
                               POSIX :        Too many levels of symbolic links.
                               WinS :         None

        EMEDIUMTYPE         :  errno :        -
                               os_str by # :  ? (see below)
                               Linux :        Wrong medium type.
                               POSIX :        None
                               WinS :         None

           EMFILE           :  errno :        24
                               os_str by # :  Too many open files
                               Linux :        Too many open files (POSIX.1-2001).  Commonly caused by exceeding the RLIMIT_NOFILE resource limit described in getrlimit(2).  Can also be caused by exceeding the limit specified in /proc/sys/fs/nr_open.
                               POSIX :        File descriptor value too large.
                               WinS :         None

           EMLINK           :  errno :        31
                               os_str by # :  Too many links
                               Linux :        Too many links (POSIX.1-2001).
                               POSIX :        Too many links.
                               WinS :         None

          EMSGSIZE          :  errno :        -
                               os_str by # :  ? (see below)
                               Linux :        Message too long (POSIX.1-2001).
                               POSIX :        Message too large.
                               WinS :         None

         EMULTIHOP          :  errno :        -
                               os_str by # :  ? (see below)
                               Linux :        Multihop attempted (POSIX.1-2001).
                               POSIX :        Reserved.
                               WinS :         None

        ENAMETOOLONG        :  errno :        38
                               os_str by # :  Filename too long
                               Linux :        Filename too long (POSIX.1-2001).
                               POSIX :        Filename too long.
                               WinS :         None

          ENETDOWN          :  errno :        -
                               os_str by # :  ? (see below)
                               Linux :        Network is down (POSIX.1-2001).
                               POSIX :        Network is down.
                               WinS :         None

         ENETRESET          :  errno :        -
                               os_str by # :  ? (see below)
                               Linux :        Connection aborted by network (POSIX.1-2001).
                               POSIX :        Connection aborted by network.
                               WinS :         None

        ENETUNREACH         :  errno :        -
                               os_str by # :  ? (see below)
                               Linux :        Network unreachable (POSIX.1-2001).
                               POSIX :        Network unreachable.
                               WinS :         None

           ENFILE           :  errno :        23
                               os_str by # :  Too many open files in system
                               Linux :        Too many open files in system (POSIX.1-2001).  On Linux, this is probably a result of encountering the /proc/sys/fs/file-max limit (see proc(5)).
                               POSIX :        Too many files open in system.
                               WinS :         None

           ENOANO           :  errno :        -
                               os_str by # :  ? (see below)
                               Linux :        No anode.
                               POSIX :        None
                               WinS :         None

          ENOBUFS           :  errno :        -
                               os_str by # :  ? (see below)
                               Linux :        No buffer space available (POSIX.1 (XSI STREAMS option)).
                               POSIX :        No buffer space available.
                               WinS :         None

          ENODATA           :  errno :        120
                               os_str by # :  no message available
                               Linux :        The named attribute does not exist, or the process has no access to this attribute; see xattr(7). In POSIX.1-2001 (XSI STREAMS option), this error was described as _ _ No message is available on the STREAM head read queue _ _.
                               POSIX :        [OBSOLETE, XSR-optional]No message is available on the STREAM head read queue.
                               WinS :         None

           ENODEV           :  errno :        19
                               os_str by # :  No such device
                               Linux :        No such device (POSIX.1-2001).
                               POSIX :        No such device.
                               WinS :         None

           ENOENT           :  errno :        2
                               os_str by # :  No such file or directory
                               Linux :        No such file or directory (POSIX.1-2001). Typically, this error results when a specified pathname does not exist, or one of the components in the directory prefix of a pathname does not exist, or the specified pathname is a dangling symbolic link.
                               POSIX :        No such file or directory.
                               WinS :         None

          ENOEXEC           :  errno :        8
                               os_str by # :  Exec format error
                               Linux :        Exec format error (POSIX.1-2001).
                               POSIX :        Executable file format error.
                               WinS :         None

           ENOKEY           :  errno :        -
                               os_str by # :  ? (see below)
                               Linux :        Required key not available.
                               POSIX :        None
                               WinS :         None

           ENOLCK           :  errno :        39
                               os_str by # :  No locks available
                               Linux :        No locks available (POSIX.1-2001).
                               POSIX :        No locks available.
                               WinS :         None

          ENOLINK           :  errno :        121
                               os_str by # :  no link
                               Linux :        Link has been severed (POSIX.1-2001).
                               POSIX :        Reserved.
                               WinS :         None

         ENOMEDIUM          :  errno :        -
                               os_str by # :  ? (see below)
                               Linux :        No medium found.
                               POSIX :        None
                               WinS :         None

           ENOMEM           :  errno :        12
                               os_str by # :  Not enough space
                               Linux :        Not enough space/cannot allocate memory (POSIX.1-2001).
                               POSIX :        Not enough space.
                               WinS :         None

           ENOMSG           :  errno :        122
                               os_str by # :  no message
                               Linux :        No message of the desired type (POSIX.1-2001).
                               POSIX :        No message of the desired type.
                               WinS :         None

           ENONET           :  errno :        -
                               os_str by # :  ? (see below)
                               Linux :        Machine is not on the network.
                               POSIX :        None
                               WinS :         None

           ENOPKG           :  errno :        -
                               os_str by # :  ? (see below)
                               Linux :        Package not installed.
                               POSIX :        None
                               WinS :         None

        ENOPROTOOPT         :  errno :        -
                               os_str by # :  ? (see below)
                               Linux :        Protocol not available (POSIX.1-2001).
                               POSIX :        Protocol not available.
                               WinS :         None

           ENOSPC           :  errno :        28
                               os_str by # :  No space left on device
                               Linux :        No space left on device (POSIX.1-2001).
                               POSIX :        No space left on device.
                               WinS :         None

           ENOSR            :  errno :        124
                               os_str by # :  no stream resources
                               Linux :         No STREAM resources (POSIX.1 (XSI STREAMS option)).
                               POSIX :        [OBSOLETE, XSR-optional]No STREAM resources.
                               WinS :         None

           ENOSTR           :  errno :        125
                               os_str by # :  not a stream
                               Linux :        Not a STREAM (POSIX.1 (XSI STREAMS option)).
                               POSIX :        [OBSOLETE, XSR-optional]Not a STREAM.
                               WinS :         None

           ENOSYS           :  errno :        40
                               os_str by # :  Function not implemented
                               Linux :        Function not implemented (POSIX.1-2001).
                               POSIX :        Functionality not supported.
                               WinS :         None

          ENOTBLK           :  errno :        -
                               os_str by # :  ? (see below)
                               Linux :        Block device required.
                               POSIX :        None
                               WinS :         None

          ENOTCONN          :  errno :        -
                               os_str by # :  ? (see below)
                               Linux :        The socket is not connected (POSIX.1-2001).
                               POSIX :        The socket is not connected.
                               WinS :         None

          ENOTDIR           :  errno :        20
                               os_str by # :  Not a directory
                               Linux :        Not a directory (POSIX.1-2001).
                               POSIX :        Not a directory or a symbolic link to a directory.
                               WinS :         None

         ENOTEMPTY          :  errno :        41
                               os_str by # :  Directory not empty
                               Linux :        Directory not empty (POSIX.1-2001).
                               POSIX :        Directory not empty.
                               WinS :         None

      ENOTRECOVERABLE       :  errno :        127
                               os_str by # :  state not recoverable
                               Linux :        State not recoverable (POSIX.1-2008).
                               POSIX :        State not recoverable.
                               WinS :         None

          ENOTSOCK          :  errno :        -
                               os_str by # :  ? (see below)
                               Linux :        Not a socket (POSIX.1-2001).
                               POSIX :        Not a socket.
                               WinS :         None

          ENOTSUP           :  errno :        129
                               os_str by # :  not supported
                               Linux :        Operation not supported (POSIX.1-2001).
                               POSIX :        Not supported (may be the same value as EOPNOTSUPP).
                               WinS :         None

           ENOTTY           :  errno :        25
                               os_str by # :  Inappropriate I/O control operation
                               Linux :        Inappropriate I/O control operation (POSIX.1-2001).
                               POSIX :        Inappropriate I/O control operation.
                               WinS :         None

          ENOTUNIQ          :  errno :        -
                               os_str by # :  ? (see below)
                               Linux :        Name not unique on network.
                               POSIX :        None
                               WinS :         None

           ENXIO            :  errno :        6
                               os_str by # :  No such device or address
                               Linux :         No such device or address (POSIX.1-2001).
                               POSIX :        No such device or address.
                               WinS :         None

         EOPNOTSUPP         :  errno :        -
                               os_str by # :  ? (see below)
                               Linux :        Operation not supported on socket (POSIX.1-2001). (ENOTSUP and EOPNOTSUPP have the same value on Linux, but according to POSIX.1 these error values should be distinct.)
                               POSIX :        Operation not supported on socket (may be the same value as ENOTSUP).
                               WinS :         None

         EOVERFLOW          :  errno :        132
                               os_str by # :  value too large
                               Linux :        Value too large to be stored in data type (POSIX.1-2001).
                               POSIX :        Value too large to be stored in data type.
                               WinS :         None

         EOWNERDEAD         :  errno :        133
                               os_str by # :  owner dead
                               Linux :        Owner died (POSIX.1-2008).
                               POSIX :        Previous owner died.
                               WinS :         None

           EPERM            :  errno :        1
                               os_str by # :  Operation not permitted
                               Linux :         Operation not permitted (POSIX.1-2001).
                               POSIX :        Operation not permitted.
                               WinS :         None

        EPFNOSUPPORT        :  errno :        -
                               os_str by # :  ? (see below)
                               Linux :        Protocol family not supported.
                               POSIX :        None
                               WinS :         None

           EPIPE            :  errno :        32
                               os_str by # :  Broken pipe
                               Linux :         Broken pipe (POSIX.1-2001).
                               POSIX :        Broken pipe.
                               WinS :         None

           EPROTO           :  errno :        134
                               os_str by # :  protocol error
                               Linux :        Protocol error (POSIX.1-2001).
                               POSIX :        Protocol error.
                               WinS :         None

      EPROTONOSUPPORT       :  errno :        -
                               os_str by # :  ? (see below)
                               Linux :        Protocol not supported (POSIX.1-2001).
                               POSIX :        Protocol not supported.
                               WinS :         None

         EPROTOTYPE         :  errno :        -
                               os_str by # :  ? (see below)
                               Linux :        Protocol wrong type for socket (POSIX.1-2001).
                               POSIX :        Protocol wrong type for socket.
                               WinS :         None

           ERANGE           :  errno :        34
                               os_str by # :  Result too large
                               Linux :        Result too large (POSIX.1, C99).
                               POSIX :        Result too large.
                               WinS :         None

          EREMCHG           :  errno :        -
                               os_str by # :  ? (see below)
                               Linux :        Remote address changed.
                               POSIX :        None
                               WinS :         None

          EREMOTE           :  errno :        -
                               os_str by # :  ? (see below)
                               Linux :        Object is remote.
                               POSIX :        None
                               WinS :         None

         EREMOTEIO          :  errno :        -
                               os_str by # :  ? (see below)
                               Linux :        Remote I/O error.
                               POSIX :        None
                               WinS :         None

          ERESTART          :  errno :        -
                               os_str by # :  ? (see below)
                               Linux :        Interrupted system call should be restarted.
                               POSIX :        None
                               WinS :         None

          ERFKILL           :  errno :        -
                               os_str by # :  ? (see below)
                               Linux :        Operation not possible due to RF-kill.
                               POSIX :        None
                               WinS :         None

           EROFS            :  errno :        30
                               os_str by # :  Read-only file system
                               Linux :         Read-only filesystem (POSIX.1-2001).
                               POSIX :        Read-only file system.
                               WinS :         None

         ESHUTDOWN          :  errno :        -
                               os_str by # :  ? (see below)
                               Linux :        Cannot send after transport endpoint shutdown.
                               POSIX :        None
                               WinS :         None

      ESOCKTNOSUPPORT       :  errno :        -
                               os_str by # :  ? (see below)
                               Linux :        Socket type not supported.
                               POSIX :        None
                               WinS :         None

           ESPIPE           :  errno :        29
                               os_str by # :  Invalid seek
                               Linux :        Invalid seek (POSIX.1-2001).
                               POSIX :        Invalid seek.
                               WinS :         None

           ESRCH            :  errno :        3
                               os_str by # :  No such process
                               Linux :         No such process (POSIX.1-2001).
                               POSIX :        No such process.
                               WinS :         None

           ESTALE           :  errno :        -
                               os_str by # :  ? (see below)
                               Linux :        Stale file handle (POSIX.1-2001). This error can occur for NFS and for other filesystems.
                               POSIX :        Reserved.
                               WinS :         None

          ESTRPIPE          :  errno :        -
                               os_str by # :  ? (see below)
                               Linux :        Streams pipe error.
                               POSIX :        None
                               WinS :         None

           ETIME            :  errno :        137
                               os_str by # :  stream timeout
                               Linux :        Timer expired (POSIX.1 (XSI STREAMS option)). (POSIX.1 says "STREAM ioctl(2) timeout".)
                               POSIX :        [OBSOLETE, XSR-optional]Stream ioctl() timeout.
                               WinS :         None

         ETIMEDOUT          :  errno :        -
                               os_str by # :  ? (see below)
                               Linux :        Connection timed out (POSIX.1-2001).
                               POSIX :        Connection timed out.
                               WinS :         None

        ETOOMANYREFS        :  errno :        -
                               os_str by # :  ? (see below)
                               Linux :        Too many references: cannot splice.
                               POSIX :        None
                               WinS :         None

          ETXTBSY           :  errno :        139
                               os_str by # :  text file busy
                               Linux :        Text file busy (POSIX.1-2001).
                               POSIX :        Text file busy.
                               WinS :         None

          EUCLEAN           :  errno :        -
                               os_str by # :  ? (see below)
                               Linux :        Structure needs cleaning.
                               POSIX :        None
                               WinS :         None

          EUNATCH           :  errno :        -
                               os_str by # :  ? (see below)
                               Linux :        Protocol driver not attached.
                               POSIX :        None
                               WinS :         None

           EUSERS           :  errno :        -
                               os_str by # :  ? (see below)
                               Linux :        Too many users.
                               POSIX :        None
                               WinS :         None

        EWOULDBLOCK         :  errno :        -
                               os_str by # :  ? (see below)
                               Linux :        None
                               POSIX :        Operation would block (may be the same value as EAGAIN).
                               WinS :         None

           EXDEV            :  errno :        18
                               os_str by # :  Improper link
                               Linux :        Improper link (POSIX.1-2001).
                               POSIX :        Cross-device link.
                               WinS :         None

           EXFULL           :  errno :        -
                               os_str by # :  ? (see below)
                               Linux :        Exchange full.
                               POSIX :        None
                               WinS :         None

         WSABASEERR         :  errno :        10000
                               os_str by # :  None
                               Linux :        None
                               POSIX :        None
                               WinS :         None

         WSAEACCES          :  errno :        10013
                               os_str by # :  None
                               Linux :        None
                               POSIX :        None
                               WinS :         Permission denied. An attempt was made to access a socket in a way forbidden by its access permissions. An example is using a broadcast address for sendto without broadcast permission being set using setsockopt(SO_BROADCAST). Another possible reason for the WSAEACCES error is that when the bind function is called (on Windows NT 4.0 with SP4 and later), another application, service, or kernel mode driver is bound to the same address with exclusive access. Such exclusive access is a new feature of Windows NT 4.0 with SP4 and later, and is implemented by using the SO_EXCLUSIVEADDRUSE option.

       WSAEADDRINUSE        :  errno :        10048
                               os_str by # :  None
                               Linux :        None
                               POSIX :        None
                               WinS :         Address already in use. Typically, only one usage of each socket address (protocol/IP address/port) is permitted. This error occurs if an application attempts to bind a socket to an IP address/port that has already been used for an existing socket, or a socket that was not closed properly, or one that is still in the process of closing. For server applications that need to bind multiple sockets to the same port number, consider using setsockopt (SO_REUSEADDR). Client applications usually need not call bind at all—connect chooses an unused port automatically. When bind is called with a wildcard address (involving ADDR_ANY), a WSAEADDRINUSE error could be delayed until the specific address is committed. This could happen with a call to another function later, including connect, listen, WSAConnect, or WSAJoinLeaf.

      WSAEADDRNOTAVAIL      :  errno :        10049
                               os_str by # :  None
                               Linux :        None
                               POSIX :        None
                               WinS :         Cannot assign requested address. The requested address is not valid in its context. This normally results from an attempt to bind to an address that is not valid for the local computer. This can also result from connect, sendto, WSAConnect, WSAJoinLeaf, or WSASendTo when the remote address or port is not valid for a remote computer (for example, address or port 0).

      WSAEAFNOSUPPORT       :  errno :        10047
                               os_str by # :  None
                               Linux :        None
                               POSIX :        None
                               WinS :         Address family not supported by protocol family. An address incompatible with the requested protocol was used. All sockets are created with an associated address family (that is, AF_INET for Internet Protocols) and a generic protocol type (that is, SOCK_STREAM). This error is returned if an incorrect protocol is explicitly requested in the socket call, or if an address of the wrong family is used for a socket, for example, in sendto.

        WSAEALREADY         :  errno :        10037
                               os_str by # :  None
                               Linux :        None
                               POSIX :        None
                               WinS :         Operation already in progress. An operation was attempted on a nonblocking socket with an operation already in progress—that is, calling connect a second time on a nonblocking socket that is already connecting, or canceling an asynchronous request (WSAAsyncGetXbyY) that has already been canceled or completed.

          WSAEBADF          :  errno :        10009
                               os_str by # :  None
                               Linux :        None
                               POSIX :        None
                               WinS :         File handle is not valid. The file handle supplied is not valid.

       WSAECANCELLED        :  errno :        -
                               os_str by # :  ? (see below)
                               Linux :        None
                               POSIX :        None
                               WinS :         Call has been canceled. A call to the WSALookupServiceEnd function was made while this call was still processing. The call has been canceled.

      WSAECONNABORTED       :  errno :        10053
                               os_str by # :  None
                               Linux :        None
                               POSIX :        None
                               WinS :         Software caused connection abort. An established connection was aborted by the software in your host computer, possibly due to a data transmission time-out or protocol error.

      WSAECONNREFUSED       :  errno :        10061
                               os_str by # :  None
                               Linux :        None
                               POSIX :        None
                               WinS :         Connection refused. No connection could be made because the target computer actively refused it. This usually results from trying to connect to a service that is inactive on the foreign host—that is, one with no server application running.

       WSAECONNRESET        :  errno :        10054
                               os_str by # :  None
                               Linux :        None
                               POSIX :        None
                               WinS :         Connection reset by peer. An existing connection was forcibly closed by the remote host. This normally results if the peer application on the remote host is suddenly stopped, the host is rebooted, the host or remote network interface is disabled, or the remote host uses a hard close (see setsockopt for more information on the SO_LINGER option on the remote socket). This error may also result if a connection was broken due to keep-alive activity detecting a failure while one or more operations are in progress. Operations that were in progress fail with WSAENETRESET. Subsequent operations fail with WSAECONNRESET.

      WSAEDESTADDRREQ       :  errno :        10039
                               os_str by # :  None
                               Linux :        None
                               POSIX :        None
                               WinS :         Destination address required. A required address was omitted from an operation on a socket. For example, this error is returned if sendto is called with the remote address of ADDR_ANY.

         WSAEDISCON         :  errno :        10101
                               os_str by # :  None
                               Linux :        None
                               POSIX :        None
                               WinS :         Graceful shutdown in progress. Returned by WSARecv and WSARecvFrom to indicate that the remote party has initiated a graceful shutdown sequence.

         WSAEDQUOT          :  errno :        10069
                               os_str by # :  None
                               Linux :        None
                               POSIX :        None
                               WinS :         Disk quota exceeded. Ran out of disk quota.

         WSAEFAULT          :  errno :        10014
                               os_str by # :  None
                               Linux :        None
                               POSIX :        None
                               WinS :         Bad address. The system detected an invalid pointer address in attempting to use a pointer argument of a call. This error occurs if an application passes an invalid pointer value, or if the length of the buffer is too small. For instance, if the length of an argument, which is a sockaddr structure, is smaller than the sizeof(sockaddr).

        WSAEHOSTDOWN        :  errno :        10064
                               os_str by # :  None
                               Linux :        None
                               POSIX :        None
                               WinS :         Host is down. A socket operation failed because the destination host is down. A socket operation encountered a dead host. Networking activity on the local host has not been initiated. These conditions are more likely to be indicated by the error WSAETIMEDOUT.

      WSAEHOSTUNREACH       :  errno :        10065
                               os_str by # :  None
                               Linux :        None
                               POSIX :        None
                               WinS :         No route to host. A socket operation was attempted to an unreachable host. See WSAENETUNREACH.

       WSAEINPROGRESS       :  errno :        10036
                               os_str by # :  None
                               Linux :        None
                               POSIX :        None
                               WinS :         Operation now in progress. A blocking operation is currently executing. Windows Sockets only allows a single blocking operation—per- task or thread—to be outstanding, and if any other function call is made (whether or not it references that or any other socket) the function fails with the WSAEINPROGRESS error.

          WSAEINTR          :  errno :        10004
                               os_str by # :  None
                               Linux :        None
                               POSIX :        None
                               WinS :         Interrupted function call. A blocking operation was interrupted by a call to WSACancelBlockingCall.

         WSAEINVAL          :  errno :        10022
                               os_str by # :  None
                               Linux :        None
                               POSIX :        None
                               WinS :         Invalid argument. Some invalid argument was supplied (for example, specifying an invalid level to the setsockopt function). In some instances, it also refers to the current state of the socket—for instance, calling accept on a socket that is not listening.

    WSAEINVALIDPROCTABLE    :  errno :        -
                               os_str by # :  ? (see below)
                               Linux :        None
                               POSIX :        None
                               WinS :         Procedure call table is invalid. The service provider procedure call table is invalid. A service provider returned a bogus procedure table to Ws2_32.dll. This is usually caused by one or more of the function pointers being NULL.

    WSAEINVALIDPROVIDER     :  errno :        -
                               os_str by # :  ? (see below)
                               Linux :        None
                               POSIX :        None
                               WinS :         Service provider is invalid. The requested service provider is invalid. This error is returned by the WSCGetProviderInfo and WSCGetProviderInfo32 functions if the protocol entry specified could not be found. This error is also returned if the service provider returned a version number other than 2.0.

         WSAEISCONN         :  errno :        10056
                               os_str by # :  None
                               Linux :        None
                               POSIX :        None
                               WinS :         Socket is already connected. A connect request was made on an already-connected socket. Some implementations also return this error if sendto is called on a connected SOCK_DGRAM socket (for SOCK_STREAM sockets, the to parameter in sendto is ignored) although other implementations treat this as a legal occurrence.

          WSAELOOP          :  errno :        10062
                               os_str by # :  None
                               Linux :        None
                               POSIX :        None
                               WinS :         Cannot translate name. Cannot translate a name.

         WSAEMFILE          :  errno :        10024
                               os_str by # :  None
                               Linux :        None
                               POSIX :        None
                               WinS :         Too many open files. Too many open sockets. Each implementation may have a maximum number of socket handles available, either globally, per process, or per thread.

        WSAEMSGSIZE         :  errno :        10040
                               os_str by # :  None
                               Linux :        None
                               POSIX :        None
                               WinS :         Message too long. A message sent on a datagram socket was larger than the internal message buffer or some other network limit, or the buffer used to receive a datagram was smaller than the datagram itself.

      WSAENAMETOOLONG       :  errno :        10063
                               os_str by # :  None
                               Linux :        None
                               POSIX :        None
                               WinS :         Name too long. A name component or a name was too long.

        WSAENETDOWN         :  errno :        10050
                               os_str by # :  None
                               Linux :        None
                               POSIX :        None
                               WinS :         Network is down. A socket operation encountered a dead network. This could indicate a serious failure of the network system (that is, the protocol stack that the Windows Sockets DLL runs over), the network interface, or the local network itself.

        WSAENETRESET        :  errno :        10052
                               os_str by # :  None
                               Linux :        None
                               POSIX :        None
                               WinS :         Network dropped connection on reset. The connection has been broken due to keep-alive activity detecting a failure while the operation was in progress. It can also be returned by setsockopt if an attempt is made to set SO_KEEPALIVE on a connection that has already failed.

       WSAENETUNREACH       :  errno :        10051
                               os_str by # :  None
                               Linux :        None
                               POSIX :        None
                               WinS :         Network is unreachable. A socket operation was attempted to an unreachable network. This usually means the local software knows no route to reach the remote host.

         WSAENOBUFS         :  errno :        10055
                               os_str by # :  None
                               Linux :        None
                               POSIX :        None
                               WinS :         No buffer space available. An operation on a socket could not be performed because the system lacked sufficient buffer space or because a queue was full.

         WSAENOMORE         :  errno :        -
                               os_str by # :  ? (see below)
                               Linux :        None
                               POSIX :        None
                               WinS :         No more results. No more results can be returned by the WSALookupServiceNext function.

       WSAENOPROTOOPT       :  errno :        10042
                               os_str by # :  None
                               Linux :        None
                               POSIX :        None
                               WinS :         Bad protocol option. An unknown, invalid or unsupported option or level was specified in a getsockopt or setsockopt call.

        WSAENOTCONN         :  errno :        10057
                               os_str by # :  None
                               Linux :        None
                               POSIX :        None
                               WinS :         Socket is not connected. A request to send or receive data was disallowed because the socket is not connected and (when sending on a datagram socket using sendto) no address was supplied. Any other type of operation might also return this error—for example, setsockopt setting SO_KEEPALIVE if the connection has been reset.

        WSAENOTEMPTY        :  errno :        10066
                               os_str by # :  None
                               Linux :        None
                               POSIX :        None
                               WinS :         Directory not empty. Cannot remove a directory that is not empty.

        WSAENOTSOCK         :  errno :        10038
                               os_str by # :  None
                               Linux :        None
                               POSIX :        None
                               WinS :         Socket operation on nonsocket. An operation was attempted on something that is not a socket. Either the socket handle parameter did not reference a valid socket, or for select, a member of an fd_set was not valid.

       WSAEOPNOTSUPP        :  errno :        10045
                               os_str by # :  None
                               Linux :        None
                               POSIX :        None
                               WinS :         Operation not supported. The attempted operation is not supported for the type of object referenced. Usually this occurs when a socket descriptor to a socket that cannot support this operation is trying to accept a connection on a datagram socket.

      WSAEPFNOSUPPORT       :  errno :        10046
                               os_str by # :  None
                               Linux :        None
                               POSIX :        None
                               WinS :         Protocol family not supported. The protocol family has not been configured into the system or no implementation for it exists. This message has a slightly different meaning from WSAEAFNOSUPPORT. However, it is interchangeable in most cases, and all Windows Sockets functions that return one of these messages also specify WSAEAFNOSUPPORT.

        WSAEPROCLIM         :  errno :        10067
                               os_str by # :  None
                               Linux :        None
                               POSIX :        None
                               WinS :         Too many processes. A Windows Sockets implementation may have a limit on the number of applications that can use it simultaneously. WSAStartup may fail with this error if the limit has been reached.

     WSAEPROTONOSUPPORT     :  errno :        10043
                               os_str by # :  None
                               Linux :        None
                               POSIX :        None
                               WinS :         Protocol not supported. The requested protocol has not been configured into the system, or no implementation for it exists. For example, a socket call requests a SOCK_DGRAM socket, but specifies a stream protocol.

       WSAEPROTOTYPE        :  errno :        10041
                               os_str by # :  None
                               Linux :        None
                               POSIX :        None
                               WinS :         Protocol wrong type for socket. A protocol was specified in the socket function call that does not support the semantics of the socket type requested. For example, the ARPA Internet UDP protocol cannot be specified with a socket type of SOCK_STREAM.

   WSAEPROVIDERFAILEDINIT   :  errno :        -
                               os_str by # :  ? (see below)
                               Linux :        None
                               POSIX :        None
                               WinS :         Service provider failed to initialize. The requested service provider could not be loaded or initialized. This error is returned if either a service provider-s DLL could not be loaded (LoadLibrary failed) or the provider-s WSPStartup or NSPStartup function failed.

        WSAEREFUSED         :  errno :        -
                               os_str by # :  ? (see below)
                               Linux :        None
                               POSIX :        None
                               WinS :         Database query was refused. A database query failed because it was actively refused.

         WSAEREMOTE         :  errno :        10071
                               os_str by # :  None
                               Linux :        None
                               POSIX :        None
                               WinS :         Item is remote. The item is not available locally.

        WSAESHUTDOWN        :  errno :        10058
                               os_str by # :  None
                               Linux :        None
                               POSIX :        None
                               WinS :         Cannot send after socket shutdown. A request to send or receive data was disallowed because the socket had already been shut down in that direction with a previous shutdown call. By calling shutdown a partial close of a socket is requested, which is a signal that sending or receiving, or both have been discontinued.

     WSAESOCKTNOSUPPORT     :  errno :        10044
                               os_str by # :  None
                               Linux :        None
                               POSIX :        None
                               WinS :         Socket type not supported. The support for the specified socket type does not exist in this address family. For example, the optional type SOCK_RAW might be selected in a socket call, and the implementation does not support SOCK_RAW sockets at all.

         WSAESTALE          :  errno :        10070
                               os_str by # :  None
                               Linux :        None
                               POSIX :        None
                               WinS :         Stale file handle reference. The file handle reference is no longer available.

        WSAETIMEDOUT        :  errno :        10060
                               os_str by # :  None
                               Linux :        None
                               POSIX :        None
                               WinS :         Connection timed out. A connection attempt failed because the connected party did not properly respond after a period of time, or the established connection failed because the connected host has failed to respond.

      WSAETOOMANYREFS       :  errno :        10059
                               os_str by # :  None
                               Linux :        None
                               POSIX :        None
                               WinS :         Too many references. Too many references to some kernel object.

         WSAEUSERS          :  errno :        10068
                               os_str by # :  None
                               Linux :        None
                               POSIX :        None
                               WinS :         User quota exceeded. Ran out of user quota.

       WSAEWOULDBLOCK       :  errno :        10035
                               os_str by # :  None
                               Linux :        None
                               POSIX :        None
                               WinS :         Resource temporarily unavailable. This error is returned from operations on nonblocking sockets that cannot be completed immediately, for example recv when no data is queued to be read from the socket. It is a nonfatal error, and the operation should be retried later. It is normal for WSAEWOULDBLOCK to be reported as the result from calling connect on a nonblocking SOCK_STREAM socket, since some time must elapse for the connection to be established.

     WSAHOST_NOT_FOUND      :  errno :        -
                               os_str by # :  ? (see below)
                               Linux :        None
                               POSIX :        None
                               WinS :         Host not found. No such host is known. The name is not an official host name or alias, or it cannot be found in the database(s) being queried. This error may also be returned for protocol and service queries, and means that the specified name could not be found in the relevant database.

     WSANOTINITIALISED      :  errno :        10093
                               os_str by # :  None
                               Linux :        None
                               POSIX :        None
                               WinS :         Successful WSAStartup not yet performed. Either the application has not called WSAStartup or WSAStartup failed. The application may be accessing a socket that the current active task does not own (that is, trying to share a socket between tasks), or WSACleanup has been called too many times.

         WSANO_DATA         :  errno :        -
                               os_str by # :  ? (see below)
                               Linux :        None
                               POSIX :        None
                               WinS :         Valid name, no data record of requested type. The requested name is valid and was found in the database, but it does not have the correct associated data being resolved for. The usual example for this is a host name-to-address translation attempt (using gethostbyname or WSAAsyncGetHostByName) which uses the DNS (Domain Name Server). An MX record is returned but no A record—indicating the host itself exists, but is not directly reachable.

       WSANO_RECOVERY       :  errno :        -
                               os_str by # :  ? (see below)
                               Linux :        None
                               POSIX :        None
                               WinS :         This is a nonrecoverable error. This indicates that some sort of nonrecoverable error occurred during a database lookup. This may be because the database files (for example, BSD-compatible HOSTS, SERVICES, or PROTOCOLS files) could not be found, or a DNS request was returned by the server with a severe error.

    WSASERVICE_NOT_FOUND    :  errno :        -
                               os_str by # :  ? (see below)
                               Linux :        None
                               POSIX :        None
                               WinS :         Service not found. No such service is known. The service cannot be found in the specified name space.

     WSASYSCALLFAILURE      :  errno :        -
                               os_str by # :  ? (see below)
                               Linux :        None
                               POSIX :        None
                               WinS :         System call failure. A system call that should never fail has failed. This is a generic error code, returned under various conditions. Returned when a system call that should never fail does fail. For example, if a call to WaitForMultipleEvents fails or one of the registry functions fails trying to manipulate the protocol/namespace catalogs. Returned when a provider does not return SUCCESS and does not provide an extended error code. Can indicate a service provider implementation error.

       WSASYSNOTREADY       :  errno :        10091
                               os_str by # :  None
                               Linux :        None
                               POSIX :        None
                               WinS :         Network subsystem is unavailable. This error is returned by WSAStartup if the Windows Sockets implementation cannot function at this time because the underlying system it uses to provide network services is currently unavailable. Users should check: That the appropriate Windows Sockets DLL file is in the current path. That they are not trying to use more than one Windows Sockets implementation simultaneously. If there is more than one Winsock DLL on your system, be sure the first one in the path is appropriate for the network subsystem currently loaded. The Windows Sockets implementation documentation to be sure all necessary components are currently installed and configured correctly.

        WSATRY_AGAIN        :  errno :        -
                               os_str by # :  ? (see below)
                               Linux :        None
                               POSIX :        None
                               WinS :         Nonauthoritative host not found. This is usually a temporary error during host name resolution and means that the local server did not receive a response from an authoritative server. A retry at some time later may be successful.

     WSATYPE_NOT_FOUND      :  errno :        -
                               os_str by # :  ? (see below)
                               Linux :        None
                               POSIX :        None
                               WinS :         Class type not found. The specified class was not found.

     WSAVERNOTSUPPORTED     :  errno :        10092
                               os_str by # :  None
                               Linux :        None
                               POSIX :        None
                               WinS :         Winsock.dll version out of range. The current Windows Sockets implementation does not support the Windows Sockets specification version requested by the application. Check that no old Windows Sockets DLL files are being accessed.

      WSA_E_CANCELLED       :  errno :        -
                               os_str by # :  ? (see below)
                               Linux :        None
                               POSIX :        None
                               WinS :         Call was canceled. A call to the WSALookupServiceEnd function was made while this call was still processing. The call has been canceled.

       WSA_E_NO_MORE        :  errno :        -
                               os_str by # :  ? (see below)
                               Linux :        None
                               POSIX :        None
                               WinS :         No more results. No more results can be returned by the WSALookupServiceNext function.

     WSA_INVALID_HANDLE     :  errno :        -
                               os_str by # :  ? (see below)
                               Linux :        None
                               POSIX :        None
                               WinS :         Specified event object handle is invalid. An application attempts to use an event object, but the specified handle is not valid.

   WSA_INVALID_PARAMETER    :  errno :        -
                               os_str by # :  ? (see below)
                               Linux :        None
                               POSIX :        None
                               WinS :         One or more parameters are invalid. An application used a Windows Sockets function which directly maps to a Windows function. The Windows function is indicating a problem with one or more parameters.

     WSA_IO_INCOMPLETE      :  errno :        -
                               os_str by # :  ? (see below)
                               Linux :        None
                               POSIX :        None
                               WinS :         Overlapped I/O event object not in signaled state. The application has tried to determine the status of an overlapped operation which is not yet completed. Applications that use WSAGetOverlappedResult (with the fWait flag set to FALSE) in a polling mode to determine when an overlapped operation has completed, get this error code until the operation is complete.

       WSA_IO_PENDING       :  errno :        -
                               os_str by # :  ? (see below)
                               Linux :        None
                               POSIX :        None
                               WinS :         Overlapped operations will complete later. The application has initiated an overlapped operation that cannot be completed immediately. A completion indication will be given later when the operation has been completed.

   WSA_NOT_ENOUGH_MEMORY    :  errno :        -
                               os_str by # :  ? (see below)
                               Linux :        None
                               POSIX :        None
                               WinS :         Insufficient memory available. An application used a Windows Sockets function that directly maps to a Windows function. The Windows function is indicating a lack of required memory resources.

   WSA_OPERATION_ABORTED    :  errno :        -
                               os_str by # :  ? (see below)
                               Linux :        None
                               POSIX :        None
                               WinS :         Overlapped operation aborted. An overlapped operation was canceled due to the closure of the socket, or the execution of the SIO_FLUSH command in WSAIoctl.

 WSA_QOS_ADMISSION_FAILURE  :  errno :        -
                               os_str by # :  ? (see below)
                               Linux :        None
                               POSIX :        None
                               WinS :         QoS admission error. A QoS error occurred due to lack of resources.

     WSA_QOS_BAD_OBJECT     :  errno :        -
                               os_str by # :  ? (see below)
                               Linux :        None
                               POSIX :        None
                               WinS :         QoS bad object. A problem was encountered with some part of the filterspec or the provider-specific buffer in general.

     WSA_QOS_BAD_STYLE      :  errno :        -
                               os_str by # :  ? (see below)
                               Linux :        None
                               POSIX :        None
                               WinS :         QoS bad style. An unknown or conflicting QoS style was encountered.

    WSA_QOS_EFILTERCOUNT    :  errno :        -
                               os_str by # :  ? (see below)
                               Linux :        None
                               POSIX :        None
                               WinS :         Incorrect QoS filter count. An incorrect number of QoS FILTERSPECs were specified in the FLOWDESCRIPTOR.

    WSA_QOS_EFILTERSTYLE    :  errno :        -
                               os_str by # :  ? (see below)
                               Linux :        None
                               POSIX :        None
                               WinS :         Invalid QoS filter style. An invalid QoS filter style was used.

    WSA_QOS_EFILTERTYPE     :  errno :        -
                               os_str by # :  ? (see below)
                               Linux :        None
                               POSIX :        None
                               WinS :         Invalid QoS filter type. An invalid QoS filter type was used.

     WSA_QOS_EFLOWCOUNT     :  errno :        -
                               os_str by # :  ? (see below)
                               Linux :        None
                               POSIX :        None
                               WinS :         Incorrect QoS flow count. An incorrect number of flow descriptors was specified in the QoS structure.

     WSA_QOS_EFLOWDESC      :  errno :        -
                               os_str by # :  ? (see below)
                               Linux :        None
                               POSIX :        None
                               WinS :         Invalid QoS flow descriptor. An invalid QoS flow descriptor was found in the flow descriptor list.

     WSA_QOS_EFLOWSPEC      :  errno :        -
                               os_str by # :  ? (see below)
                               Linux :        None
                               POSIX :        None
                               WinS :         QoS flowspec error. An invalid or inconsistent flowspec was found in the QOS structure.

     WSA_QOS_EOBJLENGTH     :  errno :        -
                               os_str by # :  ? (see below)
                               Linux :        None
                               POSIX :        None
                               WinS :         Invalid QoS object length. An object with an invalid ObjectLength field was specified in the QoS provider-specific buffer.

     WSA_QOS_EPOLICYOBJ     :  errno :        -
                               os_str by # :  ? (see below)
                               Linux :        None
                               POSIX :        None
                               WinS :         Invalid QoS policy object. An invalid policy object was found in the QoS provider-specific buffer.

    WSA_QOS_EPROVSPECBUF    :  errno :        -
                               os_str by # :  ? (see below)
                               Linux :        None
                               POSIX :        None
                               WinS :         Invalid QoS provider buffer. An invalid QoS provider-specific buffer.

   WSA_QOS_EPSFILTERSPEC    :  errno :        -
                               os_str by # :  ? (see below)
                               Linux :        None
                               POSIX :        None
                               WinS :         Invalid QoS provider-specific filterspec. An invalid FILTERSPEC was found in the QoS provider-specific buffer.

    WSA_QOS_EPSFLOWSPEC     :  errno :        -
                               os_str by # :  ? (see below)
                               Linux :        None
                               POSIX :        None
                               WinS :         Invalid QoS provider-specific flowspec. An invalid or inconsistent flowspec was found in the QoS provider-specific buffer.

     WSA_QOS_ESDMODEOBJ     :  errno :        -
                               os_str by # :  ? (see below)
                               Linux :        None
                               POSIX :        None
                               WinS :         Invalid QoS shape discard mode object. An invalid shape discard mode object was found in the QoS provider-specific buffer.

    WSA_QOS_ESERVICETYPE    :  errno :        -
                               os_str by # :  ? (see below)
                               Linux :        None
                               POSIX :        None
                               WinS :         QoS service type error. An invalid or unrecognized service type was found in the QoS flowspec.

   WSA_QOS_ESHAPERATEOBJ    :  errno :        -
                               os_str by # :  ? (see below)
                               Linux :        None
                               POSIX :        None
                               WinS :         Invalid QoS shaping rate object. An invalid shaping rate object was found in the QoS provider-specific buffer.

    WSA_QOS_EUNKOWNPSOBJ    :  errno :        -
                               os_str by # :  ? (see below)
                               Linux :        None
                               POSIX :        None
                               WinS :         Unrecognized QoS object. An unrecognized object was found in the QoS provider-specific buffer.

   WSA_QOS_GENERIC_ERROR    :  errno :        -
                               os_str by # :  ? (see below)
                               Linux :        None
                               POSIX :        None
                               WinS :         QoS generic error. A general QoS error.

    WSA_QOS_NO_RECEIVERS    :  errno :        -
                               os_str by # :  ? (see below)
                               Linux :        None
                               POSIX :        None
                               WinS :         QoS no receivers. There are no QoS receivers.

     WSA_QOS_NO_SENDERS     :  errno :        -
                               os_str by # :  ? (see below)
                               Linux :        None
                               POSIX :        None
                               WinS :         No QoS senders. There are no QoS senders.

   WSA_QOS_POLICY_FAILURE   :  errno :        -
                               os_str by # :  ? (see below)
                               Linux :        None
                               POSIX :        None
                               WinS :         QoS policy failure. The QoS request was rejected because the policy system couldn-t allocate the requested resource within the existing policy.

     WSA_QOS_RECEIVERS      :  errno :        -
                               os_str by # :  ? (see below)
                               Linux :        None
                               POSIX :        None
                               WinS :         QoS receivers. At least one QoS reserve has arrived.

 WSA_QOS_REQUEST_CONFIRMED  :  errno :        -
                               os_str by # :  ? (see below)
                               Linux :        None
                               POSIX :        None
                               WinS :         QoS request confirmed. The QoS reserve request has been confirmed.

  WSA_QOS_RESERVED_PETYPE   :  errno :        -
                               os_str by # :  ? (see below)
                               Linux :        None
                               POSIX :        None
                               WinS :         Reserved policy QoS element type. A reserved policy element was found in the QoS provider-specific buffer.

      WSA_QOS_SENDERS       :  errno :        -
                               os_str by # :  ? (see below)
                               Linux :        None
                               POSIX :        None
                               WinS :         QoS senders. At least one QoS send path has arrived.

 WSA_QOS_TRAFFIC_CTRL_ERROR :  errno :        -
                               os_str by # :  ? (see below)
                               Linux :        None
                               POSIX :        None
                               WinS :         QoS traffic control error. An error with the underlying traffic control (TC) API as the generic QoS request was converted for local enforcement by the TC API. This could be due to an out of memory error or to an internal QoS provider error.




--------------------------------------------------------------
comparison of different sources (for numeric codes of errors):
'errno' - from  errno.errorcode
'os_str' - from  os.strerror
             0              :  errno :   None                          os_str :  No error

             1              :  errno :   EPERM                         os_str :  Operation not permitted

             2              :  errno :   ENOENT                        os_str :  No such file or directory

             3              :  errno :   ESRCH                         os_str :  No such process

             4              :  errno :   EINTR                         os_str :  Interrupted function call

             5              :  errno :   EIO                           os_str :  Input/output error

             6              :  errno :   ENXIO                         os_str :  No such device or address

             7              :  errno :   E2BIG                         os_str :  Arg list too long

             8              :  errno :   ENOEXEC                       os_str :  Exec format error

             9              :  errno :   EBADF                         os_str :  Bad file descriptor

             10             :  errno :   ECHILD                        os_str :  No child processes

             11             :  errno :   EAGAIN                        os_str :  Resource temporarily unavailable

             12             :  errno :   ENOMEM                        os_str :  Not enough space

             13             :  errno :   EACCES                        os_str :  Permission denied

             14             :  errno :   EFAULT                        os_str :  Bad address

             16             :  errno :   EBUSY                         os_str :  Resource device

             17             :  errno :   EEXIST                        os_str :  File exists

             18             :  errno :   EXDEV                         os_str :  Improper link

             19             :  errno :   ENODEV                        os_str :  No such device

             20             :  errno :   ENOTDIR                       os_str :  Not a directory

             21             :  errno :   EISDIR                        os_str :  Is a directory

             22             :  errno :   EINVAL                        os_str :  Invalid argument

             23             :  errno :   ENFILE                        os_str :  Too many open files in system

             24             :  errno :   EMFILE                        os_str :  Too many open files

             25             :  errno :   ENOTTY                        os_str :  Inappropriate I/O control operation

             27             :  errno :   EFBIG                         os_str :  File too large

             28             :  errno :   ENOSPC                        os_str :  No space left on device

             29             :  errno :   ESPIPE                        os_str :  Invalid seek

             30             :  errno :   EROFS                         os_str :  Read-only file system

             31             :  errno :   EMLINK                        os_str :  Too many links

             32             :  errno :   EPIPE                         os_str :  Broken pipe

             33             :  errno :   EDOM                          os_str :  Domain error

             34             :  errno :   ERANGE                        os_str :  Result too large

             36             :  errno :   EDEADLOCK                     os_str :  Resource deadlock avoided

             38             :  errno :   ENAMETOOLONG                  os_str :  Filename too long

             39             :  errno :   ENOLCK                        os_str :  No locks available

             40             :  errno :   ENOSYS                        os_str :  Function not implemented

             41             :  errno :   ENOTEMPTY                     os_str :  Directory not empty

             42             :  errno :   EILSEQ                        os_str :  Illegal byte sequence

            100             :  errno :   None                          os_str :  address in use

            101             :  errno :   None                          os_str :  address not available

            102             :  errno :   None                          os_str :  address family not supported

            103             :  errno :   None                          os_str :  connection already in progress

            104             :  errno :   EBADMSG                       os_str :  bad message

            105             :  errno :   ECANCELED                     os_str :  operation canceled

            106             :  errno :   None                          os_str :  connection aborted

            107             :  errno :   None                          os_str :  connection refused

            108             :  errno :   None                          os_str :  connection reset

            109             :  errno :   None                          os_str :  destination address required

            110             :  errno :   None                          os_str :  host unreachable

            111             :  errno :   EIDRM                         os_str :  identifier removed

            112             :  errno :   None                          os_str :  operation in progress

            113             :  errno :   None                          os_str :  already connected

            114             :  errno :   None                          os_str :  too many symbolic link levels

            115             :  errno :   None                          os_str :  message size

            116             :  errno :   None                          os_str :  network down

            117             :  errno :   None                          os_str :  network reset

            118             :  errno :   None                          os_str :  network unreachable

            119             :  errno :   None                          os_str :  no buffer space

            120             :  errno :   ENODATA                       os_str :  no message available

            121             :  errno :   ENOLINK                       os_str :  no link

            122             :  errno :   ENOMSG                        os_str :  no message

            123             :  errno :   None                          os_str :  no protocol option

            124             :  errno :   ENOSR                         os_str :  no stream resources

            125             :  errno :   ENOSTR                        os_str :  not a stream

            126             :  errno :   None                          os_str :  not connected

            127             :  errno :   ENOTRECOVERABLE               os_str :  state not recoverable

            128             :  errno :   None                          os_str :  not a socket

            129             :  errno :   ENOTSUP                       os_str :  not supported

            130             :  errno :   None                          os_str :  operation not supported

            132             :  errno :   EOVERFLOW                     os_str :  value too large

            133             :  errno :   EOWNERDEAD                    os_str :  owner dead

            134             :  errno :   EPROTO                        os_str :  protocol error

            135             :  errno :   None                          os_str :  protocol not supported

            136             :  errno :   None                          os_str :  wrong protocol type

            137             :  errno :   ETIME                         os_str :  stream timeout

            138             :  errno :   None                          os_str :  timed out

            139             :  errno :   ETXTBSY                       os_str :  text file busy

            140             :  errno :   None                          os_str :  operation would block

           10000            :  errno :   WSABASEERR                    os_str :  Unknown error

           10004            :  errno :   WSAEINTR                      os_str :  Unknown error

           10009            :  errno :   WSAEBADF                      os_str :  Unknown error

           10013            :  errno :   WSAEACCES                     os_str :  Unknown error

           10014            :  errno :   WSAEFAULT                     os_str :  Unknown error

           10022            :  errno :   WSAEINVAL                     os_str :  Unknown error

           10024            :  errno :   WSAEMFILE                     os_str :  Unknown error

           10035            :  errno :   WSAEWOULDBLOCK                os_str :  Unknown error

           10036            :  errno :   WSAEINPROGRESS                os_str :  Unknown error

           10037            :  errno :   WSAEALREADY                   os_str :  Unknown error

           10038            :  errno :   WSAENOTSOCK                   os_str :  Unknown error

           10039            :  errno :   WSAEDESTADDRREQ               os_str :  Unknown error

           10040            :  errno :   WSAEMSGSIZE                   os_str :  Unknown error

           10041            :  errno :   WSAEPROTOTYPE                 os_str :  Unknown error

           10042            :  errno :   WSAENOPROTOOPT                os_str :  Unknown error

           10043            :  errno :   WSAEPROTONOSUPPORT            os_str :  Unknown error

           10044            :  errno :   WSAESOCKTNOSUPPORT            os_str :  Unknown error

           10045            :  errno :   WSAEOPNOTSUPP                 os_str :  Unknown error

           10046            :  errno :   WSAEPFNOSUPPORT               os_str :  Unknown error

           10047            :  errno :   WSAEAFNOSUPPORT               os_str :  Unknown error

           10048            :  errno :   WSAEADDRINUSE                 os_str :  Unknown error

           10049            :  errno :   WSAEADDRNOTAVAIL              os_str :  Unknown error

           10050            :  errno :   WSAENETDOWN                   os_str :  Unknown error

           10051            :  errno :   WSAENETUNREACH                os_str :  Unknown error

           10052            :  errno :   WSAENETRESET                  os_str :  Unknown error

           10053            :  errno :   WSAECONNABORTED               os_str :  Unknown error

           10054            :  errno :   WSAECONNRESET                 os_str :  Unknown error

           10055            :  errno :   WSAENOBUFS                    os_str :  Unknown error

           10056            :  errno :   WSAEISCONN                    os_str :  Unknown error

           10057            :  errno :   WSAENOTCONN                   os_str :  Unknown error

           10058            :  errno :   WSAESHUTDOWN                  os_str :  Unknown error

           10059            :  errno :   WSAETOOMANYREFS               os_str :  Unknown error

           10060            :  errno :   WSAETIMEDOUT                  os_str :  Unknown error

           10061            :  errno :   WSAECONNREFUSED               os_str :  Unknown error

           10062            :  errno :   WSAELOOP                      os_str :  Unknown error

           10063            :  errno :   WSAENAMETOOLONG               os_str :  Unknown error

           10064            :  errno :   WSAEHOSTDOWN                  os_str :  Unknown error

           10065            :  errno :   WSAEHOSTUNREACH               os_str :  Unknown error

           10066            :  errno :   WSAENOTEMPTY                  os_str :  Unknown error

           10067            :  errno :   WSAEPROCLIM                   os_str :  Unknown error

           10068            :  errno :   WSAEUSERS                     os_str :  Unknown error

           10069            :  errno :   WSAEDQUOT                     os_str :  Unknown error

           10070            :  errno :   WSAESTALE                     os_str :  Unknown error

           10071            :  errno :   WSAEREMOTE                    os_str :  Unknown error

           10091            :  errno :   WSASYSNOTREADY                os_str :  Unknown error

           10092            :  errno :   WSAVERNOTSUPPORTED            os_str :  Unknown error

           10093            :  errno :   WSANOTINITIALISED             os_str :  Unknown error

           10101            :  errno :   WSAEDISCON                    os_str :  Unknown error
```
