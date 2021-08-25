#
# 何の関数のテストなのか見やすくするデコレータ
#

from typing import Optional

def termdecorate(testfunc):
    try:
        module_name: Optional[str] = testfunc.__module__
        func_name: str = testfunc.__name__
    except AttributeError:
        module_name: Optional[str] = None
        func_name: str = str(testfunc)

    def wrapper(self, *args, **kwargs):
        print(f"\n--- \033[32mSTART\033[0m: {func_name} (module: {module_name or 'unknown'}) ---\n")

        testfunc(self, *args, **kwargs)
        
        print("\n--- finished ---")

    return wrapper
