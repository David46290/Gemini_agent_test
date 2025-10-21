import subprocess, sys
import os

def make_new_code(new_addon='', addon_name=''):
    func_def = f"def {addon_name}():"
    
    # main.py
    the_main = f"""if __name__ == "__main__":\n
    try:
        {addon_name}()
        print('execution successful')
    except Exception as e:
        print({{e}})
    """
    new_code = func_def + '\n' + new_addon + '\n' + the_main
    
    with open("new_script.py", "w", encoding="utf-8") as f:
        f.write(new_code)

def run_new_code(code_name="new_script.py",  retry_time=0, retry_limit=1):
    result = subprocess.run([sys.executable, code_name], capture_output=True, text=True, cwd=os.getcwd()).stdout.strip() # string
    error_alarm = "|Error Encountered|"
    is_error = False
    if 'Error' in result:
        print(error_alarm)
        is_error = True
        if 'ModuleNotFoundError' in result:
            missing_module = result.split('named')[-1].split('\'')[1]
            print(f'Try downloading {missing_module}......retry time:{retry_time}')
            install_missing_module(missing_module, retry_time=retry_time, retry_limit=retry_limit)
    else:
        # print(result + str(retry_time))
        print(result)
    return is_error

def install_missing_module(module_name, retry_time, retry_limit=0):
    # using pip install
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", module_name])
        print(f'{module_name} downloaded, trying re-execute the program......')
        while retry_time <= retry_limit:
            is_error = run_new_code(retry_time=retry_time+1, retry_limit=retry_limit)
            if not is_error:
                return
        print(f'Error: More than {retry_limit} attempt failed, stop the program')
            
    except Exception as e:
        print(f'Error encountered when installing {module_name}')
        print(e)

def build_new_addon():
    new_addon = """
    import numpy as np
    import scipy
    import matplotlib
    arr = np.arange(1, 11)
    print(arr)
    return 'function succeed'
    """
    return new_addon

if __name__ == "__main__":
    addon_name = 'new_func'
    new_addon = build_new_addon()
    make_new_code(new_addon, addon_name)
    run_new_code(retry_limit=2)
    
