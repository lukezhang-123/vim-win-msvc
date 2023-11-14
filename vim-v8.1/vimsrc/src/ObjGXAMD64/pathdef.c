/* pathdef.c */ 
#include "vim.h" 
char_u *default_vim_dir = (char_u *)""; 
char_u *default_vimruntime_dir = (char_u *)""; 
char_u *all_cflags = (char_u *)"cl -c /W3 /nologo  -I. -Iproto -DHAVE_PATHDEF -DWIN32  -DFEAT_CSCOPE -DFEAT_TERMINAL -DFEAT_NETBEANS_INTG -DFEAT_JOB_CHANNEL   -DFEAT_XPM_W32   -DWINVER=0x0501 -D_WIN32_WINNT=0x0501 /MP -DHAVE_STDINT_H /Ox /GL -DNDEBUG  /Zl /MT -DFEAT_GUI_W32 -DFEAT_DIRECTX -DDYNAMIC_DIRECTX -DFEAT_DIRECTX_COLOR_EMOJI -DDYNAMIC_ICONV -DDYNAMIC_GETTEXT -DFEAT_HUGE /Fd.\\ObjGXAMD64/ /Zi"; 
char_u *all_lflags = (char_u *)"link  /nologo /subsystem:windows /opt:ref /LTCG:STATUS /HIGHENTROPYVA:NO oldnames.lib kernel32.lib advapi32.lib shell32.lib gdi32.lib  comdlg32.lib ole32.lib uuid.lib /machine:AMD64 gdi32.lib version.lib   winspool.lib comctl32.lib advapi32.lib shell32.lib  /machine:AMD64  libcmt.lib  user32.lib          WSock32.lib xpm\\x64\\lib-vc14\\libXpm.lib /PDB:gvim.pdb -debug"; 
char_u *compiled_user = (char_u *)"hui"; 
char_u *compiled_sys = (char_u *)"DESKTOP-HQNCD2T"; 
