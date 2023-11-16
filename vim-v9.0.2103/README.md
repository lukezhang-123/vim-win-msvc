
https://github.com/vim/vim/tags

https://github.com/vim/vim/archive/refs/tags/v9.0.2103.tar.gz

基于VIM最新v9.0.2103版本，在windows使用 `Visual Studio Community 2022` 编译和组织vim项目，方便使用IDE工具来调试和查看源码

`README.md` 根目录readme里的 `Compiling` 说编译要看 `src/INSTALL` 文件，源码都在 `src` 目录中

`src/INSTALL` 文件说, `src/INSTALLpc.txt` 是在windows的编译说明

`src/INSTALLpc.txt` 推荐使用最新 Visual Studio Community 2022工具编译

命令行编译过程：
1. 安装完 Visual Studio Community 2022，要选上编译桌面c++程序
2. 在win11开始菜单按钮，所有应用列表，打开`Visual Studio 2022`下 `x64 Native Tools Command Prompt for VS 2022`命令提示符窗口工具，`nmake /?` 测试编译工具正常输出
3. 切换到VIM/src源码目录`cd /d D:\tmp\vim-9.0.2103\src`，执行编译命令行VIM, `nmake -f Make_mvc.mak`, src/vim.exe生成，双击执行可见vim
4. 相同目录再次执行编译窗口gvim命令，`nmake -f Make_mvc.mak GUI=yes`
5. 现在的源码目录可以用于构建IDE项目，编译的目的是完整生成vim需要的所有文件，部分文件只有编译后才会产生

Make_mvc.mak的编译target是1225行的 all:

579行 VIM = vim, 如果定义了DEBUG宏，那就是605行VIM = vimd
179行OBJDIR值为ObjC（目录的文件夹名 ObjCAMD64），所以 VIMDLL是空，GUI是空，!if "$(VIMDLL)" == "yes" 这个判断会走到else部分，!叹号不是非的逻辑判断，在行首表示改行是逻辑代码，后面的有些行!在行首，空格几个再if,else等等可见证

1225  all
1219  MAIN_TARGET
1258  $(VIM).exe
1274  $(OUTDIR)

缺少日志里的 pathdef，encoding.c是 340 TERM_OBJ

634  OBJ

makefile中编译vim.exe依赖的组件
$(OUTDIR)  检查编译目录 507 OUTDIR=$(OBJDIR)  247  OBJDIR = $(OBJDIR)$(CPU)  179  OBJDIR = .\ObjC  234  CPU = AMD64  所以是 ObjCAMD64
$(OBJ)    634 OBJ = （因为最后一行747行最后是连接符，所以包括下面的if块，755行）
$(XDIFF_OBJ)   809  XDIFF_OBJ =
$(GUI_OBJ)   796 空 GUI_OBJ = ，上下是if块，但是因为没有GUI=yes参数，所以没被执行，GUI_OBJ是空的
$(CUI_OBJ)   805 CUI_OBJ = ，参考$(GUI_OBJ)，在if块的else部分，是两个if块的外层大if的else块部分
$(OLE_OBJ)   761 空，因为没有OLE=yes参数
$(OLE_IDL)   762 空
$(MZSCHEME_OBJ)   1022 空，未定义MZSCHEME
$(LUA_OBJ)   895 空  nmake-vim.log编译日志没有
$(PERL_OBJ)  1064 空
$(PYTHON_OBJ)  923 空
$(PYTHON3_OBJ)  952 空
$(RUBY_OBJ)   1120 空
$(TCL_OBJ)    874 空，vim会使用 if_tcl.c这样的组件标志文件
$(TERM_OBJ)   340
$(SOUND_OBJ)  465 没定义SOUND=yes,但是编译日志里有sound.c
$(NETBEANS_OBJ)  415 空
$(CHANNEL_OBJ)   472 没定义CHANNEL=yes，但是编译日志有channel.c
$(XPM_OBJ)   456 空
version.c
version.h


vim项目右键，添加，现有项，选择源码目录的alloc.c
查看 vim-v9.0.2103.vcxproj 里的添加项，用python脚本批量生成，注意pathdef.c是在编译目录生成的

先加 634行的obj（脚本生成后，手动改vs 项目文件）, 755 os_w32exe.c  vim.rc
pathdef.c
809 XDIFF_OBJ  xdiff目录下
805 CUI_OBJ
340 TERM_OBJ，vterm_encoding 是libvterm/src下的encoding
465 SOUND_OBJ
472 channel job
version.c

vim项目右键，属性，c/c++，输出文件，对象文件名，$(IntDir)/%(RelativeDir)/


vim项目右键，属性，c/c++，常规 —>附加包含目录
$(SolutionDir)vim-9.0.2103-src\src; $(SolutionDir)vim-9.0.2103-src\src\proto; $(SolutionDir)vim-9.0.2103-src\src\libvterm\include


vim项目右键，属性，c/c++,预处理器
NDEBUG ;WINVER=0x0501 ;HAVE_STDINT_H ;_WIN32_WINNT=0x0501 ;_WIN32_WINNT=0x0600 ;FEAT_JOB_CHANNEL ;DYNAMIC_GETTEXT ;IS_COMBINING_FUNCTION=utf_iscomposing_uint ;DYNAMIC_ICONV ;HAVE_PATHDEF ;VSNPRINTF=vim_vsnprintf ;FEAT_HUGE ;INLINE="" ;WCWIDTH_FUNCTION=utf_uint2cells ;_CRT_SECURE_NO_WARNINGS ;USE_DYNFILEID ;FEAT_GETTEXT ;FEAT_CSCOPE ;FEAT_TERMINAL ;WIN32 

