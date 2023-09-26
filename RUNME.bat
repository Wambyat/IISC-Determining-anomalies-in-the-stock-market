@echo off
start cmd /k "echo This news server && cd "\Main Code\iiscproj" && node sideserver.js"
start cmd /k "echo This is Flask server && cd "\Main Code\Flask" && python3 app.py"
echo "This is Vue server"
cd "\Main Code\iiscproj"
npm run serve
