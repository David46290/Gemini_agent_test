import subprocess, sys
import os

def make_new_code(new_addon='', addon_name=''):
    func_def = f"def {addon_name}():"
    
    # main.py
    the_main = f"""if __name__ == "__main__":\n
    try:
        print({addon_name}())
    except Exception as e:
        print({{e}})
    """
    new_code = func_def + '\n' + new_addon + '\n' + the_main
    
    with open("new_script.py", "w", encoding="utf-8") as f:
        f.write(new_code)

def run_new_code():
    result = subprocess.run([sys.executable, "new_script.py"], capture_output=True, text=True, cwd=os.getcwd()).stdout.strip() # string
    error_alarm = "|Error Encountered|:"
    if 'Error' in result:
        print(error_alarm)
    if 'ModuleNotFoundError' in result:
        missing_module = result.split('named')[-1].split('\'')[1]
        print(f'Please download {missing_module} first')
    print(result)

if __name__ == "__main__":
    addon_name = 'new_func'
    new_addon = """
    
    import scipy as sci
    arr = np.arange(1, 11)
    print(arr)
    return 'function successed'
    """
    make_new_code(new_addon, addon_name)
    run_new_code()
    