从编译日志提取
GET_SPECIAL_PTY_TYPE_FUNCTION=get_special_pty_type;HAVE_INET_NTOP;FEAT_SOUND;NDEBUG;WCWIDTH_FUNCTION=utf_uint2cells;HAVE_PATHDEF;FEAT_HUGE;DYNAMIC_GETTEXT;HAVE_STDINT_H;VSNPRINTF=vim_vsnprintf;SNPRINTF=vim_snprintf;INLINE="";DYNAMIC_IME;FEAT_JOB_CHANNEL;IS_COMBINING_FUNCTION=utf_iscomposing_uint;FEAT_CSCOPE;WIN32;_CRT_SECURE_NO_WARNINGS;FEAT_IPV6;DYNAMIC_ICONV;FEAT_TERMINAL;_WIN32_WINNT=0x0601;FEAT_GETTEXT;WINVER=0x0601;FEAT_MBYTE_IME

vim项目右键，属性，c/c++，连接器，输入，附加依赖项
kernel32.lib;advapi32.lib;shell32.lib;user32.lib;uuid.lib;ole32.lib;comctl32.lib;gdi32.lib;oleaut32.lib;oldnames.lib;comdlg32.lib;netapi32.lib;winmm.lib


vim项目右键，属性，c/c++,预编译头，预编译头--不使用

_DEBUG;%(PreprocessorDefinitions);
fatal  error C1010: 在查找预编译头时遇到意外的文件结尾。是否忘记了向源中添加“#include "pch.h"”?

---

### GVim

ObjGXAMD64 说明 gui和DIRECTX，  177  182

Make_mvc.mak的编译target是1225行的 all:

1219 VIMDLL是空，MAIN_TARGET =
793  VIM = g$(VIM)
1258 $(VIM).exe  和vim.exe差不多

makefile中编译gvim.exe依赖的组件
$(OUTDIR)  检查编译目录 507 OUTDIR=$(OBJDIR)  247  OBJDIR = $(OBJDIR)$(CPU)  179  OBJDIR = .\ObjC  234  CPU = AMD64  所以是 ObjCAMD64
$(OBJ)    634 OBJ = （因为最后一行747行最后是连接符，所以包括下面的if块，755行）
$(XDIFF_OBJ)   809  XDIFF_OBJ =
$(GUI_OBJ)   841  GUI_OBJ = $(GUI_OBJ) $(DIRECTX_OBJ) 796  GUI_OBJ =  432 DIRECTX_OBJ	=
$(CUI_OBJ)   805 空，没有iscygpty
$(OLE_OBJ)   761 空，因为没有OLE=yes参数
$(OLE_IDL)   762 空
$(MZSCHEME_OBJ)   1022 空，未定义MZSCHEME
$(LUA_OBJ)   895 空  nmake-vim.log编译日志没有
$(PERL_OBJ)  1064 空
$(PYTHON_OBJ)  923 空
$(PYTHON3_OBJ)  952 空
$(RUBY_OBJ)   1120 空
$(TCL_OBJ)    874 空，vim会使用 if_tcl.c这样的组件标志文件
$(TERM_OBJ)   340
$(SOUND_OBJ)  465 没定义SOUND=yes,但是编译日志里有sound.c
$(NETBEANS_OBJ)  415 空
$(CHANNEL_OBJ)   472 没定义CHANNEL=yes，但是编译日志有channel.c
$(XPM_OBJ)   456
version.c
version.h
NETBEANS_OBJ  415

$(SolutionDir)vim-9.0.2103-src\src\xpm\include

HAVE_STDINT_H;FEAT_IPV6;HAVE_INET_NTOP;DYNAMIC_GETTEXT;FEAT_XPM_W32;FEAT_GUI_MSWIN;NDEBUG;WCWIDTH_FUNCTION=utf_uint2cells;DYNAMIC_DIRECTX;FEAT_NETBEANS_INTG;FEAT_SOUND;_WIN32_WINNT=0x0601;WIN32;FEAT_DIRECTX_COLOR_EMOJI;FEAT_HUGE;FEAT_JOB_CHANNEL;WINVER=0x0601;INLINE="";DYNAMIC_IME;SNPRINTF=vim_snprintf;HAVE_PATHDEF;FEAT_CSCOPE;DYNAMIC_ICONV;FEAT_TERMINAL;FEAT_MBYTE_IME;GET_SPECIAL_PTY_TYPE_FUNCTION=get_special_pty_type;_CRT_SECURE_NO_WARNINGS;IS_COMBINING_FUNCTION=utf_iscomposing_uint;VSNPRINTF=vim_vsnprintf;FEAT_DIRECTX


kernel32.lib;advapi32.lib;shell32.lib;user32.lib;uuid.lib;ole32.lib;comctl32.lib;gdi32.lib;oleaut32.lib;oldnames.lib;comdlg32.lib;netapi32.lib;winmm.lib;version.lib;imm32.lib;winspool.lib;comctl32.lib;$(SolutionDir)vim-9.0.2103-src\src\xpm\$(LibrariesArchitecture)\lib-vc14\libXpm.lib


test01.py  是根据makefile里obj要编译的c文件，110多个，批量生成visual studio工程配置文件，避免手动添加麻烦
test02.py  是根据编译日志，提取定义的宏变量和link使用的库文件名
