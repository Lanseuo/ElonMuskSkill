zip -X -r index.zip * -x venv/**\* -x skill.zip
aws lambda update-function-code --function-name ElonMuskSkill --zip-file fileb://index.zip
rm index.zip