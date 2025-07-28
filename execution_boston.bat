set input_table=boston
set input_path=../../input/boston.csv
set target=MEDV
set model=linear_regression
set target_type=continuos

cd .venv/Scripts/
python.exe ../../main.py --input_path=%input_path% --input_table=%input_table% --target=%target% --model=%model% --target_type=%target_type%