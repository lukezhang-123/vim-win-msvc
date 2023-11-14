vim console

vimsrc/src/INSTALLpc.txt

open open visual studio 2015 x64 native tools command prompt
nmake -f Make_mvc.mak

the make will generate some source file like pathdef.c, vim.res etc...,
and we can find out some makefile logic through the make output,
and the defined variable from the compile parameter -D which determine the real code logic.

from
all:	$(VIM).exe  ; from makefile
link  ... -out:vim.exe  ; from output
get the need source code

include path:
$(SolutionDir)vimsrc\src; $(SolutionDir)vimsrc\src\proto; $(SolutionDir)vimsrc\src\libvterm\include

c preprocessor #define variable arguments:
NDEBUG ;WINVER=0x0501 ;HAVE_STDINT_H ;_WIN32_WINNT=0x0501 ;_WIN32_WINNT=0x0600 ;FEAT_JOB_CHANNEL ;DYNAMIC_GETTEXT ;IS_COMBINING_FUNCTION=utf_iscomposing_uint ;DYNAMIC_ICONV ;HAVE_PATHDEF ;VSNPRINTF=vim_vsnprintf ;FEAT_HUGE ;INLINE="" ;WCWIDTH_FUNCTION=utf_uint2cells ;_CRT_SECURE_NO_WARNINGS ;USE_DYNFILEID ;FEAT_GETTEXT ;FEAT_CSCOPE ;FEAT_TERMINAL ;WIN32 

entry point: main.c#main()