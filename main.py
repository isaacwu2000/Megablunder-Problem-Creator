from model import generate_hard_length, generate_hard_trick, generate_medium

for i in range(3):
    generate_medium("FRAG")
    print("FRAG", i)
"""
topics = ["A", "FRAG", "ROS", "PR", "AGR", "PAR", "CASE", "MM", "DM"]

for topic in topics[2:]:
    for i in range(20):
        generate_medium(topic)
        print(topic, i)
"""