@echo off
for /l %%x in (1, 1, 10) do (
    start cmd /k "python pets.py"
)
