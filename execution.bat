set input_table=titanic
set input_path=../../input/titanic.csv
set target=Survived
set model=logistic_regression
set target_type=binary

cd .venv/Scripts/
python.exe ../../main.py --input_path=%input_path% --input_table=%input_table% --target=%target% --model=%model% --target_type=%target_type%