# -*- coding: utf-8 -*-

nmake_log = r"""
D:\tmp\vim-9.0.2103\src>nmake -f Make_mvc.mak GUI=yes

Microsoft (R) 程序维护实用工具 14.37.32824.0 版
版权所有 (C) Microsoft Corporation。  保留所有权利。


        if not exist .\ObjGXAMD64/nul  mkdir .\ObjGXAMD64
creating .\ObjGXAMD64\pathdef.c
        cl -c /W3 /GF /nologo -I. -Iproto -DHAVE_PATHDEF -DWIN32 -DHAVE_STDINT_H  -DFEAT_CSCOPE -DFEAT_TERMINAL -DFEAT_SOUND -DFEAT_NETBEANS_INTG -DFEAT_JOB_CHANNEL -DFEAT_IPV6 -DHAVE_INET_NTOP   -DFEAT_XPM_W32     -DWINVER=0x0601 -D_WIN32_WINNT=0x0601  /source-charset:utf-8 /MP /Ox /GL -DNDEBUG  /Zl /MT /D_CRT_SECURE_NO_DEPRECATE /D_CRT_NONSTDC_NO_DEPRECATE -DFEAT_MBYTE_IME -DDYNAMIC_IME -DFEAT_GUI_MSWIN -DFEAT_DIRECTX -DDYNAMIC_DIRECTX -DFEAT_DIRECTX_COLOR_EMOJI -DDYNAMIC_ICONV -DDYNAMIC_GETTEXT -DFEAT_HUGE /Fd.\ObjGXAMD64/ /Zi /Fo.\ObjGXAMD64/ .\ObjGXAMD64\pathdef.c
pathdef.c
        rc /nologo /l 0x409 /Fo.\ObjGXAMD64/vim.res -DNDEBUG -DFEAT_GUI_MSWIN vim.rc
        cl -c /W3 /GF /nologo -I. -Iproto -DHAVE_PATHDEF -DWIN32 -DHAVE_STDINT_H  -DFEAT_CSCOPE -DFEAT_TERMINAL -DFEAT_SOUND -DFEAT_NETBEANS_INTG -DFEAT_JOB_CHANNEL -DFEAT_IPV6 -DHAVE_INET_NTOP   -DFEAT_XPM_W32     -DWINVER=0x0601 -D_WIN32_WINNT=0x0601  /source-charset:utf-8 /MP /Ox /GL -DNDEBUG  /Zl /MT /D_CRT_SECURE_NO_DEPRECATE /D_CRT_NONSTDC_NO_DEPRECATE -DFEAT_MBYTE_IME -DDYNAMIC_IME -DFEAT_GUI_MSWIN -DFEAT_DIRECTX -DDYNAMIC_DIRECTX -DFEAT_DIRECTX_COLOR_EMOJI -DDYNAMIC_ICONV -DDYNAMIC_GETTEXT -DFEAT_HUGE /Fd.\ObjGXAMD64/ /Zi -Ilibvterm/include -DINLINE=""  -DVSNPRINTF=vim_vsnprintf  -DSNPRINTF=vim_snprintf  -DIS_COMBINING_FUNCTION=utf_iscomposing_uint  -DWCWIDTH_FUNCTION=utf_uint2cells  -DGET_SPECIAL_PTY_TYPE_FUNCTION=get_special_pty_type  -D_CRT_SECURE_NO_WARNINGS /Fo.\ObjGXAMD64/vterm_encoding.obj libvterm/src/encoding.c
encoding.c
        cl -c /W3 /GF /nologo -I. -Iproto -DHAVE_PATHDEF -DWIN32 -DHAVE_STDINT_H  -DFEAT_CSCOPE -DFEAT_TERMINAL -DFEAT_SOUND -DFEAT_NETBEANS_INTG -DFEAT_JOB_CHANNEL -DFEAT_IPV6 -DHAVE_INET_NTOP   -DFEAT_XPM_W32     -DWINVER=0x0601 -D_WIN32_WINNT=0x0601  /source-charset:utf-8 /MP /Ox /GL -DNDEBUG  /Zl /MT /D_CRT_SECURE_NO_DEPRECATE /D_CRT_NONSTDC_NO_DEPRECATE -DFEAT_MBYTE_IME -DDYNAMIC_IME -DFEAT_GUI_MSWIN -DFEAT_DIRECTX -DDYNAMIC_DIRECTX -DFEAT_DIRECTX_COLOR_EMOJI -DDYNAMIC_ICONV -DDYNAMIC_GETTEXT -DFEAT_HUGE /Fd.\ObjGXAMD64/ /Zi -Ilibvterm/include -DINLINE=""  -DVSNPRINTF=vim_vsnprintf  -DSNPRINTF=vim_snprintf  -DIS_COMBINING_FUNCTION=utf_iscomposing_uint  -DWCWIDTH_FUNCTION=utf_uint2cells  -DGET_SPECIAL_PTY_TYPE_FUNCTION=get_special_pty_type  -D_CRT_SECURE_NO_WARNINGS /Fo.\ObjGXAMD64/vterm_keyboard.obj libvterm/src/keyboard.c
keyboard.c
        cl -c /W3 /GF /nologo -I. -Iproto -DHAVE_PATHDEF -DWIN32 -DHAVE_STDINT_H  -DFEAT_CSCOPE -DFEAT_TERMINAL -DFEAT_SOUND -DFEAT_NETBEANS_INTG -DFEAT_JOB_CHANNEL -DFEAT_IPV6 -DHAVE_INET_NTOP   -DFEAT_XPM_W32     -DWINVER=0x0601 -D_WIN32_WINNT=0x0601  /source-charset:utf-8 /MP /Ox /GL -DNDEBUG  /Zl /MT /D_CRT_SECURE_NO_DEPRECATE /D_CRT_NONSTDC_NO_DEPRECATE -DFEAT_MBYTE_IME -DDYNAMIC_IME -DFEAT_GUI_MSWIN -DFEAT_DIRECTX -DDYNAMIC_DIRECTX -DFEAT_DIRECTX_COLOR_EMOJI -DDYNAMIC_ICONV -DDYNAMIC_GETTEXT -DFEAT_HUGE /Fd.\ObjGXAMD64/ /Zi -Ilibvterm/include -DINLINE=""  -DVSNPRINTF=vim_vsnprintf  -DSNPRINTF=vim_snprintf  -DIS_COMBINING_FUNCTION=utf_iscomposing_uint  -DWCWIDTH_FUNCTION=utf_uint2cells  -DGET_SPECIAL_PTY_TYPE_FUNCTION=get_special_pty_type  -D_CRT_SECURE_NO_WARNINGS /Fo.\ObjGXAMD64/vterm_mouse.obj libvterm/src/mouse.c
mouse.c
        cl -c /W3 /GF /nologo -I. -Iproto -DHAVE_PATHDEF -DWIN32 -DHAVE_STDINT_H  -DFEAT_CSCOPE -DFEAT_TERMINAL -DFEAT_SOUND -DFEAT_NETBEANS_INTG -DFEAT_JOB_CHANNEL -DFEAT_IPV6 -DHAVE_INET_NTOP   -DFEAT_XPM_W32     -DWINVER=0x0601 -D_WIN32_WINNT=0x0601  /source-charset:utf-8 /MP /Ox /GL -DNDEBUG  /Zl /MT /D_CRT_SECURE_NO_DEPRECATE /D_CRT_NONSTDC_NO_DEPRECATE -DFEAT_MBYTE_IME -DDYNAMIC_IME -DFEAT_GUI_MSWIN -DFEAT_DIRECTX -DDYNAMIC_DIRECTX -DFEAT_DIRECTX_COLOR_EMOJI -DDYNAMIC_ICONV -DDYNAMIC_GETTEXT -DFEAT_HUGE /Fd.\ObjGXAMD64/ /Zi -Ilibvterm/include -DINLINE=""  -DVSNPRINTF=vim_vsnprintf  -DSNPRINTF=vim_snprintf  -DIS_COMBINING_FUNCTION=utf_iscomposing_uint  -DWCWIDTH_FUNCTION=utf_uint2cells  -DGET_SPECIAL_PTY_TYPE_FUNCTION=get_special_pty_type  -D_CRT_SECURE_NO_WARNINGS /Fo.\ObjGXAMD64/vterm_parser.obj libvterm/src/parser.c
parser.c
        cl -c /W3 /GF /nologo -I. -Iproto -DHAVE_PATHDEF -DWIN32 -DHAVE_STDINT_H  -DFEAT_CSCOPE -DFEAT_TERMINAL -DFEAT_SOUND -DFEAT_NETBEANS_INTG -DFEAT_JOB_CHANNEL -DFEAT_IPV6 -DHAVE_INET_NTOP   -DFEAT_XPM_W32     -DWINVER=0x0601 -D_WIN32_WINNT=0x0601  /source-charset:utf-8 /MP /Ox /GL -DNDEBUG  /Zl /MT /D_CRT_SECURE_NO_DEPRECATE /D_CRT_NONSTDC_NO_DEPRECATE -DFEAT_MBYTE_IME -DDYNAMIC_IME -DFEAT_GUI_MSWIN -DFEAT_DIRECTX -DDYNAMIC_DIRECTX -DFEAT_DIRECTX_COLOR_EMOJI -DDYNAMIC_ICONV -DDYNAMIC_GETTEXT -DFEAT_HUGE /Fd.\ObjGXAMD64/ /Zi -Ilibvterm/include -DINLINE=""  -DVSNPRINTF=vim_vsnprintf  -DSNPRINTF=vim_snprintf  -DIS_COMBINING_FUNCTION=utf_iscomposing_uint  -DWCWIDTH_FUNCTION=utf_uint2cells  -DGET_SPECIAL_PTY_TYPE_FUNCTION=get_special_pty_type  -D_CRT_SECURE_NO_WARNINGS /Fo.\ObjGXAMD64/vterm_pen.obj libvterm/src/pen.c
pen.c
        cl -c /W3 /GF /nologo -I. -Iproto -DHAVE_PATHDEF -DWIN32 -DHAVE_STDINT_H  -DFEAT_CSCOPE -DFEAT_TERMINAL -DFEAT_SOUND -DFEAT_NETBEANS_INTG -DFEAT_JOB_CHANNEL -DFEAT_IPV6 -DHAVE_INET_NTOP   -DFEAT_XPM_W32     -DWINVER=0x0601 -D_WIN32_WINNT=0x0601  /source-charset:utf-8 /MP /Ox /GL -DNDEBUG  /Zl /MT /D_CRT_SECURE_NO_DEPRECATE /D_CRT_NONSTDC_NO_DEPRECATE -DFEAT_MBYTE_IME -DDYNAMIC_IME -DFEAT_GUI_MSWIN -DFEAT_DIRECTX -DDYNAMIC_DIRECTX -DFEAT_DIRECTX_COLOR_EMOJI -DDYNAMIC_ICONV -DDYNAMIC_GETTEXT -DFEAT_HUGE /Fd.\ObjGXAMD64/ /Zi -Ilibvterm/include -DINLINE=""  -DVSNPRINTF=vim_vsnprintf  -DSNPRINTF=vim_snprintf  -DIS_COMBINING_FUNCTION=utf_iscomposing_uint  -DWCWIDTH_FUNCTION=utf_uint2cells  -DGET_SPECIAL_PTY_TYPE_FUNCTION=get_special_pty_type  -D_CRT_SECURE_NO_WARNINGS /Fo.\ObjGXAMD64/vterm_screen.obj libvterm/src/screen.c
screen.c
        cl -c /W3 /GF /nologo -I. -Iproto -DHAVE_PATHDEF -DWIN32 -DHAVE_STDINT_H  -DFEAT_CSCOPE -DFEAT_TERMINAL -DFEAT_SOUND -DFEAT_NETBEANS_INTG -DFEAT_JOB_CHANNEL -DFEAT_IPV6 -DHAVE_INET_NTOP   -DFEAT_XPM_W32     -DWINVER=0x0601 -D_WIN32_WINNT=0x0601  /source-charset:utf-8 /MP /Ox /GL -DNDEBUG  /Zl /MT /D_CRT_SECURE_NO_DEPRECATE /D_CRT_NONSTDC_NO_DEPRECATE -DFEAT_MBYTE_IME -DDYNAMIC_IME -DFEAT_GUI_MSWIN -DFEAT_DIRECTX -DDYNAMIC_DIRECTX -DFEAT_DIRECTX_COLOR_EMOJI -DDYNAMIC_ICONV -DDYNAMIC_GETTEXT -DFEAT_HUGE /Fd.\ObjGXAMD64/ /Zi -Ilibvterm/include -DINLINE=""  -DVSNPRINTF=vim_vsnprintf  -DSNPRINTF=vim_snprintf  -DIS_COMBINING_FUNCTION=utf_iscomposing_uint  -DWCWIDTH_FUNCTION=utf_uint2cells  -DGET_SPECIAL_PTY_TYPE_FUNCTION=get_special_pty_type  -D_CRT_SECURE_NO_WARNINGS /Fo.\ObjGXAMD64/vterm_state.obj libvterm/src/state.c
state.c
        cl -c /W3 /GF /nologo -I. -Iproto -DHAVE_PATHDEF -DWIN32 -DHAVE_STDINT_H  -DFEAT_CSCOPE -DFEAT_TERMINAL -DFEAT_SOUND -DFEAT_NETBEANS_INTG -DFEAT_JOB_CHANNEL -DFEAT_IPV6 -DHAVE_INET_NTOP   -DFEAT_XPM_W32     -DWINVER=0x0601 -D_WIN32_WINNT=0x0601  /source-charset:utf-8 /MP /Ox /GL -DNDEBUG  /Zl /MT /D_CRT_SECURE_NO_DEPRECATE /D_CRT_NONSTDC_NO_DEPRECATE -DFEAT_MBYTE_IME -DDYNAMIC_IME -DFEAT_GUI_MSWIN -DFEAT_DIRECTX -DDYNAMIC_DIRECTX -DFEAT_DIRECTX_COLOR_EMOJI -DDYNAMIC_ICONV -DDYNAMIC_GETTEXT -DFEAT_HUGE /Fd.\ObjGXAMD64/ /Zi -Ilibvterm/include -DINLINE=""  -DVSNPRINTF=vim_vsnprintf  -DSNPRINTF=vim_snprintf  -DIS_COMBINING_FUNCTION=utf_iscomposing_uint  -DWCWIDTH_FUNCTION=utf_uint2cells  -DGET_SPECIAL_PTY_TYPE_FUNCTION=get_special_pty_type  -D_CRT_SECURE_NO_WARNINGS /Fo.\ObjGXAMD64/vterm_unicode.obj libvterm/src/unicode.c
unicode.c
        cl -c /W3 /GF /nologo -I. -Iproto -DHAVE_PATHDEF -DWIN32 -DHAVE_STDINT_H  -DFEAT_CSCOPE -DFEAT_TERMINAL -DFEAT_SOUND -DFEAT_NETBEANS_INTG -DFEAT_JOB_CHANNEL -DFEAT_IPV6 -DHAVE_INET_NTOP   -DFEAT_XPM_W32     -DWINVER=0x0601 -D_WIN32_WINNT=0x0601  /source-charset:utf-8 /MP /Ox /GL -DNDEBUG  /Zl /MT /D_CRT_SECURE_NO_DEPRECATE /D_CRT_NONSTDC_NO_DEPRECATE -DFEAT_MBYTE_IME -DDYNAMIC_IME -DFEAT_GUI_MSWIN -DFEAT_DIRECTX -DDYNAMIC_DIRECTX -DFEAT_DIRECTX_COLOR_EMOJI -DDYNAMIC_ICONV -DDYNAMIC_GETTEXT -DFEAT_HUGE /Fd.\ObjGXAMD64/ /Zi -Ilibvterm/include -DINLINE=""  -DVSNPRINTF=vim_vsnprintf  -DSNPRINTF=vim_snprintf  -DIS_COMBINING_FUNCTION=utf_iscomposing_uint  -DWCWIDTH_FUNCTION=utf_uint2cells  -DGET_SPECIAL_PTY_TYPE_FUNCTION=get_special_pty_type  -D_CRT_SECURE_NO_WARNINGS /Fo.\ObjGXAMD64/vterm_vterm.obj libvterm/src/vterm.c
vterm.c
        cl -c /W3 /GF /nologo -I. -Iproto -DHAVE_PATHDEF -DWIN32 -DHAVE_STDINT_H  -DFEAT_CSCOPE -DFEAT_TERMINAL -DFEAT_SOUND -DFEAT_NETBEANS_INTG -DFEAT_JOB_CHANNEL -DFEAT_IPV6 -DHAVE_INET_NTOP   -DFEAT_XPM_W32     -DWINVER=0x0601 -D_WIN32_WINNT=0x0601  /source-charset:utf-8 /MP /Ox /GL -DNDEBUG  /Zl /MT /D_CRT_SECURE_NO_DEPRECATE /D_CRT_NONSTDC_NO_DEPRECATE -DFEAT_MBYTE_IME -DDYNAMIC_IME -DFEAT_GUI_MSWIN -DFEAT_DIRECTX -DDYNAMIC_DIRECTX -DFEAT_DIRECTX_COLOR_EMOJI -DDYNAMIC_ICONV -DDYNAMIC_GETTEXT -DFEAT_HUGE /Fd.\ObjGXAMD64/ /Zi /Fo.\ObjGXAMD64/ -I xpm\x64\include -I xpm\x64\..\include xpm_w32.c
xpm_w32.c
        cl -c /W3 /GF /nologo -I. -Iproto -DHAVE_PATHDEF -DWIN32 -DHAVE_STDINT_H  -DFEAT_CSCOPE -DFEAT_TERMINAL -DFEAT_SOUND -DFEAT_NETBEANS_INTG -DFEAT_JOB_CHANNEL -DFEAT_IPV6 -DHAVE_INET_NTOP   -DFEAT_XPM_W32     -DWINVER=0x0601 -D_WIN32_WINNT=0x0601  /source-charset:utf-8 /MP /Ox /GL -DNDEBUG  /Zl /MT /D_CRT_SECURE_NO_DEPRECATE /D_CRT_NONSTDC_NO_DEPRECATE -DFEAT_MBYTE_IME -DDYNAMIC_IME -DFEAT_GUI_MSWIN -DFEAT_DIRECTX -DDYNAMIC_DIRECTX -DFEAT_DIRECTX_COLOR_EMOJI -DDYNAMIC_ICONV -DDYNAMIC_GETTEXT -DFEAT_HUGE /Fd.\ObjGXAMD64/ /Zi /Fo.\ObjGXAMD64/ alloc.c arabic.c arglist.c autocmd.c beval.c blob.c blowfish.c buffer.c bufwrite.c change.c charset.c cindent.c clientserver.c clipboard.c cmdexpand.c cmdhist.c crypt.c crypt_zip.c debugger.c dict.c diff.c digraph.c drawline.c drawscreen.c edit.c eval.c evalbuffer.c evalfunc.c evalvars.c evalwindow.c ex_cmds.c ex_cmds2.c ex_docmd.c ex_eval.c ex_getln.c fileio.c filepath.c findfile.c float.c fold.c getchar.c gui_xim.c hardcopy.c hashtab.c help.c highlight.c if_cscope.c indent.c insexpand.c json.c list.c locale.c logfile.c main.c map.c mark.c match.c mbyte.c memfile.c memline.c menu.c message.c misc1.c misc2.c mouse.c move.c normal.c ops.c option.c optionstr.c os_mswin.c os_win32.c popupmenu.c popupwin.c profiler.c quickfix.c regexp.c register.c scriptfile.c screen.c search.c session.c sha256.c sign.c spell.c spellfile.c spellsuggest.c strings.c syntax.c tag.c term.c testing.c textformat.c textobject.c textprop.c time.c typval.c ui.c undo.c usercmd.c userfunc.c vim9class.c vim9cmds.c vim9compile.c vim9execute.c vim9expr.c vim9instr.c vim9script.c vim9type.c viminfo.c winclip.c window.c os_w32exe.c gui.c gui_beval.c gui_w32.c terminal.c sound.c netbeans.c job.c channel.c
alloc.c
arabic.c
arglist.c
autocmd.c
beval.c
blob.c
blowfish.c
buffer.c
bufwrite.c
change.c
charset.c
cindent.c
clientserver.c
clipboard.c
cmdexpand.c
cmdhist.c
crypt.c
crypt_zip.c
debugger.c
dict.c
diff.c
digraph.c
drawline.c
drawscreen.c
edit.c
eval.c
evalbuffer.c
evalfunc.c
evalvars.c
evalwindow.c
ex_cmds.c
ex_cmds2.c
ex_docmd.c
ex_eval.c
ex_getln.c
fileio.c
filepath.c
findfile.c
float.c
fold.c
getchar.c
gui_xim.c
hardcopy.c
hashtab.c
help.c
highlight.c
if_cscope.c
indent.c
insexpand.c
json.c
list.c
locale.c
logfile.c
main.c
map.c
mark.c
match.c
mbyte.c
memfile.c
memline.c
menu.c
message.c
misc1.c
misc2.c
mouse.c
move.c
normal.c
ops.c
option.c
optionstr.c
os_mswin.c
os_win32.c
popupmenu.c
popupwin.c
profiler.c
quickfix.c
regexp.c
register.c
scriptfile.c
screen.c
search.c
session.c
sha256.c
sign.c
spell.c
spellfile.c
spellsuggest.c
strings.c
syntax.c
tag.c
term.c
testing.c
textformat.c
textobject.c
textprop.c
time.c
typval.c
ui.c
undo.c
usercmd.c
userfunc.c
vim9class.c
vim9cmds.c
vim9compile.c
vim9execute.c
vim9expr.c
vim9instr.c
vim9script.c
vim9type.c
viminfo.c
winclip.c
window.c
os_w32exe.c
gui.c
gui_beval.c
gui_w32.c
terminal.c
sound.c
netbeans.c
job.c
channel.c
        cl -c /W3 /GF /nologo -I. -Iproto -DHAVE_PATHDEF -DWIN32 -DHAVE_STDINT_H  -DFEAT_CSCOPE -DFEAT_TERMINAL -DFEAT_SOUND -DFEAT_NETBEANS_INTG -DFEAT_JOB_CHANNEL -DFEAT_IPV6 -DHAVE_INET_NTOP   -DFEAT_XPM_W32     -DWINVER=0x0601 -D_WIN32_WINNT=0x0601  /source-charset:utf-8 /MP /Ox /GL -DNDEBUG  /Zl /MT /D_CRT_SECURE_NO_DEPRECATE /D_CRT_NONSTDC_NO_DEPRECATE -DFEAT_MBYTE_IME -DDYNAMIC_IME -DFEAT_GUI_MSWIN -DFEAT_DIRECTX -DDYNAMIC_DIRECTX -DFEAT_DIRECTX_COLOR_EMOJI -DDYNAMIC_ICONV -DDYNAMIC_GETTEXT -DFEAT_HUGE /Fd.\ObjGXAMD64/ /Zi /Fo.\ObjGXAMD64/ xdiff/\xdiffi.c xdiff/\xemit.c xdiff/\xprepare.c xdiff/\xutils.c xdiff/\xhistogram.c xdiff/\xpatience.c
xdiffi.c
xemit.c
xprepare.c
xutils.c
xhistogram.c
xpatience.c
        cl -c /W3 /GF /nologo -I. -Iproto -DHAVE_PATHDEF -DWIN32 -DHAVE_STDINT_H  -DFEAT_CSCOPE -DFEAT_TERMINAL -DFEAT_SOUND -DFEAT_NETBEANS_INTG -DFEAT_JOB_CHANNEL -DFEAT_IPV6 -DHAVE_INET_NTOP   -DFEAT_XPM_W32     -DWINVER=0x0601 -D_WIN32_WINNT=0x0601  /source-charset:utf-8 /MP /Ox /GL -DNDEBUG  /Zl /MT /D_CRT_SECURE_NO_DEPRECATE /D_CRT_NONSTDC_NO_DEPRECATE -DFEAT_MBYTE_IME -DDYNAMIC_IME -DFEAT_GUI_MSWIN -DFEAT_DIRECTX -DDYNAMIC_DIRECTX -DFEAT_DIRECTX_COLOR_EMOJI -DDYNAMIC_ICONV -DDYNAMIC_GETTEXT -DFEAT_HUGE /Fd.\ObjGXAMD64/ /Zi /Fo.\ObjGXAMD64/ gui_dwrite.cpp
gui_dwrite.cpp
        cl -c /W3 /GF /nologo -I. -Iproto -DHAVE_PATHDEF -DWIN32 -DHAVE_STDINT_H  -DFEAT_CSCOPE -DFEAT_TERMINAL -DFEAT_SOUND -DFEAT_NETBEANS_INTG -DFEAT_JOB_CHANNEL -DFEAT_IPV6 -DHAVE_INET_NTOP   -DFEAT_XPM_W32     -DWINVER=0x0601 -D_WIN32_WINNT=0x0601  /source-charset:utf-8 /MP /Ox /GL -DNDEBUG  /Zl /MT /D_CRT_SECURE_NO_DEPRECATE /D_CRT_NONSTDC_NO_DEPRECATE -DFEAT_MBYTE_IME -DDYNAMIC_IME -DFEAT_GUI_MSWIN -DFEAT_DIRECTX -DDYNAMIC_DIRECTX -DFEAT_DIRECTX_COLOR_EMOJI -DDYNAMIC_ICONV -DDYNAMIC_GETTEXT -DFEAT_HUGE /Fd.\ObjGXAMD64/ /Zi /Fo.\ObjGXAMD64/ version.c
version.c
        link @C:\Users\hui74\AppData\Local\Temp\nm4D08.tmp
正在生成代码
  100%   0 seconds remaining
已完成代码的生成

D:\tmp\vim-9.0.2103\src>
"""

defined_words = set()

for word in nmake_log.split(" "):
    word = word.strip()
    if len(word) == 0:
        continue
    if word[:2] != '-D':
        continue
    # print(word)
    defined_words.add(word.replace("-D", ""))
print(";".join(defined_words))

lib_words = set()

for word in nmake_log.split(" "):
    word = word.strip()
    if len(word) == 0:
        continue
    if word[-4:] != '.lib':
        continue
    # print(word)
    lib_words.add(word.replace("-D", ""))
# print(";".join(lib_words))
