import os
import pandas as pd
import xml.etree.ElementTree as ET

questions = []
answers = []

dataset_path = "data"

for root_dir, dirs, files in os.walk(dataset_path):

    for file in files:

        if file.endswith(".xml"):

            filepath = os.path.join(root_dir, file)

            try:
                tree = ET.parse(filepath)
                root = tree.getroot()

                qa_pairs = root.find("QAPairs")

                if qa_pairs is not None:

                    for qa in qa_pairs.findall("QAPair"):

                        question = qa.find("Question")
                        answer = qa.find("Answer")

                        if question is not None and answer is not None:

                            questions.append(question.text)
                            answers.append(answer.text)

            except Exception as e:
                print("Error:", filepath)
                print(e)

df = pd.DataFrame({
    "question": questions,
    "answer": answers
})

df.to_csv("medical_qa.csv", index=False)

print(f"\nDataset created successfully!")
print(f"Total Q&A pairs: {len(df)}")