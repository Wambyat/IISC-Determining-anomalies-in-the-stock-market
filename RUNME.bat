@echo off
start cmd /k "echo This news server && cd "\Main Code\iiscproj" && node sideserver.js"
start cmd /k "echo This is Flask server && cd "\Main Code\Scripts" && activate.bat"
echo "This is Vue server"
cd "\Main Code\iiscproj"
npm run serve
