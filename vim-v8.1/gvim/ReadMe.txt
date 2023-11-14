gvim  vim win32 gui

nmake -f Make_mvc.mak GUI=yes

include path:
$(SolutionDir)vimsrc\src; $(SolutionDir)vimsrc\src\proto; $(SolutionDir)vimsrc\src\libvterm\include; $(SolutionDir)vimsrc\src\xpm\include

c preprocessor #define variable arguments:
NDEBUG ;WINVER=0x0501 ;HAVE_STDINT_H ;DYNAMIC_DIRECTX ;_WIN32_WINNT=0x0501 ;FEAT_GUI_W32 ;FEAT_JOB_CHANNEL ;FEAT_XPM_W32 ;DYNAMIC_GETTEXT ;IS_COMBINING_FUNCTION=utf_iscomposing_uint ;DYNAMIC_ICONV ;FEAT_DIRECTX ;HAVE_PATHDEF ;VSNPRINTF=vim_vsnprintf ;FEAT_HUGE ;INLINE="" ;WCWIDTH_FUNCTION=utf_uint2cells ;_CRT_SECURE_NO_WARNINGS ;FEAT_NETBEANS_INTG ;FEAT_CSCOPE ;FEAT_TERMINAL ;FEAT_DIRECTX_COLOR_EMOJI ;WIN32

entry point: os_win32exe.c#WinMain()