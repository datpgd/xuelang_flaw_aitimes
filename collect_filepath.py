import os
import shutil

f_true = open('true_file.text', 'w', encoding='utf-8')  # 追加模式
f_false = open('false_file.text', 'w', encoding='utf-8')  # 追加模式
train_dirs = ["xuelang_round1_train_part1_20180628", "xuelang_round1_train_part2_20180705",
              "xuelang_round1_train_part3_20180709"]

true_count = 0
false_count = 0
for d1 in train_dirs:
    for d2 in os.listdir("./{0}".format(d1)):
        if d2 == "正常":
            for f in os.listdir("./{0}/{1}".format(d1, d2)):
                if f.lower().endswith(".jpg"):
                    true_count += 1
                    f_true.write("./{0}/{1}/{2}\n".format(d1, d2, f))
        else:
            for f in os.listdir("./{0}/{1}".format(d1, d2)):
                if f.lower().endswith(".jpg"):
                    false_count += 1
                    f_false.write("./{0}/{1}/{2}\n".format(d1, d2, f))

print("true_count={0}, false_count={1}".format(true_count, false_count))
f_true.close()
f_false.close()
