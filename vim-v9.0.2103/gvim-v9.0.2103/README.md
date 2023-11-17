
HAVE_STDINT_H;FEAT_IPV6;HAVE_INET_NTOP;DYNAMIC_GETTEXT;FEAT_XPM_W32;FEAT_GUI_MSWIN;NDEBUG;WCWIDTH_FUNCTION=utf_uint2cells;DYNAMIC_DIRECTX;FEAT_NETBEANS_INTG;FEAT_SOUND;_WIN32_WINNT=0x0601;WIN32;FEAT_DIRECTX_COLOR_EMOJI;FEAT_HUGE;FEAT_JOB_CHANNEL;WINVER=0x0601;INLINE="";DYNAMIC_IME;SNPRINTF=vim_snprintf;HAVE_PATHDEF;FEAT_CSCOPE;DYNAMIC_ICONV;FEAT_TERMINAL;FEAT_MBYTE_IME;GET_SPECIAL_PTY_TYPE_FUNCTION=get_special_pty_type;_CRT_SECURE_NO_WARNINGS;IS_COMBINING_FUNCTION=utf_iscomposing_uint;VSNPRINTF=vim_vsnprintf;FEAT_DIRECTX


$(CoreLibraryDependencies);%(AdditionalDependencies);kernel32.lib;advapi32.lib;shell32.lib;user32.lib;uuid.lib;ole32.lib;comctl32.lib;gdi32.lib;oleaut32.lib;oldnames.lib;comdlg32.lib;netapi32.lib;winmm.lib;version.lib;imm32.lib;winspool.lib;ws2_32.lib;$(SolutionDir)vim-9.0.2103-src\src\xpm\$(LibrariesArchitecture)\lib-vc14\libXpm.lib


pathdef.c里面也有编译参数
char_u *all_cflags = (char_u *)"cl -c /W3 /GF /nologo -I. -Iproto -DHAVE_PATHDEF -DWIN32 -DHAVE_STDINT_H  -DFEAT_CSCOPE -DFEAT_TERMINAL -DFEAT_SOUND -DFEAT_NETBEANS_INTG -DFEAT_JOB_CHANNEL -DFEAT_IPV6 -DHAVE_INET_NTOP   -DFEAT_XPM_W32     -DWINVER=0x0601 -D_WIN32_WINNT=0x0601  /source-charset:utf-8 /MP /Ox /GL -DNDEBUG  /Zl /MT /D_CRT_SECURE_NO_DEPRECATE /D_CRT_NONSTDC_NO_DEPRECATE -DFEAT_MBYTE_IME -DDYNAMIC_IME -DFEAT_GUI_MSWIN -DFEAT_DIRECTX -DDYNAMIC_DIRECTX -DFEAT_DIRECTX_COLOR_EMOJI -DDYNAMIC_ICONV -DDYNAMIC_GETTEXT -DFEAT_HUGE /Fd.\\ObjGXAMD64/ /Zi"; 
char_u *all_lflags = (char_u *)"link /nologo /opt:ref /LTCG:STATUS /HIGHENTROPYVA:NO oldnames.lib kernel32.lib advapi32.lib shell32.lib gdi32.lib  comdlg32.lib ole32.lib netapi32.lib uuid.lib user32.lib  /machine:AMD64 version.lib  winspool.lib comctl32.lib libcmt.lib           winmm.lib Ws2_32.lib xpm\\x64\\lib-vc14\\libXpm.lib  /PDB:gvim.pdb -debug"; 


entry point: os_win32exe.c#L30#wWinMain()

main.c#L94#VimMain()


