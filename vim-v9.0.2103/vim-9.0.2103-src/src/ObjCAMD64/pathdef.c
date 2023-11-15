/* pathdef.c */ 
#include "vim.h" 
char_u *default_vim_dir = (char_u *)""; 
char_u *default_vimruntime_dir = (char_u *)""; 
char_u *all_cflags = (char_u *)"cl -c /W3 /GF /nologo -I. -Iproto -DHAVE_PATHDEF -DWIN32 -DHAVE_STDINT_H  -DFEAT_CSCOPE -DFEAT_TERMINAL -DFEAT_SOUND  -DFEAT_JOB_CHANNEL -DFEAT_IPV6 -DHAVE_INET_NTOP        -DWINVER=0x0601 -D_WIN32_WINNT=0x0601  /source-charset:utf-8 /MP /Ox /GL -DNDEBUG  /Zl /MT /D_CRT_SECURE_NO_DEPRECATE /D_CRT_NONSTDC_NO_DEPRECATE -DFEAT_MBYTE_IME -DDYNAMIC_IME -DDYNAMIC_ICONV -DDYNAMIC_GETTEXT -DFEAT_HUGE /Fd.\\ObjCAMD64/ /Zi"; 
char_u *all_lflags = (char_u *)"link /nologo /opt:ref /LTCG:STATUS oldnames.lib kernel32.lib advapi32.lib shell32.lib gdi32.lib  comdlg32.lib ole32.lib netapi32.lib uuid.lib user32.lib  /machine:AMD64  libcmt.lib           winmm.lib Ws2_32.lib   /PDB:vim.pdb -debug"; 
char_u *compiled_user = (char_u *)"hui74"; 
char_u *compiled_sys = (char_u *)"DESKTOP-JFH902A"; 
