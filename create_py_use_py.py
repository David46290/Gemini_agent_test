import subprocess

def make_new_code(new_addon='', addon_name=''):
    func_def = f"def {addon_name}():"
    
    # main.py
    the_main = f"""if __name__ == "__main__":\n
    try:
        print({addon_name}())
    except Exception as e:
        print("|error encountered|:" + e)
    """
    new_code = func_def + '\n' + new_addon + '\n' + the_main
    
    with open("new_script.py", "w", encoding="utf-8") as f:
        f.write(new_code)

def run_new_code():
    result = subprocess.run(["python", "new_script.py"], capture_output=True, text=True) # string
    error_alarm = "|error encountered|:"
    print(result.stdout.strip())

if __name__ == "__main__":
    addon_name = 'new_func'
    new_addon = """
    return 'function successed'
    """
    make_new_code(new_addon, addon_name)
    run_new_code()
    
