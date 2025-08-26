from model import generate_hard_length, generate_hard_trick

topics = ["A", "FRAG", "ROS", "PR", "AGR", "PAR", "CASE", "MM", "DM"]

for topic in topics:
    for i in range(20):
        generate_hard_trick(topic)
        print(topic, i)

# todo: generate medium problems