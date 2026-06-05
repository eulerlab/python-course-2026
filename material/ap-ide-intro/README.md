## Setup (do this once, in order)

1. **Unzip** this folder and remember where you put it.
2. In VS Code: **File → Open Folder…** and choose this `ap-ide-intro` folder
   (the folder itself, not a file inside it, and not the `.zip`).
3. Open a terminal in VS Code: **Terminal → New Terminal**.
4. Create the environment and install the packages:
   ```
   uv venv
   uv pip install -r requirements.txt
   ```
5. Open `ap_analysis/ap_analysis.ipynb`.
6. **Select the kernel** (top-right of the notebook): click **Select Kernel →
   Python Environments → ap-ide-intro\.venv\... .
   If you do not see this option click the little refresh icon on the top right.

## What you will do

- **Task 1–3:** run plots and *Ctrl-click* (Mac: *Cmd-click*) into the functions
  in `utils.py` to understand how each plot is made, then write a one- or
  two-sentence "methods" description.
- **Debug 1–3:** three broken versions of the same function. Use the debugger
  (breakpoints + the Variables panel) to find the single bug in each.

Everything you need is in `ap_analysis/`.
