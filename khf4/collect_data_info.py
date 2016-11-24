# Open training labels

f = open("assets/dict.csv")
label_dict = {}
for line in f:
    next_label =line.split()
    label_dict[next_label[0]]=next_label[1]
f.close()
print("Data labels - OK")

# Collect training data URL - label pairs

#ID-label pairs
train_data_ID = {}
with open("machine_ann_2016_08/train/labels.csv") as f:
    for line in f:
        next_line = line.split(',')
        if(label_dict.get(next_line[2])!=None):
            
            train_data_ID[next_line[0]]=label_dict.get(next_line[2])
#URL-label pairs
train_data_URL = []
with open("images_2016_08/train/images.csv") as f:
    for line in f:
        next_line = line.split(',')
        if(train_data_ID.get(next_line[0])!=None):
            if(next_line[10]!=""):
                train_data_URL.append([next_line[10].rstrip(),train_data_ID.get(next_line[0])])
#Save into file
with open("assets/train_url_labels.csv",'w') as f:
    for line in train_data_URL:
        f.write("{},{}\n".format(line[0],line[1]))
print("Train data - OK")

#Collect validation data URL - label pairs

validation_data_ID = {}
with open("machine_ann_2016_08/validation/labels.csv") as f:
    for line in f:
        next_line = line.split(',')
        if(label_dict.get(next_line[2])!=None):
            
            validation_data_ID[next_line[0]]=label_dict.get(next_line[2])
validation_data_URL = []
with open("images_2016_08/validation/images.csv") as f:
    for line in f:
        next_line = line.split(',')
        if(validation_data_ID.get(next_line[0])!=None):
            if(next_line[10]!=""):
                validation_data_URL.append([next_line[10].rstrip(),validation_data_ID.get(next_line[0])])
with open("assets/validation_url_labels.csv",'w') as f:
    for line in validation_data_URL:
        f.write("{},{}\n".format(line[0],line[1]))
print("Validation data - OK")
