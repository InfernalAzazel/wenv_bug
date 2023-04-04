<div align="center"><h1>bdba_to_sbom</h1></div>

## compile help
### 1. run compile.py
- The compiled program is under the dist folder
- Environmental requirements Python 3.10
```shell
WENV_ARCH=win64 WENV_PYTHONVERSION=3.10.0 wenv pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

WENV_ARCH=win64 WENV_PYTHONVERSION=3.10.0 wenv pyinstaller --onefile main.py
```
### 2. err
```
ext@hzh5u:/work/code/github/wenv_bug$ WENV_ARCH=win64 WENV_PYTHONVERSION=3.10.0 wenv pyinstaller --onefile main.py
883 INFO: PyInstaller: 5.9.0
884 INFO: Python: 3.10.0
951 INFO: Platform: Windows-10-10.0.18362
953 INFO: wrote Z:\work\code\github\wenv_bug\main.spec
959 INFO: UPX is not available.
962 INFO: Extending PYTHONPATH with paths
['Z:\\work\\code\\github\\wenv_bug']
2142 INFO: checking Analysis
2143 INFO: Building Analysis because Analysis-00.toc is non existent
2143 INFO: Initializing module dependency graph...
2149 INFO: Caching module graph hooks...
2201 INFO: Analyzing base_library.zip ...
6104 INFO: Loading module hook 'hook-heapq.py' from 'Z:\\tmp\\wenv-88fbf1b9\\lib\\site-packages\\PyInstaller\\hooks'...
6173 INFO: Loading module hook 'hook-encodings.py' from 'Z:\\tmp\\wenv-88fbf1b9\\lib\\site-packages\\PyInstaller\\hooks'...
8055 INFO: Loading module hook 'hook-pickle.py' from 'Z:\\tmp\\wenv-88fbf1b9\\lib\\site-packages\\PyInstaller\\hooks'...
8855 INFO: Caching module dependency graph...
8967 INFO: running Analysis Analysis-00.toc
8974 INFO: Adding Microsoft.Windows.Common-Controls to dependent assemblies of final executable
  required by Z:\tmp\wenv-88fbf1b9\python.exe
9053 INFO: Analyzing Z:\work\code\github\wenv_bug\main.py
9142 INFO: Loading module hook 'hook-numpy.py' from 'C:\\python-3.10.0.stable\\Lib\\site-packages\\numpy\\_pyinstaller'...
10111 INFO: Loading module hook 'hook-difflib.py' from 'Z:\\tmp\\wenv-88fbf1b9\\lib\\site-packages\\PyInstaller\\hooks'...
10310 INFO: Loading module hook 'hook-multiprocessing.util.py' from 'Z:\\tmp\\wenv-88fbf1b9\\lib\\site-packages\\PyInstaller\\hooks'...
10442 INFO: Loading module hook 'hook-xml.py' from 'Z:\\tmp\\wenv-88fbf1b9\\lib\\site-packages\\PyInstaller\\hooks'...
10847 INFO: Loading module hook 'hook-platform.py' from 'Z:\\tmp\\wenv-88fbf1b9\\lib\\site-packages\\PyInstaller\\hooks'...
11019 INFO: Loading module hook 'hook-sysconfig.py' from 'Z:\\tmp\\wenv-88fbf1b9\\lib\\site-packages\\PyInstaller\\hooks'...
11279 INFO: Loading module hook 'hook-win32ctypes.core.py' from 'Z:\\tmp\\wenv-88fbf1b9\\lib\\site-packages\\PyInstaller\\hooks'...
13084 INFO: Loading module hook 'hook-pkg_resources.py' from 'Z:\\tmp\\wenv-88fbf1b9\\lib\\site-packages\\PyInstaller\\hooks'...
15993 INFO: Processing pre-find module path hook distutils from 'Z:\\tmp\\wenv-88fbf1b9\\lib\\site-packages\\PyInstaller\\hooks\\pre_find_module_path\\hook-distutils.py'.
16807 INFO: Loading module hook 'hook-distutils.py' from 'Z:\\tmp\\wenv-88fbf1b9\\lib\\site-packages\\PyInstaller\\hooks'...
16891 INFO: Loading module hook 'hook-xml.dom.domreg.py' from 'Z:\\tmp\\wenv-88fbf1b9\\lib\\site-packages\\PyInstaller\\hooks'...
17323 INFO: Processing pre-safe import module hook gi from 'Z:\\tmp\\wenv-88fbf1b9\\lib\\site-packages\\PyInstaller\\hooks\\pre_safe_import_module\\hook-gi.py'.
18368 INFO: Loading module hook 'hook-openpyxl.py' from 'Z:\\tmp\\wenv-88fbf1b9\\lib\\site-packages\\_pyinstaller_hooks_contrib\\hooks\\stdhooks'...
19515 INFO: Loading module hook 'hook-xml.etree.cElementTree.py' from 'Z:\\tmp\\wenv-88fbf1b9\\lib\\site-packages\\PyInstaller\\hooks'...
20956 INFO: Loading module hook 'hook-pandas.py' from 'Z:\\tmp\\wenv-88fbf1b9\\lib\\site-packages\\PyInstaller\\hooks'...
25532 INFO: Loading module hook 'hook-pytz.py' from 'Z:\\tmp\\wenv-88fbf1b9\\lib\\site-packages\\PyInstaller\\hooks'...
Traceback (most recent call last):
  File "runpy.py", line 196, in _run_module_as_main
  File "runpy.py", line 86, in _run_code
  File "Z:\tmp\wenv-88fbf1b9\Scripts\pyinstaller.exe\__main__.py", line 7, in <module>
  File "Z:\tmp\wenv-88fbf1b9\lib\site-packages\PyInstaller\__main__.py", line 194, in _console_script_run
    run()
  File "Z:\tmp\wenv-88fbf1b9\lib\site-packages\PyInstaller\__main__.py", line 180, in run
    run_build(pyi_config, spec_file, **vars(args))
  File "Z:\tmp\wenv-88fbf1b9\lib\site-packages\PyInstaller\__main__.py", line 61, in run_build
    PyInstaller.building.build_main.main(pyi_config, spec_file, **kwargs)
  File "Z:\tmp\wenv-88fbf1b9\lib\site-packages\PyInstaller\building\build_main.py", line 979, in main
    build(specfile, distpath, workpath, clean_build)
  File "Z:\tmp\wenv-88fbf1b9\lib\site-packages\PyInstaller\building\build_main.py", line 901, in build
    exec(code, spec_namespace)
  File "Z:\work\code\github\wenv_bug\main.spec", line 7, in <module>
    a = Analysis(
  File "Z:\tmp\wenv-88fbf1b9\lib\site-packages\PyInstaller\building\build_main.py", line 414, in __init__
    self.__postinit__()
  File "Z:\tmp\wenv-88fbf1b9\lib\site-packages\PyInstaller\building\datastruct.py", line 173, in __postinit__
    self.assemble()
  File "Z:\tmp\wenv-88fbf1b9\lib\site-packages\PyInstaller\building\build_main.py", line 577, in assemble
    priority_scripts.append(self.graph.add_script(script))
  File "Z:\tmp\wenv-88fbf1b9\lib\site-packages\PyInstaller\depend\analysis.py", line 269, in add_script
    self._top_script_node = super().add_script(pathname)
  File "Z:\tmp\wenv-88fbf1b9\lib\site-packages\PyInstaller\lib\modulegraph\modulegraph.py", line 1433, in add_script
    self._process_imports(n)
  File "Z:\tmp\wenv-88fbf1b9\lib\site-packages\PyInstaller\lib\modulegraph\modulegraph.py", line 2850, in _process_imports
    target_modules = self._safe_import_hook(*import_info, **kwargs)
  File "Z:\tmp\wenv-88fbf1b9\lib\site-packages\PyInstaller\depend\analysis.py", line 382, in _safe_import_hook
    return super()._safe_import_hook(target_module_partname, source_module, target_attr_names, level, edge_attr)
  File "Z:\tmp\wenv-88fbf1b9\lib\site-packages\PyInstaller\lib\modulegraph\modulegraph.py", line 2301, in _safe_import_hook
    target_modules = self.import_hook(
  File "Z:\tmp\wenv-88fbf1b9\lib\site-packages\PyInstaller\lib\modulegraph\modulegraph.py", line 1505, in import_hook
    target_package, target_module_partname = self._find_head_package(
  File "Z:\tmp\wenv-88fbf1b9\lib\site-packages\PyInstaller\lib\modulegraph\modulegraph.py", line 1684, in _find_head_package
    target_package = self._safe_import_module(
  File "Z:\tmp\wenv-88fbf1b9\lib\site-packages\PyInstaller\depend\analysis.py", line 429, in _safe_import_module
    return super()._safe_import_module(module_basename, module_name, parent_package)
  File "Z:\tmp\wenv-88fbf1b9\lib\site-packages\PyInstaller\lib\modulegraph\modulegraph.py", line 2062, in _safe_import_module
    self._process_imports(n)
  File "Z:\tmp\wenv-88fbf1b9\lib\site-packages\PyInstaller\lib\modulegraph\modulegraph.py", line 2850, in _process_imports
    target_modules = self._safe_import_hook(*import_info, **kwargs)
  File "Z:\tmp\wenv-88fbf1b9\lib\site-packages\PyInstaller\depend\analysis.py", line 382, in _safe_import_hook
    return super()._safe_import_hook(target_module_partname, source_module, target_attr_names, level, edge_attr)
  File "Z:\tmp\wenv-88fbf1b9\lib\site-packages\PyInstaller\lib\modulegraph\modulegraph.py", line 2301, in _safe_import_hook
    target_modules = self.import_hook(
  File "Z:\tmp\wenv-88fbf1b9\lib\site-packages\PyInstaller\lib\modulegraph\modulegraph.py", line 1518, in import_hook
    submodule = self._safe_import_module(head, mname, submodule)
  File "Z:\tmp\wenv-88fbf1b9\lib\site-packages\PyInstaller\depend\analysis.py", line 429, in _safe_import_module
    return super()._safe_import_module(module_basename, module_name, parent_package)
  File "Z:\tmp\wenv-88fbf1b9\lib\site-packages\PyInstaller\lib\modulegraph\modulegraph.py", line 2062, in _safe_import_module
    self._process_imports(n)
  File "Z:\tmp\wenv-88fbf1b9\lib\site-packages\PyInstaller\lib\modulegraph\modulegraph.py", line 2850, in _process_imports
    target_modules = self._safe_import_hook(*import_info, **kwargs)
  File "Z:\tmp\wenv-88fbf1b9\lib\site-packages\PyInstaller\depend\analysis.py", line 382, in _safe_import_hook
    return super()._safe_import_hook(target_module_partname, source_module, target_attr_names, level, edge_attr)
  File "Z:\tmp\wenv-88fbf1b9\lib\site-packages\PyInstaller\lib\modulegraph\modulegraph.py", line 2301, in _safe_import_hook
    target_modules = self.import_hook(
  File "Z:\tmp\wenv-88fbf1b9\lib\site-packages\PyInstaller\lib\modulegraph\modulegraph.py", line 1518, in import_hook
    submodule = self._safe_import_module(head, mname, submodule)
  File "Z:\tmp\wenv-88fbf1b9\lib\site-packages\PyInstaller\depend\analysis.py", line 429, in _safe_import_module
    return super()._safe_import_module(module_basename, module_name, parent_package)
  File "Z:\tmp\wenv-88fbf1b9\lib\site-packages\PyInstaller\lib\modulegraph\modulegraph.py", line 2062, in _safe_import_module
    self._process_imports(n)
  File "Z:\tmp\wenv-88fbf1b9\lib\site-packages\PyInstaller\lib\modulegraph\modulegraph.py", line 2850, in _process_imports
    target_modules = self._safe_import_hook(*import_info, **kwargs)
  File "Z:\tmp\wenv-88fbf1b9\lib\site-packages\PyInstaller\depend\analysis.py", line 382, in _safe_import_hook
    return super()._safe_import_hook(target_module_partname, source_module, target_attr_names, level, edge_attr)
  File "Z:\tmp\wenv-88fbf1b9\lib\site-packages\PyInstaller\lib\modulegraph\modulegraph.py", line 2301, in _safe_import_hook
    target_modules = self.import_hook(
  File "Z:\tmp\wenv-88fbf1b9\lib\site-packages\PyInstaller\lib\modulegraph\modulegraph.py", line 1518, in import_hook
    submodule = self._safe_import_module(head, mname, submodule)
  File "Z:\tmp\wenv-88fbf1b9\lib\site-packages\PyInstaller\depend\analysis.py", line 429, in _safe_import_module
    return super()._safe_import_module(module_basename, module_name, parent_package)
  File "Z:\tmp\wenv-88fbf1b9\lib\site-packages\PyInstaller\lib\modulegraph\modulegraph.py", line 2062, in _safe_import_module
    self._process_imports(n)
  File "Z:\tmp\wenv-88fbf1b9\lib\site-packages\PyInstaller\lib\modulegraph\modulegraph.py", line 2850, in _process_imports
    target_modules = self._safe_import_hook(*import_info, **kwargs)
  File "Z:\tmp\wenv-88fbf1b9\lib\site-packages\PyInstaller\depend\analysis.py", line 382, in _safe_import_hook
    return super()._safe_import_hook(target_module_partname, source_module, target_attr_names, level, edge_attr)
  File "Z:\tmp\wenv-88fbf1b9\lib\site-packages\PyInstaller\lib\modulegraph\modulegraph.py", line 2301, in _safe_import_hook
    target_modules = self.import_hook(
  File "Z:\tmp\wenv-88fbf1b9\lib\site-packages\PyInstaller\lib\modulegraph\modulegraph.py", line 1518, in import_hook
    submodule = self._safe_import_module(head, mname, submodule)
  File "Z:\tmp\wenv-88fbf1b9\lib\site-packages\PyInstaller\depend\analysis.py", line 429, in _safe_import_module
    return super()._safe_import_module(module_basename, module_name, parent_package)
  File "Z:\tmp\wenv-88fbf1b9\lib\site-packages\PyInstaller\lib\modulegraph\modulegraph.py", line 2062, in _safe_import_module
    self._process_imports(n)
  File "Z:\tmp\wenv-88fbf1b9\lib\site-packages\PyInstaller\lib\modulegraph\modulegraph.py", line 2850, in _process_imports
    target_modules = self._safe_import_hook(*import_info, **kwargs)
  File "Z:\tmp\wenv-88fbf1b9\lib\site-packages\PyInstaller\depend\analysis.py", line 382, in _safe_import_hook
    return super()._safe_import_hook(target_module_partname, source_module, target_attr_names, level, edge_attr)
  File "Z:\tmp\wenv-88fbf1b9\lib\site-packages\PyInstaller\lib\modulegraph\modulegraph.py", line 2301, in _safe_import_hook
    target_modules = self.import_hook(
  File "Z:\tmp\wenv-88fbf1b9\lib\site-packages\PyInstaller\lib\modulegraph\modulegraph.py", line 1518, in import_hook
    submodule = self._safe_import_module(head, mname, submodule)
  File "Z:\tmp\wenv-88fbf1b9\lib\site-packages\PyInstaller\depend\analysis.py", line 429, in _safe_import_module
    return super()._safe_import_module(module_basename, module_name, parent_package)
  File "Z:\tmp\wenv-88fbf1b9\lib\site-packages\PyInstaller\lib\modulegraph\modulegraph.py", line 2062, in _safe_import_module
    self._process_imports(n)
  File "Z:\tmp\wenv-88fbf1b9\lib\site-packages\PyInstaller\lib\modulegraph\modulegraph.py", line 2850, in _process_imports
    target_modules = self._safe_import_hook(*import_info, **kwargs)
  File "Z:\tmp\wenv-88fbf1b9\lib\site-packages\PyInstaller\depend\analysis.py", line 382, in _safe_import_hook
    return super()._safe_import_hook(target_module_partname, source_module, target_attr_names, level, edge_attr)
  File "Z:\tmp\wenv-88fbf1b9\lib\site-packages\PyInstaller\lib\modulegraph\modulegraph.py", line 2301, in _safe_import_hook
    target_modules = self.import_hook(
  File "Z:\tmp\wenv-88fbf1b9\lib\site-packages\PyInstaller\lib\modulegraph\modulegraph.py", line 1518, in import_hook
    submodule = self._safe_import_module(head, mname, submodule)
  File "Z:\tmp\wenv-88fbf1b9\lib\site-packages\PyInstaller\depend\analysis.py", line 429, in _safe_import_module
    return super()._safe_import_module(module_basename, module_name, parent_package)
  File "Z:\tmp\wenv-88fbf1b9\lib\site-packages\PyInstaller\lib\modulegraph\modulegraph.py", line 2062, in _safe_import_module
    self._process_imports(n)
  File "Z:\tmp\wenv-88fbf1b9\lib\site-packages\PyInstaller\lib\modulegraph\modulegraph.py", line 2850, in _process_imports
    target_modules = self._safe_import_hook(*import_info, **kwargs)
  File "Z:\tmp\wenv-88fbf1b9\lib\site-packages\PyInstaller\depend\analysis.py", line 382, in _safe_import_hook
    return super()._safe_import_hook(target_module_partname, source_module, target_attr_names, level, edge_attr)
  File "Z:\tmp\wenv-88fbf1b9\lib\site-packages\PyInstaller\lib\modulegraph\modulegraph.py", line 2510, in _safe_import_hook
    self.import_hook(
  File "Z:\tmp\wenv-88fbf1b9\lib\site-packages\PyInstaller\lib\modulegraph\modulegraph.py", line 1544, in import_hook
    for target_submodule in self._import_importable_package_submodules(
  File "Z:\tmp\wenv-88fbf1b9\lib\site-packages\PyInstaller\lib\modulegraph\modulegraph.py", line 1794, in _import_importable_package_submodules
    submodule = self._safe_import_module(
  File "Z:\tmp\wenv-88fbf1b9\lib\site-packages\PyInstaller\depend\analysis.py", line 429, in _safe_import_module
    return super()._safe_import_module(module_basename, module_name, parent_package)
  File "Z:\tmp\wenv-88fbf1b9\lib\site-packages\PyInstaller\lib\modulegraph\modulegraph.py", line 2062, in _safe_import_module
    self._process_imports(n)
  File "Z:\tmp\wenv-88fbf1b9\lib\site-packages\PyInstaller\lib\modulegraph\modulegraph.py", line 2850, in _process_imports
    target_modules = self._safe_import_hook(*import_info, **kwargs)
  File "Z:\tmp\wenv-88fbf1b9\lib\site-packages\PyInstaller\depend\analysis.py", line 382, in _safe_import_hook
    return super()._safe_import_hook(target_module_partname, source_module, target_attr_names, level, edge_attr)
  File "Z:\tmp\wenv-88fbf1b9\lib\site-packages\PyInstaller\lib\modulegraph\modulegraph.py", line 2301, in _safe_import_hook
    target_modules = self.import_hook(
  File "Z:\tmp\wenv-88fbf1b9\lib\site-packages\PyInstaller\lib\modulegraph\modulegraph.py", line 1518, in import_hook
    submodule = self._safe_import_module(head, mname, submodule)
  File "Z:\tmp\wenv-88fbf1b9\lib\site-packages\PyInstaller\depend\analysis.py", line 429, in _safe_import_module
    return super()._safe_import_module(module_basename, module_name, parent_package)
  File "Z:\tmp\wenv-88fbf1b9\lib\site-packages\PyInstaller\lib\modulegraph\modulegraph.py", line 2062, in _safe_import_module
    self._process_imports(n)
  File "Z:\tmp\wenv-88fbf1b9\lib\site-packages\PyInstaller\lib\modulegraph\modulegraph.py", line 2850, in _process_imports
    target_modules = self._safe_import_hook(*import_info, **kwargs)
  File "Z:\tmp\wenv-88fbf1b9\lib\site-packages\PyInstaller\depend\analysis.py", line 382, in _safe_import_hook
    return super()._safe_import_hook(target_module_partname, source_module, target_attr_names, level, edge_attr)
  File "Z:\tmp\wenv-88fbf1b9\lib\site-packages\PyInstaller\lib\modulegraph\modulegraph.py", line 2301, in _safe_import_hook
    target_modules = self.import_hook(
  File "Z:\tmp\wenv-88fbf1b9\lib\site-packages\PyInstaller\lib\modulegraph\modulegraph.py", line 1518, in import_hook
    submodule = self._safe_import_module(head, mname, submodule)
  File "Z:\tmp\wenv-88fbf1b9\lib\site-packages\PyInstaller\depend\analysis.py", line 429, in _safe_import_module
    return super()._safe_import_module(module_basename, module_name, parent_package)
  File "Z:\tmp\wenv-88fbf1b9\lib\site-packages\PyInstaller\lib\modulegraph\modulegraph.py", line 2062, in _safe_import_module
    self._process_imports(n)
  File "Z:\tmp\wenv-88fbf1b9\lib\site-packages\PyInstaller\lib\modulegraph\modulegraph.py", line 2850, in _process_imports
    target_modules = self._safe_import_hook(*import_info, **kwargs)
  File "Z:\tmp\wenv-88fbf1b9\lib\site-packages\PyInstaller\depend\analysis.py", line 382, in _safe_import_hook
    return super()._safe_import_hook(target_module_partname, source_module, target_attr_names, level, edge_attr)
  File "Z:\tmp\wenv-88fbf1b9\lib\site-packages\PyInstaller\lib\modulegraph\modulegraph.py", line 2301, in _safe_import_hook
    target_modules = self.import_hook(
  File "Z:\tmp\wenv-88fbf1b9\lib\site-packages\PyInstaller\lib\modulegraph\modulegraph.py", line 1518, in import_hook
    submodule = self._safe_import_module(head, mname, submodule)
  File "Z:\tmp\wenv-88fbf1b9\lib\site-packages\PyInstaller\depend\analysis.py", line 429, in _safe_import_module
    return super()._safe_import_module(module_basename, module_name, parent_package)
  File "Z:\tmp\wenv-88fbf1b9\lib\site-packages\PyInstaller\lib\modulegraph\modulegraph.py", line 2062, in _safe_import_module
    self._process_imports(n)
  File "Z:\tmp\wenv-88fbf1b9\lib\site-packages\PyInstaller\lib\modulegraph\modulegraph.py", line 2850, in _process_imports
    target_modules = self._safe_import_hook(*import_info, **kwargs)
  File "Z:\tmp\wenv-88fbf1b9\lib\site-packages\PyInstaller\depend\analysis.py", line 382, in _safe_import_hook
    return super()._safe_import_hook(target_module_partname, source_module, target_attr_names, level, edge_attr)
  File "Z:\tmp\wenv-88fbf1b9\lib\site-packages\PyInstaller\lib\modulegraph\modulegraph.py", line 2301, in _safe_import_hook
    target_modules = self.import_hook(
  File "Z:\tmp\wenv-88fbf1b9\lib\site-packages\PyInstaller\lib\modulegraph\modulegraph.py", line 1518, in import_hook
    submodule = self._safe_import_module(head, mname, submodule)
  File "Z:\tmp\wenv-88fbf1b9\lib\site-packages\PyInstaller\depend\analysis.py", line 429, in _safe_import_module
    return super()._safe_import_module(module_basename, module_name, parent_package)
  File "Z:\tmp\wenv-88fbf1b9\lib\site-packages\PyInstaller\lib\modulegraph\modulegraph.py", line 2062, in _safe_import_module
    self._process_imports(n)
  File "Z:\tmp\wenv-88fbf1b9\lib\site-packages\PyInstaller\lib\modulegraph\modulegraph.py", line 2850, in _process_imports
    target_modules = self._safe_import_hook(*import_info, **kwargs)
  File "Z:\tmp\wenv-88fbf1b9\lib\site-packages\PyInstaller\depend\analysis.py", line 382, in _safe_import_hook
    return super()._safe_import_hook(target_module_partname, source_module, target_attr_names, level, edge_attr)
  File "Z:\tmp\wenv-88fbf1b9\lib\site-packages\PyInstaller\lib\modulegraph\modulegraph.py", line 2301, in _safe_import_hook
    target_modules = self.import_hook(
  File "Z:\tmp\wenv-88fbf1b9\lib\site-packages\PyInstaller\lib\modulegraph\modulegraph.py", line 1518, in import_hook
    submodule = self._safe_import_module(head, mname, submodule)
  File "Z:\tmp\wenv-88fbf1b9\lib\site-packages\PyInstaller\depend\analysis.py", line 429, in _safe_import_module
    return super()._safe_import_module(module_basename, module_name, parent_package)
  File "Z:\tmp\wenv-88fbf1b9\lib\site-packages\PyInstaller\lib\modulegraph\modulegraph.py", line 2062, in _safe_import_module
    self._process_imports(n)
  File "Z:\tmp\wenv-88fbf1b9\lib\site-packages\PyInstaller\lib\modulegraph\modulegraph.py", line 2850, in _process_imports
    target_modules = self._safe_import_hook(*import_info, **kwargs)
  File "Z:\tmp\wenv-88fbf1b9\lib\site-packages\PyInstaller\depend\analysis.py", line 382, in _safe_import_hook
    return super()._safe_import_hook(target_module_partname, source_module, target_attr_names, level, edge_attr)
  File "Z:\tmp\wenv-88fbf1b9\lib\site-packages\PyInstaller\lib\modulegraph\modulegraph.py", line 2301, in _safe_import_hook
    target_modules = self.import_hook(
  File "Z:\tmp\wenv-88fbf1b9\lib\site-packages\PyInstaller\lib\modulegraph\modulegraph.py", line 1518, in import_hook
    submodule = self._safe_import_module(head, mname, submodule)
  File "Z:\tmp\wenv-88fbf1b9\lib\site-packages\PyInstaller\depend\analysis.py", line 429, in _safe_import_module
    return super()._safe_import_module(module_basename, module_name, parent_package)
  File "Z:\tmp\wenv-88fbf1b9\lib\site-packages\PyInstaller\lib\modulegraph\modulegraph.py", line 2062, in _safe_import_module
    self._process_imports(n)
  File "Z:\tmp\wenv-88fbf1b9\lib\site-packages\PyInstaller\lib\modulegraph\modulegraph.py", line 2850, in _process_imports
    target_modules = self._safe_import_hook(*import_info, **kwargs)
  File "Z:\tmp\wenv-88fbf1b9\lib\site-packages\PyInstaller\depend\analysis.py", line 382, in _safe_import_hook
    return super()._safe_import_hook(target_module_partname, source_module, target_attr_names, level, edge_attr)
  File "Z:\tmp\wenv-88fbf1b9\lib\site-packages\PyInstaller\lib\modulegraph\modulegraph.py", line 2301, in _safe_import_hook
    target_modules = self.import_hook(
  File "Z:\tmp\wenv-88fbf1b9\lib\site-packages\PyInstaller\lib\modulegraph\modulegraph.py", line 1518, in import_hook
    submodule = self._safe_import_module(head, mname, submodule)
  File "Z:\tmp\wenv-88fbf1b9\lib\site-packages\PyInstaller\depend\analysis.py", line 429, in _safe_import_module
    return super()._safe_import_module(module_basename, module_name, parent_package)
  File "Z:\tmp\wenv-88fbf1b9\lib\site-packages\PyInstaller\lib\modulegraph\modulegraph.py", line 2062, in _safe_import_module
    self._process_imports(n)
  File "Z:\tmp\wenv-88fbf1b9\lib\site-packages\PyInstaller\lib\modulegraph\modulegraph.py", line 2850, in _process_imports
    target_modules = self._safe_import_hook(*import_info, **kwargs)
  File "Z:\tmp\wenv-88fbf1b9\lib\site-packages\PyInstaller\depend\analysis.py", line 382, in _safe_import_hook
    return super()._safe_import_hook(target_module_partname, source_module, target_attr_names, level, edge_attr)
  File "Z:\tmp\wenv-88fbf1b9\lib\site-packages\PyInstaller\lib\modulegraph\modulegraph.py", line 2301, in _safe_import_hook
    target_modules = self.import_hook(
  File "Z:\tmp\wenv-88fbf1b9\lib\site-packages\PyInstaller\lib\modulegraph\modulegraph.py", line 1518, in import_hook
    submodule = self._safe_import_module(head, mname, submodule)
  File "Z:\tmp\wenv-88fbf1b9\lib\site-packages\PyInstaller\depend\analysis.py", line 429, in _safe_import_module
    return super()._safe_import_module(module_basename, module_name, parent_package)
  File "Z:\tmp\wenv-88fbf1b9\lib\site-packages\PyInstaller\lib\modulegraph\modulegraph.py", line 2062, in _safe_import_module
    self._process_imports(n)
  File "Z:\tmp\wenv-88fbf1b9\lib\site-packages\PyInstaller\lib\modulegraph\modulegraph.py", line 2850, in _process_imports
    target_modules = self._safe_import_hook(*import_info, **kwargs)
  File "Z:\tmp\wenv-88fbf1b9\lib\site-packages\PyInstaller\depend\analysis.py", line 382, in _safe_import_hook
    return super()._safe_import_hook(target_module_partname, source_module, target_attr_names, level, edge_attr)
  File "Z:\tmp\wenv-88fbf1b9\lib\site-packages\PyInstaller\lib\modulegraph\modulegraph.py", line 2301, in _safe_import_hook
    target_modules = self.import_hook(
  File "Z:\tmp\wenv-88fbf1b9\lib\site-packages\PyInstaller\lib\modulegraph\modulegraph.py", line 1518, in import_hook
    submodule = self._safe_import_module(head, mname, submodule)
  File "Z:\tmp\wenv-88fbf1b9\lib\site-packages\PyInstaller\depend\analysis.py", line 429, in _safe_import_module
    return super()._safe_import_module(module_basename, module_name, parent_package)
  File "Z:\tmp\wenv-88fbf1b9\lib\site-packages\PyInstaller\lib\modulegraph\modulegraph.py", line 2061, in _safe_import_module
    n = self._scan_code(module, co, co_ast)
  File "Z:\tmp\wenv-88fbf1b9\lib\site-packages\PyInstaller\lib\modulegraph\modulegraph.py", line 2645, in _scan_code
    self._scan_bytecode(
  File "Z:\tmp\wenv-88fbf1b9\lib\site-packages\PyInstaller\lib\modulegraph\modulegraph.py", line 2749, in _scan_bytecode
    for inst in util.iterate_instructions(module_code_object):
  File "Z:\tmp\wenv-88fbf1b9\lib\site-packages\PyInstaller\lib\modulegraph\util.py", line 149, in iterate_instructions
    yield from iterate_instructions(constant)
  File "Z:\tmp\wenv-88fbf1b9\lib\site-packages\PyInstaller\lib\modulegraph\util.py", line 141, in iterate_instructions
    yield from (i for i in get_instructions(code_object) if i.opname != "EXTENDED_ARG")
  File "Z:\tmp\wenv-88fbf1b9\lib\site-packages\PyInstaller\lib\modulegraph\util.py", line 141, in <genexpr>
    yield from (i for i in get_instructions(code_object) if i.opname != "EXTENDED_ARG")
  File "dis.py", line 338, in _get_instructions_bytes
  File "dis.py", line 292, in _get_const_info
IndexError: tuple index out of range
```