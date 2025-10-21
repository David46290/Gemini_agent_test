
import subprocess



# main.py
new_func = """
def run():
    return 'function successed'//2
"""

the_main = """
if __name__ == "__main__":
    try:
        print(run())
    except Exception as e:
        print(f"|error encountered| {e}")
"""

new_code = new_func + '\n' + the_main

with open("new_script.py", "w", encoding="utf-8") as f:
    f.write(new_code)


result = subprocess.run(["python", "new_script.py"], capture_output=True, text=True)
print(result.stdout.strip())
