from model import generate_hard_length, generate_hard_trick, generate_medium

topics = ["A", "FRAG", "ROS", "PR", "AGR", "PAR", "CASE", "MM", "DM"]

for topic in topics:
    for i in range(20):
        generate_medium(topic)
        print(topic, i)