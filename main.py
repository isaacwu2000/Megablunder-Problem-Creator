from model import generate_hard_length

topics = ["A", "FRAG", "ROS", "PR", "AGR", "PAR", "CASE", "MM", "DM"]

for topic in topics[1:]:
    for i in range(20):
        generate_hard_length(topic)
        print(topic, i)