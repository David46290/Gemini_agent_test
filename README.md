[Demo video](https://youtu.be/it04FmA0d_M?si=Zr59NV5qC7rKL4kh "link" ).

Run gemini_agent.py, and then ask Gemini to write a Python code.

The new code will be written in temp_script.py, and then get executed.

The execution result will be shown in the chat.

.env file content: GEMINI_API_KEY=YOUR_ACTUAL_API_KEY_HERE. Make sure it is put it shares the same working directory as gemini_agent.py

```
${Gemini_agent_test root}
├── .env
├── gemini_agent.py
├── README.md
├── temp_script.py
├── create_py_use_py.py

```
