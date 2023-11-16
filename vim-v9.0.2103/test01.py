# -*- coding: utf-8 -*-
import os.path

obj_str = r"""
$(OUTDIR)\alloc.obj \
	$(OUTDIR)\arabic.obj \
	$(OUTDIR)\arglist.obj \
	$(OUTDIR)\autocmd.obj \
	$(OUTDIR)\beval.obj \
	$(OUTDIR)\blob.obj \
	$(OUTDIR)\blowfish.obj \
	$(OUTDIR)\buffer.obj \
	$(OUTDIR)\bufwrite.obj \
	$(OUTDIR)\change.obj \
	$(OUTDIR)\charset.obj \
	$(OUTDIR)\cindent.obj \
	$(OUTDIR)\clientserver.obj \
	$(OUTDIR)\clipboard.obj \
	$(OUTDIR)\cmdexpand.obj \
	$(OUTDIR)\cmdhist.obj \
	$(OUTDIR)\crypt.obj \
	$(OUTDIR)\crypt_zip.obj \
	$(OUTDIR)\debugger.obj \
	$(OUTDIR)\dict.obj \
	$(OUTDIR)\diff.obj \
	$(OUTDIR)\digraph.obj \
	$(OUTDIR)\drawline.obj \
	$(OUTDIR)\drawscreen.obj \
	$(OUTDIR)\edit.obj \
	$(OUTDIR)\eval.obj \
	$(OUTDIR)\evalbuffer.obj \
	$(OUTDIR)\evalfunc.obj \
	$(OUTDIR)\evalvars.obj \
	$(OUTDIR)\evalwindow.obj \
	$(OUTDIR)\ex_cmds.obj \
	$(OUTDIR)\ex_cmds2.obj \
	$(OUTDIR)\ex_docmd.obj \
	$(OUTDIR)\ex_eval.obj \
	$(OUTDIR)\ex_getln.obj \
	$(OUTDIR)\fileio.obj \
	$(OUTDIR)\filepath.obj \
	$(OUTDIR)\findfile.obj \
	$(OUTDIR)\float.obj \
	$(OUTDIR)\fold.obj \
	$(OUTDIR)\getchar.obj \
	$(OUTDIR)\gui_xim.obj \
	$(OUTDIR)\hardcopy.obj \
	$(OUTDIR)\hashtab.obj \
	$(OUTDIR)\help.obj \
	$(OUTDIR)\highlight.obj \
	$(OUTDIR)\if_cscope.obj \
	$(OUTDIR)\indent.obj \
	$(OUTDIR)\insexpand.obj \
	$(OUTDIR)\json.obj \
	$(OUTDIR)\list.obj \
	$(OUTDIR)\locale.obj \
	$(OUTDIR)\logfile.obj \
	$(OUTDIR)\main.obj \
	$(OUTDIR)\map.obj \
	$(OUTDIR)\mark.obj \
	$(OUTDIR)\match.obj \
	$(OUTDIR)\mbyte.obj \
	$(OUTDIR)\memfile.obj \
	$(OUTDIR)\memline.obj \
	$(OUTDIR)\menu.obj \
	$(OUTDIR)\message.obj \
	$(OUTDIR)\misc1.obj \
	$(OUTDIR)\misc2.obj \
	$(OUTDIR)\mouse.obj \
	$(OUTDIR)\move.obj \
	$(OUTDIR)\normal.obj \
	$(OUTDIR)\ops.obj \
	$(OUTDIR)\option.obj \
	$(OUTDIR)\optionstr.obj \
	$(OUTDIR)\os_mswin.obj \
	$(OUTDIR)\os_win32.obj \
	$(OUTDIR)\pathdef.obj \
	$(OUTDIR)\popupmenu.obj \
	$(OUTDIR)\popupwin.obj \
	$(OUTDIR)\profiler.obj \
	$(OUTDIR)\quickfix.obj \
	$(OUTDIR)\regexp.obj \
	$(OUTDIR)\register.obj \
	$(OUTDIR)\scriptfile.obj \
	$(OUTDIR)\screen.obj \
	$(OUTDIR)\search.obj \
	$(OUTDIR)\session.obj \
	$(OUTDIR)\sha256.obj \
	$(OUTDIR)\sign.obj \
	$(OUTDIR)\spell.obj \
	$(OUTDIR)\spellfile.obj \
	$(OUTDIR)\spellsuggest.obj \
	$(OUTDIR)\strings.obj \
	$(OUTDIR)\syntax.obj \
	$(OUTDIR)\tag.obj \
	$(OUTDIR)\term.obj \
	$(OUTDIR)\testing.obj \
	$(OUTDIR)\textformat.obj \
	$(OUTDIR)\textobject.obj \
	$(OUTDIR)\textprop.obj \
	$(OUTDIR)\time.obj \
	$(OUTDIR)\typval.obj \
	$(OUTDIR)\ui.obj \
	$(OUTDIR)\undo.obj \
	$(OUTDIR)\usercmd.obj \
	$(OUTDIR)\userfunc.obj \
	$(OUTDIR)\vim9class.obj \
	$(OUTDIR)\vim9cmds.obj \
	$(OUTDIR)\vim9compile.obj \
	$(OUTDIR)\vim9execute.obj \
	$(OUTDIR)\vim9expr.obj \
	$(OUTDIR)\vim9instr.obj \
	$(OUTDIR)\vim9script.obj \
	$(OUTDIR)\vim9type.obj \
	$(OUTDIR)\viminfo.obj \
	$(OUTDIR)\winclip.obj \
	$(OUTDIR)\window.obj
"""

vim_src_path = 'D:\\proj\\github\\lukezhang-123\\vim-win-msvc\\vim-v9.0.2103\\vim-9.0.2103-src\\src\\'


for obj_one in obj_str.split("\n"):
    obj_one = obj_one.strip()
    if len(obj_one) == 0:
        continue
    obj_name = obj_one.replace("$(OUTDIR)\\","")
    obj_name = obj_name.replace("\\","").strip()
    obj_name = obj_name.replace(".obj","")
    # print(obj_name)
    if not os.path.exists(vim_src_path + obj_name + '.c'):
        print(obj_name)
    print("<ClCompile Include=\"..\\vim-9.0.2103-src\\src\\%s.c\" />" % obj_name)
