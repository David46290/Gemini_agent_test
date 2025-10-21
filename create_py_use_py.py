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

def run_new_code(retry_time=0):
    result = subprocess.run([sys.executable, "new_script.py"], capture_output=True, text=True, cwd=os.getcwd()).stdout.strip() # string
    error_alarm = "|Error Encountered|"
    is_error = False
    if 'Error' in result:
        print(error_alarm)
        is_error = True
        if 'ModuleNotFoundError' in result:
            missing_module = result.split('named')[-1].split('\'')[1]
            print(f'Try downloading {missing_module}......')
            install_missing_module(missing_module, retry_time)
    else:
        print(result)
    return is_error

def install_missing_module(module_name, retry_time):
    retry_limit = 1
    # using pip install
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", module_name])
        print(f'{module_name} downloaded, trying re-execute the program......')
        while retry_time <= retry_limit:
            is_error = run_new_code(retry_time+1)
            if not is_error:
                return
        print(f'Error: More than {retry_limit} attempt failed, stop the program')
            
    except Exception as e:
        print(f'Error encountered when installing {module_name}')
        print(e)

if __name__ == "__main__":
    addon_name = 'new_func'
    new_addon = """
    
    import numpy as np
    arr = np.arange(1, 11)
    print(arr)
    return 'function successed'
    """
    make_new_code(new_addon, addon_name)
    run_new_code()
    
