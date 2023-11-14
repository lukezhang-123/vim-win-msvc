
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
179行OBJDIR值为ObjC（目录的文件夹名 ObjCAMD64），所以 VIMDLL是空，GUI是空，!if "$(VIMDLL)" == "yes" 这个判断会走到else部分，!叹号不是非，是!if一起表示if语句的意思



1225  all
1219  MAIN_TARGET
1258  $(VIM).exe
1274  $(OUTDIR)

缺少日志里的 pathdef，encoding.c是 340 TERM_OBJ

634  OBJ
