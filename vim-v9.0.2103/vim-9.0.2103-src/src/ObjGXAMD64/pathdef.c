/* pathdef.c */ 
#include "vim.h" 
char_u *default_vim_dir = (char_u *)""; 
char_u *default_vimruntime_dir = (char_u *)""; 
char_u *all_cflags = (char_u *)"cl -c /W3 /GF /nologo -I. -Iproto -DHAVE_PATHDEF -DWIN32 -DHAVE_STDINT_H  -DFEAT_CSCOPE -DFEAT_TERMINAL -DFEAT_SOUND -DFEAT_NETBEANS_INTG -DFEAT_JOB_CHANNEL -DFEAT_IPV6 -DHAVE_INET_NTOP   -DFEAT_XPM_W32     -DWINVER=0x0601 -D_WIN32_WINNT=0x0601  /source-charset:utf-8 /MP /Ox /GL -DNDEBUG  /Zl /MT /D_CRT_SECURE_NO_DEPRECATE /D_CRT_NONSTDC_NO_DEPRECATE -DFEAT_MBYTE_IME -DDYNAMIC_IME -DFEAT_GUI_MSWIN -DFEAT_DIRECTX -DDYNAMIC_DIRECTX -DFEAT_DIRECTX_COLOR_EMOJI -DDYNAMIC_ICONV -DDYNAMIC_GETTEXT -DFEAT_HUGE /Fd.\\ObjGXAMD64/ /Zi"; 
char_u *all_lflags = (char_u *)"link /nologo /opt:ref /LTCG:STATUS /HIGHENTROPYVA:NO oldnames.lib kernel32.lib advapi32.lib shell32.lib gdi32.lib  comdlg32.lib ole32.lib netapi32.lib uuid.lib user32.lib  /machine:AMD64 version.lib  winspool.lib comctl32.lib libcmt.lib           winmm.lib Ws2_32.lib xpm\\x64\\lib-vc14\\libXpm.lib  /PDB:gvim.pdb -debug"; 
char_u *compiled_user = (char_u *)"hui74"; 
char_u *compiled_sys = (char_u *)"DESKTOP-JFH902A"; 
