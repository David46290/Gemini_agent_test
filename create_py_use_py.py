
import subprocess



# main.py
new_code = """
def run():
    return "Hello from new script!"
    
if __name__ == "__main__":
    print(run())
"""

with open("new_script.py", "w", encoding="utf-8") as f:
    f.write(new_code)


result = subprocess.run(["python", "new_script.py"], capture_output=True, text=True)
print("回傳值:", result.stdout.strip())